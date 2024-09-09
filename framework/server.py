import socket
from .http import Http
from .HttpResponse import HttpResponse



addr = ("", Http.PORT)  # all interfaces, port 8080

def init_server():
    server = socket.create_server(addr, family = socket.AF_INET6)
    server.listen(0)

    print("Server starts to accept connections from clients...")
    while(True):
        client_socket, client_address = server.accept()
        client_request = client_socket.recv(1024).decode("utf-8")
        request_line = Http.parseRequest(client_request)
        http_response = HttpResponse(request_line)
        # http_response = HttpResponse("1.0", 200, "OK", "text/html", body="<h1>Hallo</h1>")

        client_socket.send(http_response.getHttpRespone().encode())
        client_socket.close()

