from .RequestLine import RequestLine
from .RouterRegister import RouterRegister


class Http:
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"
    HEAD = "HEAD"

    PORT = 8000


    def findHttpMethod(self, request_method: str) -> str:
        match request_method.upper():
            case "GET":
                return self.GET
            case "POST":
                return self.POST
            case "PUT":
                return self.PUT
            case "DELETE":
                return self.DELETE
            case "PATCH":
                return self.PATCH
            case "HEAD":
                return self.HEAD
            
    def parseRequest(request: str) -> RequestLine:
        request_line: RequestLine

        # splits the request header for each new line. 
        http_header_lines = request.split("\n") 
        for idx, line in enumerate(http_header_lines):
            if idx == 0: # Request line is always at the first line. 
                """ 
                    Lav nogle test her, og sikre dig det er en valid http request.
                    hvis det ikke er, så skal der returneres en 400 error code.
                """

                

                endpoint_start_idx = line.find('/')
                request_method = line[0:endpoint_start_idx]
                http_version_idx = line.find("H")
                http_endpoint = line[endpoint_start_idx:http_version_idx].strip()
                
                http_version = line[http_version_idx:-1]

                request_line = RequestLine(request_method, http_endpoint, http_version)
        
        return request_line
   
        
    def mapping(method: str, endpoint: str):
        def decorator(function):
            RouterRegister.addRoute(method, endpoint, function)
            def wrapper(*args, **kwargs):
                print(*args, **kwargs)
                val = function()
                return val
            return wrapper
        return decorator

