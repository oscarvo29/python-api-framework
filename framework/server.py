import socket
from .http import Http
from .HttpResponse import HttpResponse
from .RequestLogger import ServerLog


addr = ("", Http.PORT)  # all interfaces, port 8080

def init_server():
    server_log = ServerLog()
    server = socket.create_server(addr, family = socket.AF_INET6)
    server.listen(0)

    print("Server starts to accept connections from clients...")
    while(True):
        client_socket, client_address = server.accept()
        client_request = client_socket.recv(1024).decode("utf-8")
        request_line = Http.parseRequest(client_request)

        
        if request_line == "invalid":
            bad_request = Http.invalid_request()
            http_response = f"HTTP/1.0 {bad_request}"
            # logger.info(f"client address: {client_address}, {bad_request}")


            client_socket.send(http_response.encode())
            client_socket.close()


        http_response = HttpResponse(request_line)
        
        server_log.log(client_address, http_response.getHttpMethod(), http_response.getHttpEndpoint(), 200, len(http_response.getHttpRespone()))
        client_socket.send(http_response.getHttpRespone().encode())
        client_socket.close()

