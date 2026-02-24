from enum import Enum
from datetime import datetime
from .confluence_elements import ConfluenceElements
import requests


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
        Publishes the prepared content to Confluence Cloud. If you want to test the content first,
        please check printContent()
        """
        try:
            if self.__page_id:
                try:
                    # Make GET request to retrieve current page info and version number
                    page_info = requests.get(self.__url, auth=(self.__api_username, self.__api_password)).json()
                    current_version = page_info['version']['number']
                    # Prepare update payload
                    update_payload = {
                        "id": self.__page_id,
                        "status": "current",
                        "title": self.__page_title,
                        "body": {
                            "representation": "storage",
                            "value": self.__content,
                        },
                        "version": {
                            "number": current_version + 1,
                        },
                    }
                    # Make PUT request to update the page
                    response = requests.put(self.__url, json=update_payload, auth=(self.__api_username, self.__api_password))
                    response.raise_for_status()
                except Exception as e:
                    raise Exception(f"An error occurred during page update: {e}")
            else:
                raise Exception("Page ID is not specified!")

        except Exception as e:
            print(f"An error occurred: {e}")

    def get_content(self) -> str:
        """
        Returns the prepared content as a string. Can be used for test purposes
        """
        return self.__content

    def printContent(self) -> None:
        """
        Can be used for test purposes
        """
        print(self.__content)
