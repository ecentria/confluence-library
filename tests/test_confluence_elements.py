import unittest

from src.confluence import ConfluenceElements


class TestSimple(unittest.TestCase):
    def test_render_colored_cell_default(self):
        self.assertEqual(ConfluenceElements.render_colored_cell('green', 'Test1'), "<span style=\"color:green\"><b>Test1</b></span>")

    def test_render_colored_cell_bold(self):
        self.assertEqual(ConfluenceElements.render_colored_cell('red', 'Test2', True), "<span style=\"color:red\"><b>Test2</b></span>")

    def test_render_colored_cell_not_bold(self):
        self.assertEqual(ConfluenceElements.render_colored_cell('orange', 'Test3', False), "<span style=\"color:orange\">Test3</span>")

    def test_render_empty_list(self):
        self.assertEqual(ConfluenceElements.render_list([]), "")

    def test_render_list(self):
        self.assertEqual(ConfluenceElements.render_list(["test1", "test2"]), "<ul><li>test1</li><li>test2</li></ul>")

    def test_render_empty_list_and_header(self):
        self.assertEqual(
            ConfluenceElements.render(
                'Title',
                1,
                [],
                []
            ),
            "<h1>Title</h1><table><tr></tr></table>"
        )

    def test_render_empty_list(self):
        self.assertEqual(
            ConfluenceElements.render(
                'Title',
                2,
                ["Box1", "Box2"],
                []
            ),
            "<h2>Title</h2><table><tr><th>Box1</th><th>Box2</th></tr></table>"
        )

    def test_render(self):
        self.assertEqual(
            ConfluenceElements.render(
                'Title',
                3,
                ["Box1", "Box2"],
                ["box 1 text", "box 2 text"]
            ),
            "<h3>Title</h3><table><tr><th>Box1</th><th>Box2</th></tr><tr><td>b</td><td>o</td><td>x</td><td> </td><td>1</td><td> </td><td>t</td><td>e</td><td>x</td><td>t</td></tr><tr><td>b</td><td>o</td><td>x</td><td> </td><td>2</td><td> </td><td>t</td><td>e</td><td>x</td><td>t</td></tr></table>"
        )


if __name__ == '__main__':
    unittest.main()
