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
            case _:
                return "invalid"
            
            
    def parseRequest(request: str) -> RequestLine:
        request_line: RequestLine

        if request.__contains__("\n"):
            # splits the request header for each new line. 
            http_header_lines = request.split("\n") 
            for idx, line in enumerate(http_header_lines):
                if idx == 0: # Request line is always at the first line. 
                    if line.__contains__("/"):
                        print(f"REQUEST: {line}")
                        endpoint_start_idx = line.find('/')
                        request_method = line[0:endpoint_start_idx].strip()
                        http_version = "0.9"

                        if line.__contains__("HTTP/"):
                            http_version_idx = line.find("H")
                            if http_version_idx == 0:
                                http_version_idx = line.rfind("H") #Incase the request method is "HEAD"

                            http_version = line[http_version_idx:-1]


                        if http_version == "0.9":
                            http_endpoint = line[endpoint_start_idx:-1].strip()
                        else:
                            http_endpoint = line[endpoint_start_idx:http_version_idx].strip()
                            
                        request_line = RequestLine(request_method, http_endpoint, http_version)
                    else:
                        return "invalid"
                print(request_line.__str__())
        return request_line
    
    def invalid_request() -> str:
        return "400 Bad Request"
   
        
    def mapping(method: str, endpoint: str):
        def decorator(function):
            RouterRegister.addRoute(method, endpoint, function)
            def wrapper(*args, **kwargs):
                print(*args, **kwargs)
                val = function()
                return val
            return wrapper
        return decorator

