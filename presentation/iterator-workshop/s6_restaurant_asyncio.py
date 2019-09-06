import asyncio

async def get_menus():
    delay_minutes = random.randrange(3) #0 to 3 mins
    await asyncio.sleep(delay_minutes) #Sim sec==min

async def get_order():
    delay_minutes = random.randrange(10)
    await asyncio.sleep(delay_minutes)
    order = random.choice(['Special of the day', 'Fish & Chips', 'Pasta'])
    return order

async def prepare_order(order):
    delay_minutes = random.randrange(10, 20)
    await asyncio.sleep(delay_minutes)
    print(f'[Order ready from kitchen: {order}]')

async def eat():
    delay_minutes = random.randrange(20, 40)
    await asyncio.sleep(delay_minutes)

async def get_payment():
    delay_minutes = random.randrange(10)
    await asyncio.sleep(delay_minutes)

async def serve_table(tabnum):
    await get_menus()
    print(f'Welcome. Please sit at table {tabnum}. Here are your menus')
    order = await get_order()
    print('Table {tabnum} what will you be having today?')
    await prepare_order(order)
    print('Table {tabnum} here is your meal:', order)
    await eat()
    print('Table {tabnum} here is your check')
    await get_payment()
    print('Thanks for visiting us! (table {tabnum} )')

# Create tasks/coroutines for three tables
gathered_coroutines = asyncio.gather(
    serve_table(1), serve_table(2), serve_table(3)
)
loop = asyncio.get_event_loop()
# Entry from synchronous to asynchronous code.
# Will block until given coroutine has completed
loop.run_until_complete(gathered_coroutines)
# Gathered tasks complete. Done with event loop
loop.close()
