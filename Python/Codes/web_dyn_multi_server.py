import socket
import threading

# Dictionary to keep track of dynamically created servers
servers = {}

def start_new_server(port):
    if port not in servers:
        def run_server():
            # Your server logic for the new server on the specified port goes here
            print(f"Started server on port {port}")

        servers[port] = threading.Thread(target=run_server)
        servers[port].start()

def main():
    # Start the main server
    main_port = 8080
    main_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    main_server.bind(('localhost', main_port))
    main_server.listen(5)  # Listen for incoming connections
    print(f"Main server started on port {main_port}")

    while True:
        # Accept incoming Telnet connections
        client_socket, client_address = main_server.accept()
        print(f"Accepted connection from {client_address}")
        data = client_socket.recv(1024).decode()

        if data.startswith("start_server "):
            _, port = data.split()
            try:
                port = int(port)
                start_new_server(port)
                client_socket.send(f"Started server on port {port}".encode())
            except ValueError:
                client_socket.send("Invalid port number".encode())

        client_socket.close()

if __name__ == "__main__":
    # Run the main server in the main thread
    main()

    # The main thread is free to do other tasks, and the main server
    # handles dynamic server creation based on incoming Telnet connections.
    print("Main thread continues...")

    # Optionally, you can join the server threads if you want to wait for them to finish
    # This allows you to dynamically create additional servers when needed.
    for port, thread in servers.items():
        thread.join()
