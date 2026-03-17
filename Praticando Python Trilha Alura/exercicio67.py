import asyncio

async def timer():
    print('Inicio do tempo')
    await asyncio.sleep(3)
    print('Tempo finalizado.')

asyncio.run(timer())
    