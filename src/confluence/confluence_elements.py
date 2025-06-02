class ConfluenceElements:
    @staticmethod
    def render_colored_cell(color: str, text: str, is_bold: bool = True) -> str:
        content = '<span style="color:%s">' % color
        if is_bold:
            content += '<b>'
        content += '%s' % text
        if is_bold:
            content += '</b>'
        content += '</span>'
        return content

    @staticmethod
    def render(title_text: str, title_size: int, table_headers: list, table_data: list) -> str:
        content = '<h%d>%s</h%d>' % (title_size, title_text, title_size)
        content += '<table><tr>'
        for title in table_headers:
            content += '<th>%s</th>' % title
        content += '</tr>'
        for n in table_data:
            content += '<tr>'
            for m in n:
                content += '<td>%s</td>' % m
            content += '</tr>'
        content += "</table>"

        return content

    @staticmethod
    def render_list(elements: list):
        if len(elements) < 1:
            return ""

        content = "<ul>"
        for element in elements:
            content += "<li>%s</li>" % element
        content += "</ul>"

        return content

    @staticmethod
    def render_note(title: str, body: str) -> str:
        return (f"<ac:structured-macro "
                f"ac:macro-id=\"1fa0a0b5-22c9-4aec-bb4c-c4dcd0fc3b9f\" "
                f"ac:name=\"note\" "
                f"ac:schema-version=\"1\">"
                f"<ac:parameter ac:name=\"title\">{title}</ac:parameter>"
                f"<ac:rich-text-body><p>{body}</p></ac:rich-text-body>"
                f"</ac:structured-macro>")

    @staticmethod
    def render_warning(title: str, body: str) -> str:
        return (f"<ac:structured-macro "
                f"ac:macro-id=\"24b6da5c-23ee-4101-9e4d-77b1f9d24ae0\" "
                f"ac:name=\"warning\" "
                f"ac:schema-version=\"1\">"
                f"<ac:parameter ac:name=\"title\">{title}</ac:parameter>"
                f"<ac:rich-text-body><p>{body}</p></ac:rich-text-body>"
                f"</ac:structured-macro>")
    
    @staticmethod
    def render_image(filename: str) -> str:
        return f"<ac:image><ri:attachment ri:filename=\"{filename}\" /></ac:image>"
