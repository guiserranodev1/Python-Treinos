import asyncio

async def corrotina(numero):
    print(f'Inicio {numero}.')
    await asyncio.sleep(2)
    print(f'Fim {numero}.')

async def main():

    print('Olá amigo!')

    tarefa1 = asyncio.create_task(corrotina(1))
    tarefa2 = asyncio.create_task(corrotina(2))

    await tarefa1
    await tarefa2

    print('Tchau amigo!')

asyncio.run(main())