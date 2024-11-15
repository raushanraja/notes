import socket


def connect_to_server(server_address, server_port, local_port):
    client_socket = None
    try:
        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the client socket to a specific local port
        client_socket.bind(('127.0.0.1', local_port))

        # Connect to the server
        client_socket.connect((server_address, server_port))

        print(f"Connected to {server_address} on port {
              server_port} from local port {local_port}")

        # Example: send data to the server
        client_socket.sendall(b"Hello, server!")

        # Example: receive data from the server
        data = client_socket.recv(1024)
        print(f"Received from server: {data.decode()}")

    except ConnectionRefusedError:
        print(f"Connection to {server_address} on port {server_port} refused.")
    finally:
        # Always close the socket after use
        if client_socket:
            client_socket.close()


# Example usage: connect to localhost on port 8080 from local port 8081
connect_to_server('127.0.0.1', 8080, 8081)
