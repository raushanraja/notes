### Client Session
- it is suggested you use a single session for the lifetime of your application to benefit from connection pooling.
- From Twillio link:
    - A single session object that can be used for quite a number of individual requests and by default can make connections with up to 100 different servers at a time. 




#### Examples
- Client Sesison
```python
    import aiohttp
    import asyncio

    async def fetch(client):
        async with client.get('http://python.org') as resp:
            assert resp.status == 200
            return await resp.text()

    async def main():
        async with aiohttp.ClientSession() as client:
            html = await fetch(client)
            print(html)

    asyncio.run(main())
```






##### References
- https://docs.aiohttp.org/en/stable/client_reference.html#client-session
- https://www.twilio.com/blog/asynchronous-http-requests-in-python-with-aiohttp

