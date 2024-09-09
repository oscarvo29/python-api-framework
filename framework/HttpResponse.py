from .RequestLine import RequestLine
from .RouterRegister import RouterRegister
from .HtmlFinder import get_html_file


class HttpResponse:
    request_line: RequestLine

    def __init__(self, request_line: RequestLine):
        self.request_line = request_line

    def getHttpRespone(self) -> str:

        res, status_code, status_message = RouterRegister.findRoute(self.request_line)
        body = get_html_file(res())
        print(res())
        http_response = f"HTTP/1.0 {status_code} {status_message}\r\nContent-Type: Text/HTML\r\n\r\n{body}"

        return http_response
        