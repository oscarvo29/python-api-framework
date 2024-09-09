
class HttpHeader:
    http_version: str
    status_code: int
    status_message: str
    content_type: str
    body: str

    def __init__(self, version: str, status_code: int, 
                 status_message: str, content_type:str, body: str) -> None:
        self.http_version = version
        self.status_code = status_code
        self.status_message = status_message
        self.content_type = content_type
        self.body = body

    def getHeader(self) -> str:
        http_header = f"HTTP/{self.http_version} {self.status_code} {self.status_message}\r\nContent-Type: {self.content_type}\r\n\r\n{self.body}"

        return http_header
        