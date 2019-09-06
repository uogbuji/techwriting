async def connect_get_read(session, url):
    async with session.get(url) as response:
        return await response.text()

async def fetch_pages(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [ connect_get_read(session, url) for url in urls ]
        gathered = asyncio.gather(*tasks)
        return await gathered
        # Same result as last time, but more efficient
