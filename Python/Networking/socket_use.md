#### Creating Server
- A Server follows the sequence
    - create a socket  `socket()`
    - bind to an address `bind()`
    - start listening on the socket `listen()`
    - accept a new session `accept()`
        - multiple times for each new client
- Server does not sendall()/recv() on the listening socket, but on socket returned by accept()
- Ways to make server accept multiple session
    - Use `threading`
    - Use in-built async support
        - asyncio.streams
        - asyncio.transport
        - asyncio.protocols
    - Use other Async libraries



#### Creating a Client
- A client follows the sequence
    - socket() 
    - connect()



#### Asynchronous Socket  Programming
- Modules:
    - asyncio.streams: High level async/await  primitive to work with network.
    - asyncio.transport &
    - asyncio.protocols: 
        - Both are low level primitive to work with network.
        - These are the APIs  used by loop.create_connection()
        - Generally used by libraries and framework.




#### Example Socket:
```python
    
    # Server


```
