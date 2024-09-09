from http import Http


"""
Bliver først kaldt når functionen bliver kaldt, jeg skal finde en måde 
hvorpå serveren kender functionen før den bliver kaldt, eller kald den på
server start.

måske det her kan finde alle python filer under et dir:
https://sentry.io/answers/import-files-from-a-different-folder-in-python/

og det her viser hvordan man kan kalde alle filer:
https://stackoverflow.com/questions/28643534/is-there-a-way-in-python-to-execute-all-functions-in-a-file-without-explicitly-c

Det virker ikke til at være super god practice, men kunne være en fin måde at håndtere flere routes pt.

Decorator funktionen, skal så smide methoden, endpoint og funktion lokalitionen,
over i et endpoint, hvor en anden funktion så vil kunne finde den rigtige 
funktion, der tilhører den http metode + endpoint.

Derefter, skal der også laves en funktion som kan returnere http header, samt 
html siden.
"""


@Http.mapping(method=Http.GET, endpoint="/")
def index() -> str:
    return "path"