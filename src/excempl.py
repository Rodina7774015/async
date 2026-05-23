import asyncio
from time import time

from loguru import logger


async def f(time_sl: int) -> None:
    """Пробная корутина"""
    time_sleep = time()
    await asyncio.sleep(time_sl)
    print("В задаче ")
    print(f"Время выполенния : {time() - time_sleep:.10f}")


async def main() -> None:
    """Точка входа асинх.приложения"""
    time_sleep = time()
    tasks = []
    for _ in range(10):
        task = asyncio.create_task(f(1))
        tasks.append(task)

    await asyncio.gather(*tasks)
    print(f"\nВремя выполенния : {time() - time_sleep:.10f}")


###################################################################################
##Счётчики
max_counts = {"Counter 1": 10, "Counter 2": 5, "Counter 3": 15}
delays = {"Counter 1": 1, "Counter 2": 2, "Counter 3": 0.5}
counts = {"Counter 1": 0, "Counter 2": 0, "Counter 3": 0}


async def counter(name_counter: str, delays: int):
    for _ in range(max_counts[name_counter]):
        counts[name_counter] += 1
        print(f"{name_counter}: {counts[name_counter]}")
        await asyncio.sleep(delays)


async def main():
    tasks = []
    for i in range(1, len(counts) + 1):
        name = f"Counter {i}"
        task = asyncio.create_task(counter(name, delays[name]))
        tasks.append(task)

    await asyncio.gather(*tasks)


######################################################################################
##Секундный интервал''


async def print_with_delay(number_coro: int):
    await asyncio.sleep(2)
    if number_coro == 5:
        raise ValueError("Не корректное значение ")
    return f"Coroutine {number_coro} is done"


async def main():
    list_task = []
    for i in range(10):
        task = asyncio.create_task(print_with_delay(i), name=f"Задача {i}")
        list_task.append(task)
    try:
        await asyncio.gather(*list_task)
    # ------------------------Этот блок используеться вместо return_excrpt в gather()---------#
    except Exception:
        await asyncio.sleep(2)
        for i in list_task:
            try:
                logger.success(f"{i.result()}")
            except Exception as a:
                logger.warning(f"{i.get_name()}-{a}")
    else:
        for i in list_task:
            logger.success(f"{i.result()}")


asyncio.run(main())


########################################################################################
