import aiohttp

async def access_site():
    url = 'http://artscene.textfiles.com/information/ascii-newmedia.txt'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return response

