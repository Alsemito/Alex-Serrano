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
print("Connected client: ", clientAddress)
msg = ""

# Run infinite loop
while True:
    data = clientConnection.recv(1024)
    msg = data.decode()
    if msg == "y":
        print("Connection is over")
        break

    print("Equation received")
    result = 0
    str_list = msg.split()
    first = str_list[0]
    operation = str_list[1]
    second = str_list[2]

    # Turn the number to integers
    num1 = int(first)
    num2 = int(second)

    # We can now perform the operations for the calculator
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2

    print("Sending result to client...")
    output = str(result)
    clientConnection.send(output.encode())
clientConnection.close()


