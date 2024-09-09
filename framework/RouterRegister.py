from typing import Union, Callable
from .RequestLine import RequestLine

class RouterRegister:
    class Route:
        method: str
        endpoint: str
        func: Callable 

        def __init__(self, method: str, endpoint: str, func: Callable):
            self.method = method
            self.endpoint = endpoint
            self.func = func

        def __str__(self) -> str:
            return f"Method: {self.method}, Endpoint: {self.endpoint}, Func: {self.func.__name__}"

    routes: dict = {}


    @staticmethod
    def addRoute(method: str, endpoint: str, func: Callable):
        key = f"{method}:{endpoint}"
        route = RouterRegister.Route(method, endpoint, func)
        RouterRegister.routes[key] = route
        print(RouterRegister.routes)

    @staticmethod
    def findRoute(request_line: RequestLine) -> Union[Callable, int, str]:
        key = f"{request_line.request_method.strip()}:{request_line.http_endpoint}"
        if key in RouterRegister.routes:
            return RouterRegister.routes[key].func, 200, "OK"
        else:
            return RouterRegister.routes["GET:/err"].func, 404, "Page Not Found"

    @staticmethod
    def getAllRoutes() -> dict: 
        routes = RouterRegister.routes
        return routes
