# Import the python socket module
import socket

LOCAL_HOST = "127.0.0.1"
PORT = 8080

# Making a socket instance
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecting to the server
client.connect((LOCAL_HOST, PORT))

while True:
    print("This is a calculator that is able to perform addition, subtraction, multiplication and division")

    # Get the input from the user
    first_value = input("\nEnter the first value of the operation: ")
    operation = input("\nEnter the operation you want to perform: ")
    second_value = input("\nEnter the second value: ")
    
