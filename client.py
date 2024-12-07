import socket

def run_client():
    # Connect to the server on localhost at port 9999
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("localhost", 9999))

        # Receive and print the instructions from the server
        instructions = s.recv(1024).decode('utf-8')
        print(instructions)

        # Get the user input (path) from the client
        user_input = input("Enter a path to send to the server: ")

        # Send the user input to the server
        s.sendall(user_input.encode())

        # Receive and print the server's response
        response = s.recv(4096).decode('utf-8')
        print("Response from server:")
        print(response)

if __name__ == "__main__":
    run_client()
