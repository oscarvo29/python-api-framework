from typing import Callable

# class singleton(class_):
#     instances = {}
#     def getInstance(*args, **kwargs):
#         if class_ not in instances:
#             isinstance[class_] = class_(*args, **kwargs)
#         return instances[class_]
#     return getInstance

# @singleton
# class RouteRegister(BaseClass):
#     pass



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

    routes: list[Route] = []


    @staticmethod
    def addRoute(method: str, endpoint: str, func: Callable):
        route = RouterRegister.Route(method, endpoint, func)
        RouterRegister.routes.append(route)

    @staticmethod
    def getAllRoutes() -> list[Route]: 
        list = RouterRegister.routes
        return list
