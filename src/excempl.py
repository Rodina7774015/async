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


########################################################################################
# Пример с импользолванием wait_for(awaitable, timeout)
async def fun():
    await asyncio.sleep(3)
    return "Hello word"


async def main():
    try:
        wait_task = await asyncio.wait_for(fun(), timeout=1)
    except TimeoutError:
        print("Не успел закончится")
    else:
        print(wait_task)


##########################################################################################


async def long_run_task(name: str, delay: int, future: asyncio.Future):
    print(f"work {name} working {delay}")
    await asyncio.sleep(delay)
    res = "data_res"
    print(f"end work {name}")
    future.set_result(res)


async def get_res(res):

    if res == "data_res":
        print("Начали работу счетчика")
        for i in range(10):
            await asyncio.sleep(1)
            print(i)
    else:
        print("преключения")
        await asyncio.sleep(0)


async def run_task():
    future = asyncio.Future()  # создали пустой обект
    await long_run_task("Work_1", 3, future)
    re = future.result()
    await get_res(re)


########################################################################################333


async def read_book(student, time):
    print(f"{student} начал читать книгу.")
    await asyncio.sleep(time)
    print(f"{student} закончил читать книгу за {time} секунд.")


async def main():
    task = asyncio.create_task(read_book("Алекс", 5))
    asyncio.create_task(read_book("Мария", 3))
    asyncio.create_task(read_book("Иван", 4))


##########################################################################################
####Марафон знаний
students = {
    "Алекс": {"course": "Асинхронный Python", "steps": 515, "speed": 78},
    "Мария": {"course": "Многопоточный Python", "steps": 431, "speed": 62},
    "Иван": {"course": "WEB Парсинг на Python", "steps": 491, "speed": 57},
}


async def study_course(student, course, steps, speed):
    print(f"{student} начал проходить курс {course}.")
    res = steps / speed
    await asyncio.sleep(res)
    print(f"{student} прошел курс {course} за {round(res, 2)} ч.")


async def main():
    tasks = []
    for name, par in students.items():
        task = asyncio.create_task(
            study_course(name, par["course"], par["steps"], par["speed"])
        )
        tasks.append(task)
    await asyncio.gather(*tasks)


#########################################################################3


async def compute_square(x):
    print(f"Вычисляем квадрат числа: {x}")
    await asyncio.sleep(1)  # Имитация длительной операции
    return x * x


async def m():

    task = [asyncio.create_task(compute_square(i), name="my_task") for i in range(10)]
    for i in task:
        print(f"{i.get_name()}")
    tasks = await asyncio.gather(*task)
    print(tasks)
    for result in tasks:
        print(f"Результат: {result}")


asyncio.run(m())
