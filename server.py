import socket

server_ip = "127.0.0.1" 
port = 8000

def run_server():
    server = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

    # bind hte socket to a speciic address and port
    server.bind((server_ip, port))

    # listen for incoming connections
    server.listen(0)
    print(f"Listening on {server_ip}:{port}")

    # accept imcoming connections
    client_socket, client_address = server.accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")


    while True:
        request = client_socket.recv(1024)
        request = request.decode("utf-8") # convert bytes to string
    
        # if we receive "close" rom the client, then we break
        # out o the loop and close the connection
        if request.lower().strip() == "close":
            client_socket.send("closed".encode("utf-8"))
            break
        
        print(f"Received: {request}")
        response = "HTTP/1.0 200 OK\r\n\r\nHallo world2".encode("utf-8")
        # response = "accepted".encode("utf-8") # convert string to bytes
        # convert and send accept response to the client
        # client_socket.send(response)
        client_socket.send(b"HTTP/1.0 200 OK\n")
        client_socket.send(b"Content-Type: text/html\r\n\r\n")
        client_socket.send(b"<html><body><h1>hallo world?</h1></body></html>")



    client_socket.close()
    print("Connection to client closed")
    # close server socket
    server.close()

run_server()