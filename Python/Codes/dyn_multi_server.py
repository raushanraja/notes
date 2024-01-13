import asyncio
import threading
from asyncio import StreamWriter, StreamReader
import queue

# Queue to coordinate server creation
new_server_queue = queue.Queue()

async def onConnect(reader: StreamReader, writer: StreamWriter):
    print('Client onConnected')
    data = await reader.read(100)
    message = data.decode().strip()
    print(f'Received message: {message}')
    
    if message.startswith("start_server "):
        _, port = message.split()
        try:
            port = int(port)
            new_server_queue.put(port)
        except ValueError:
            print("Invalid port number")

    writer.write("hello world".encode())
    writer.close()

async def serve_on_port(port):
    server = await asyncio.start_server(onConnect, 'localhost', port)
    await server.serve_forever()

def run_server(port):
    asyncio.run(serve_on_port(port))

def start_new_server(port):
    server_thread = threading.Thread(target=run_server, args=(port,))
    server_thread.start()

if __name__ == "__main__":
    initial_ports = [5678, 5679]  # Initial list of ports for your servers

    # Create separate threads for the initial servers
    initial_server_threads = [threading.Thread(target=run_server, args=(port,)) for port in initial_ports]

    # Start all initial server threads
    for server_thread in initial_server_threads:
        server_thread.start()

    # Your main thread can continue with other tasks here
    print("Main thread continues...")

    # Check for messages and start new servers dynamically
    while True:
        try:
            port = new_server_queue.get(timeout=1)  # Wait for a message for 1 second
            start_new_server(port)
        except queue.Empty:
            pass  # No new messages, continue with other tasks

    # Optionally, you can join the initial server threads if you want to wait for them to finish
    for server_thread in initial_server_threads:
        server_thread.join()
