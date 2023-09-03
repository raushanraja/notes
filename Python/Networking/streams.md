#### Streams
- Part of asyncio module
- Higher-Level API to create Server and Client
- Use:
    - Import required modules: `streams, StreamWrite, StreamReader`
    - Based on requirement create a Clien using `stream.open_connection` or Server using `stream.start_server`
- Basic Example:
    ```
    # Server

        import asyncio
        from asyncio import streams, StreamWriter, StreamReader


        async def onConnect(reader: StreamReader, writer: StreamWriter):
            print('Client onConnected')
            writer.write("hello world".encode())
            writer.close()


        async def main():
            server = await asyncio.start_server(onConnect, 'localhost', 5678)
            await server.serve_forever()

        asyncio.run(main())


    # Client
        import asyncio
        from asyncio import streams, StreamReader, StreamWriter


        async def main():
            reader, writer = await asyncio.open_connection('localhost', 5678)
            lines = await reader.read()
            print(lines)

        asyncio.run(main())
    ```

#### Stream Function:
- asyncio.open_connection
- asyncio.start_server
- asyncio.open_unix_connection
- asyncio.start_unix_server


#### StreamReader 
- Represents a reader object that provides APIs to read data from the IO stream. 
- Allows reading data as an asynchronous iterable, the object supports the async for statement.
- Methods:
    - read
    - readline
    - readexactly
    - readuntill

#### StreamWrite
- Represents a writer object that provides APIs to write data to the IO stream.
- Methods:
    - write
    - writelines
    - close
    - can_write_eof
    - write_eof
    - transport
    - get_extra_info
    - start_tls
    - is_closing
    - wait_closed
- After `write` and `writelines` `drain` should be used.
- After `close` , `wait_closed` should be used.

##### Remarks:
- Unable to find a way for the server, where we can listen for client disconnect event.
