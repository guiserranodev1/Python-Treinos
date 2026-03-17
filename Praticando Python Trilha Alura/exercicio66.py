import asyncio

async def corrotina(futuro):
    print("Inicio")
    await asyncio.sleep(2)
    futuro.set_result('Fim')

async def main():
    futuro = asyncio.Future()
    asyncio.create_task(corrotina(futuro))
    resultado = await futuro
    print(resultado)

asyncio.run(main())