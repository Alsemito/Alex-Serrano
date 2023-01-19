# Import the python socket module
import socket

SERVER_IP = "127.0.0.1"
PORT = 8080

# Making a socket instance
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecting to the server
client.connect((SERVER_IP, PORT))

while True:
    print("This is a calculator that is able to perform addition, subtraction, multiplication and division")

    # Get the input from the user
    first_value = input("\nEnter the first value of the operation: ")
    operation = input("\nEnter the operation you want to perform: ")
    second_value = input("\nEnter the second value: ")

    # If user wants to terminate the connection with the server socket they can type y
    aux = input("\nDo you want to terminate? [y/n]")
    if aux == "y":
        break

    # Group the inputs in a list to send to the server
    sentence = [first_value, operation, second_value]

    # Here we send the user input to the server socket
    client.send(sentence.encode())

    # Here we receive the output from the server socket
    answer =  client.recv(1024)
    print("\nThe answer is ", answer.decode())

    # If user wants to terminate the connection with the server socket they can type y
    aux = input("\nDo you want to terminate? [y/n]")


client.close()

    
