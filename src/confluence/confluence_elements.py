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
