import asyncio
import aiohttp
from urllib.parse import urlparse

#List of URLs to process
URLS = [
    'http://web.textfiles.com/computers/macbeth95',
    'https://www.gutenberg.org/files/1342/1342-0.txt', #Pride and Prejudice
    'http://web.textfiles.com/humor/zenerror.txt',
    'http://artscene.textfiles.com/history/essays/pcascii.txt',
    'http://web.textfiles.com/games/boredoftherings.txt',
    'https://www.gutenberg.org/files/36/36-0.txt', #The War of the Worlds
    'http://artscene.textfiles.com/information/ascii-newmedia.txt',
    'https://www.gutenberg.org/files/244/244-0.txt', #A Study In Scarlet
    'http://web.textfiles.com/computers/dn3d_2.txt',
    'http://web.textfiles.com/computers/linux.txt',
    'http://artscene.textfiles.com/ansimusic/information/ansimtech.txt',
    'https://www.gutenberg.org/files/74/74-0.txt', #Tom Sawyer
]

#3 seconds between requests
BREATHER = 3


class worker:
    '''
    Encapsulates state for the workers that handle URLs from each domain
    '''

    def __init__(self, domain, job_q):
        self.domain = domain
        self.job_q = job_q
        return

    async def run(self):
        '''
        Keep checking the queue for for URLs to process until empty
        Enforce a breather between requests
        '''
        counts = []
        #Use one session for all the connection to this domain
        #Ignore SSL, for simplification, but be careful if you do this for real
        connector = aiohttp.TCPConnector(verify_ssl=False)
        async with aiohttp.ClientSession(connector=connector) as session:
            #Get items from queue until empty
            while not self.job_q.empty():
                url = await self.job_q.get()

                #Delegate the actual web query to another coroutine
                word_count = await self.count_words(session, url)
                counts.append(word_count)

                #Polite pause between requests to the server
                await asyncio.sleep(BREATHER)

        #Tot up the counts processed
        total = sum(counts)
        print(total, 'words counted from', self.domain)
        return total


    async def count_words(self, session, url):
        '''
        Make the network requests for a URL. Return the word count from content
        '''
        print('Processing', url)
        async with session.get(url) as response:
            content = await response.text()
            #Approximate word count by splitting on whitespace and counting 
            return len(content.split())


async def coordinator(loop):
    '''
    Main coroutine. Sets up workers and queues up URLs
    '''
    workers = []

    for url in URLS:
        #Extract the domain from the URL
        urlparts = urlparse(url)
        domain = urlparts.netloc
        #Find the worker designated for this domain. If not found, create a new worker.
        for worker_obj in workers:
            if domain == worker_obj.domain:
                worker_obj.job_q.put_nowait(url)
                break
        else:
            #Reaches here if there is no break, i.e. no worker matched
            #Create a queue for the worker, then its object
            job_q = asyncio.Queue(loop=loop)
            worker_obj = worker(domain, job_q)
            worker_obj.job_q.put_nowait(url)
            workers.append(worker_obj)

    #Gather up from the worker coroutines to get the overall total
    counts = await asyncio.gather(*[ w.run() for w in workers ])
    total = sum(counts)
    return total


if __name__ == '__main__':
    # Can also use go_async()
    loop = asyncio.get_event_loop()
    total = loop.run_until_complete(coordinator(loop))
    print(total, 'total words counted')
    loop.close()
