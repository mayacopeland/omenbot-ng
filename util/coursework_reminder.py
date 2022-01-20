import asyncio 


async def reminder_loop():
    while True:
        x = 'remind'
        await asyncio.sleep(10)