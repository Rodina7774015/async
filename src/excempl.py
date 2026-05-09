import asyncio


async def f():
    await asyncio.sleep(1)
    print("end")


def main():
    asyncio.run(f())
