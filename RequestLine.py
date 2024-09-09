
class RequestLine:
    request_method: str
    http_endpoint: str
    http_version: str

    def __init__(self, request_method: str, http_endpoint: str, http_version: str) -> None:
        self.request_method = request_method
        self.http_endpoint = http_endpoint
        self.http_version = http_version