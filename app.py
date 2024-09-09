from framework.server import init_server
from framework.http import Http




@Http.mapping(method=Http.GET, endpoint="/")
def index() -> str:
    return "index"


@Http.mapping(method=Http.GET, endpoint="/err")
def errPage() -> str:
    return "error"


init_server()