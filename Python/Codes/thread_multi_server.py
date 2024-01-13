import asyncio
import threading
from asyncio import StreamWriter, StreamReader

async def onConnect(reader: StreamReader, writer: StreamWriter):
    print('Client onConnected')
    writer.write("hello world".encode())
    writer.close()

async def serve_on_port(port):
    server = await asyncio.start_server(onConnect, 'localhost', port)
    await server.serve_forever()

def run_server(port):
    asyncio.run(serve_on_port(port))

if __name__ == "__main__":
    ports = [5678, 5679]  # List of ports for your servers

    # Create a separate thread for each server
    server_threads = [threading.Thread(target=run_server, args=(port,)) for port in ports]

    # Start all server threads
    for server_thread in server_threads:
        server_thread.start()

    # Your main thread can continue with other tasks here
    print("Main thread continues...")

    # Optionally, you can join the server threads if you want to wait for them to finish
    for server_thread in server_threads:
        server_thread.join()
