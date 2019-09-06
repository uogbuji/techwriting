import aiohttp

async def connect_get_read(session, url):
    async with session.get(url) as response:
        return await response.text()

async def fetch_page(url):
    async with aiohttp.ClientSession() as session:
        return await connect_get_read(session, url)
