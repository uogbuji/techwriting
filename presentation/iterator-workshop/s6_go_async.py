import asyncio

def go_async(launch_task, close_loop=False):
    loop = asyncio.get_event_loop()
    resp = loop.run_until_complete(launch_task)
    if close_loop: loop.close()
    return resp

