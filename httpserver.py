import socket


def handle_request(request):
    """
    HANDLES HTTP REQUESTS.
    """

    headers = request.split("\n")
    filename = headers[0].split()[1]

    if filename == "/":
        filename = "/index.html"

    try:
        with open(filename[1:]) as f:
            file = f.read()
            content = file

        response = "HTTP/1.0 200 OK\n\n" + content

    except FileNotFoundError:

        response = "HTTP/1.0 404 NOT FOUND\n\nFile Not Found"

    return response


# DEFINE HOST AND PORT
HOST = "0.0.0.0"
PORT = 8000

# CREATE SOCKET
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(1)
print("Listening on port %s ..." % PORT)

while True:
    # wait for client connection
    client_connection, client_address = server.accept()

    # get the request from browser
    request = client_connection.recv(1024).decode()
    print(request)

    # return HTTP response
    response = handle_request(request)
    client_connection.sendall(response.encode())

    # close connection
    client_connection.close()

# close server socket
server.close()


""" 
PLEASE NOTE, THIS WAS NOT ORIGINAL IMPLEMENTED OR BUILT BY ME.
IT WAS WRITEN BY @joaoventura ON GTIHUB. 
LINK: https://gist.github.com/joaoventura/824cbb501b8585f7c61bd54fec42f08f
"""
