from enum import Enum
from datetime import datetime
from .confluence_elements import ConfluenceElements
from atlassian import Confluence


class HeaderSize(Enum):
    H1 = 1
    H2 = 2
    H3 = 3
    H4 = 4


class ConfluenceGenerator():
    """
    A simple class for preparing the content and publishing it to Confluence then
    """

    def __init__(self, url: str, api_username: str, api_password: str, page_id: str, page_title: str) -> None:
        self.__content = '<ac:structured-macro ac:name=\"toc\"><ac:parameter ac:name=\"levels\">2</ac:parameter></ac:structured-macro>'
        self.__content += '<p>Automatically generated at %s</p>' % datetime.now().strftime('%m/%d/%Y %H:%M:%S')
        self.__url = url
        self.__api_username = api_username
        self.__api_password = api_password
        self.__page_id = page_id
        self.__page_title = page_title

        self.app = Confluence(
            url=self.__url,
            username=self.__api_username,
            password=self.__api_password,
        )

    def append_string(self, content: str) -> None:
        """
        Appends a single string to the content
        """
        self.__content += content

    def append_block(self, title_size: HeaderSize, title_text: str,
                     table_headers: list[str], table_data: list) -> None:
        """
        Renders and appends a block to the content
        """
        self.__content += ConfluenceElements.render(
            title_size=title_size.value,
            title_text=title_text,
            table_headers=table_headers,
            table_data=table_data,
        )

    def update_page(self):
        """
        Publishes the prepared content. If you want to test the content first,
        please check printContent()
        """
        return self.app.update_page(
            page_id=self.__page_id,
            title=self.__page_title,
            body=self.__content
        )

    def printContent(self) -> None:
        """
        Can be used for test purposes
        """
        print(self.__content)
