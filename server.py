import socket

LOCALHOST = "127.0.0.1"
PORT = 8080

# Call the server socket method
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((LOCALHOST, PORT))
server.listen(1)
print("Server started")
print("\nWaiting for request...")

# Now everything is ready for a user input
clientConnection, clientAddress = server.accept()

