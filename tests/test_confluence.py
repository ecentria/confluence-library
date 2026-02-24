import unittest

from unittest.mock import patch, MagicMock
from src.confluence import HeaderSize, ConfluenceGenerator, ConfluenceElements
from freezegun import freeze_time


class TestSimple(unittest.TestCase):
    def test_H1(self):
        self.assertEqual(HeaderSize.H1.value, 1)

    def test_H2(self):
        self.assertEqual(HeaderSize.H2.value, 2)

    def test_H3(self):
        self.assertEqual(HeaderSize.H3.value, 3)

    def test_H4(self):
        self.assertEqual(HeaderSize.H4.value, 4)

    def test_H5_fail(self):
        self.assertRaises(AttributeError)

    @freeze_time("2012-01-01")
    def test_append_string(self):
        confluence = ConfluenceGenerator("url", "api_username", "api_password", "page_id", "page_title")
        confluence.append_string("test")

        self.assertEqual("url", confluence._ConfluenceGenerator__url)
        self.assertEqual("api_username", confluence._ConfluenceGenerator__api_username)
        self.assertEqual("api_password", confluence._ConfluenceGenerator__api_password)
        self.assertEqual("page_id", confluence._ConfluenceGenerator__page_id)
        self.assertEqual("page_title", confluence._ConfluenceGenerator__page_title)

        self.assertEqual(
            "<ac:structured-macro ac:name=\"toc\"><ac:parameter ac:name=\"levels\">2</ac:parameter></ac:structured-macro><p>Automatically generated at 01/01/2012 00:00:00</p>test",
            confluence._ConfluenceGenerator__content
        )

    def confluence_elements_render(title_text: str, title_size: int, table_headers: list, table_data: list):
        return "TestRender"

    @freeze_time("2012-01-01")
    @patch.object(ConfluenceElements, 'render', confluence_elements_render)
    def test_append_block(self):
        confluence = ConfluenceGenerator("url", "api_username", "api_password", "page_id", "page_title")
        confluence.append_block(
            HeaderSize.H1,
            "Title",
            ["Box1", "Box2"],
            ["box 1 text", "box 2 text"]
        )

        self.assertEqual("url", confluence._ConfluenceGenerator__url)
        self.assertEqual("api_username", confluence._ConfluenceGenerator__api_username)
        self.assertEqual("api_password", confluence._ConfluenceGenerator__api_password)
        self.assertEqual("page_id", confluence._ConfluenceGenerator__page_id)
        self.assertEqual("page_title", confluence._ConfluenceGenerator__page_title)

        self.assertEqual(
            "<ac:structured-macro ac:name=\"toc\"><ac:parameter ac:name=\"levels\">2</ac:parameter></ac:structured-macro><p>Automatically generated at 01/01/2012 00:00:00</p>TestRender",
            confluence._ConfluenceGenerator__content
        )

    @freeze_time("2012-01-01")
    @patch('src.confluence.confluence.requests.put')
    @patch('src.confluence.confluence.requests.get')
    def test_update_page(self, mock_get, mock_put):
        mock_get.return_value.json.return_value = {'version': {'number': 5}}
        mock_put.return_value.raise_for_status = MagicMock()

        confluence = ConfluenceGenerator("url", "api_username", "api_password", "page_id", "page_title")

        self.assertEqual(
            "<ac:structured-macro ac:name=\"toc\"><ac:parameter ac:name=\"levels\">2</ac:parameter></ac:structured-macro><p>Automatically generated at 01/01/2012 00:00:00</p>",
            confluence._ConfluenceGenerator__content
        )

        confluence.update_page()

        mock_get.assert_called_once_with("url", auth=("api_username", "api_password"))
        mock_put.assert_called_once_with(
            "url",
            json={
                "id": "page_id",
                "status": "current",
                "title": "page_title",
                "body": {
                    "representation": "storage",
                    "value": confluence._ConfluenceGenerator__content,
                },
                "version": {"number": 6},
            },
            auth=("api_username", "api_password"),
        )
        mock_put.return_value.raise_for_status.assert_called_once()
