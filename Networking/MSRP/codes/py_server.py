import socket


def start_server(server_port):
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address ('', server_port) which means any available network interface
    server_socket.bind(('', server_port))

    # Listen for incoming connections (max backlog of connections set to 5)
    server_socket.listen(5)

    print(f"Server listening on port {server_port}...")

    while True:
        # Wait for a connection
        client_socket, client_address = server_socket.accept()

        try:
            print(f"Connection from {client_address}")

            # Receive data from the client
            data = client_socket.recv(1024)
            if data:
                print(f"Received from client: {data.decode()}")

                # Echo back the received data
                client_socket.sendall(data)
            else:
                print(f"No data received from {client_address}")

        except Exception as e:
            print(f"Exception handling client {client_address}: {e}")

        finally:
            # Close the client connection
            client_socket.close()


# Example usage: start the server listening on port 8080
start_server(8080)
