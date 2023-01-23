# Import the python socket module
import socket

SERVER_IP = "127.0.0.1"
PORT = 8080

# Making a socket instance
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecting to the server
client.connect((SERVER_IP, PORT))
aux = ""

while True:
    print("This is a simple calculator that is able to perform addition, subtraction, multiplication and division")

    if aux == "y":
        client.send(aux.encode())
        break

    # Get the input from the user
    first_value = str(input("\nEnter the first value of the operation: "))
    operation = str(input("\nEnter the operation you want to perform (+, -, *, /): "))
    second_value = str(input("\nEnter the second value: "))

    # Group the inputs and send them to the server
    msg = first_value + " " + operation + " " + second_value

    # Here we send the user input to the server socket
    client.send(msg.encode())

    # Here we receive the output from the server socket
    answer =  client.recv(1024)
    print("\nThe answer is ", answer.decode())
    print("\n(Note that if the answer is 0, something might have gone wrong! Check that the input was correct)")

    # If user wants to terminate the connection with the server socket they can type 'y'
    aux = input("\nDo you want to terminate? [y/n]")

client.close()

    
