import socket  # Import the python socket module
import csv     # Import the python csv module

SERVER_IP = "127.0.0.1"
PORT = 8080

# Making a socket instance
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecting to the server
client.connect((SERVER_IP, PORT))
aux = ""

while True:
    # Termination available after at least one iteration
    if aux == "y":
        client.send(aux.encode())
        break

    print("This is a simple calculator that is able to perform addition, subtraction, multiplication and division")

    # With this, one is able to toggle between parts of the assignment
    choice = input("Do you want to input the operation yourself or read it from the sample file?\n"
                   "[1] Manual input\n"
                   "[2] Input from file\n")

    first_value = ""
    operation = ""
    second_value = ""

    match choice:
        case "1":
            # Get the input from the user
            first_value = str(input("\nEnter the first value of the operation: "))
            operation = str(input("\nEnter the operation you want to perform (+, -, *, /): "))
            second_value = str(input("\nEnter the second value: "))

            # Group the inputs and send them to the server
            msg = first_value + " " + operation + " " + second_value

            # Here we send the user input to the server socket
            client.send(msg.encode())

            # Here we receive the output from the server socket
            answer = client.recv(1024)
            print("\nThe answer is ", answer.decode())

        case "2":
            log = input("Do you want a log of all the operations and results? [y][n]")
            # Open the sample file
            with open("sample.csv", "r") as f:
                reader = csv.reader(f)
                # Iterate the entire file and print every operation
                for line in reader:
                    first_value = str(line[0])
                    operation = str(line[1])
                    second_value = str(line[2])
                    msg = first_value + " " + operation + " " + second_value
                    client.send(msg.encode())
                    answer = client.recv(1024)
                    print("The operation performed is ", first_value, operation, second_value, " = ", answer.decode())

                    # If the user wants, it can generate a log file as a .txt
                    if log == "y":
                        with open('results_log.txt', 'a') as log_file:
                            log_file.write(first_value + operation + second_value + " = " + answer.decode() + "\n")

    # If user wants to terminate the connection with the server socket they can type 'y'
    aux = input("\nDo you want to terminate? [y/n]\n")

client.close()

    
