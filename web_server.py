import socket
from http import parseRequest
from HttpHeader import HttpHeader



PORT = 8000

addr = ("", PORT)  # all interfaces, port 8080

def init_server():
    server = socket.create_server(addr, family = socket.AF_INET6)
    server.listen(0)

    print("Server starts to accept connections from clients...")
    while(True):
        client_socket, client_address = server.accept()
        header = HttpHeader("1.0", 200, "OK", "text/html", body="<h1>Hallo</h1>")
        client_request = client_socket.recv(1024).decode("utf-8")
        parseRequest(client_request)

        client_socket.send(header.getHeader().encode())
        client_socket.close()

init_server()