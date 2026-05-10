import asyncio
from time import time


async def f(time_sl: int) -> None:
    """Пробная корутина"""
    time_sleep = time()
    await asyncio.sleep(time_sl)
    print(f" Время выполенния : {time() - time_sleep:.2f}")


async def main() -> None:
    """Точка входа асинх. приложения"""
    for time_sl in range(1, 10):
        await f(time_sl)


asyncio.run(main())
