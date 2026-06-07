import asyncio
import random
from time import time


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


async def long_run_task(name: str, delay: int, future: asyncio.Future) -> None:
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


#############################################################################################
async def ex(n):
    await asyncio.sleep(n)
    raise Exception("Ошибка")


async def ma() -> None:
    list_task = []

    for i in range(5):
        list_task.append(asyncio.create_task(ex(i), name=f"task{i}"))

    done, pending = await asyncio.wait(list_task, timeout=3)

    for i in done:
        print(i.get_name())
        if i.exception() is not None:
            print(i.exception())
    for i in pending:
        print(f"wait - {i.get_name()}")


###############################################################################################
processor_delays = {
    "Intel Core i9-11900K": 7.01,
    "Intel Core i7-11700K": 4.32,
    "Intel Core i5-11600K": 8.59,
    "AMD Ryzen 9 5950X": 2.53,
    "AMD Ryzen 9 5900X": 8.4,
    "AMD Ryzen 7 5800X": 3.55,
    "AMD Ryzen 5 5600X": 1.15,
    "Intel Core i9-10900K": 1.8,
    "Intel Core i7-10700K": 5.58,
    "Intel Core i5-10600K": 2.01,
    "AMD Ryzen 9 3950X": 6.19,
    "AMD Ryzen 9 3900X": 3.08,
    "AMD Ryzen 7 3800X": 4.1,
    "AMD Ryzen 5 3600X": 6.13,
    "Intel Core i9-9900K": 1.26,
    "Intel Core i7-9700K": 2.46,
    "Intel Core i5-9600K": 4.91,
    "AMD Ryzen 9 3850X": 1.33,
    "AMD Ryzen 9 3750X": 7.62,
    "AMD Ryzen 7 3700X": 6.67,
    "AMD Ryzen 5 3500X": 5.65,
    "Intel Core i9-10850K": 8.89,
    "Intel Core i7-10600K": 8.37,
    "Intel Core i5-10400F": 3.07,
    "AMD Ryzen 9 3950XT": 4.37,
    "AMD Ryzen 9 3900XT": 3.92,
    "AMD Ryzen 7 3800XT": 1.93,
    "AMD Ryzen 5 3600XT": 3.55,
    "Intel Core i9-10980XE": 1.67,
    "Intel Core i7-10700F": 6.79,
}


async def speed_pro(speed):
    await asyncio.sleep(speed)


async def m():
    tasks = [
        asyncio.create_task(speed_pro(speed), name=name)
        for name, speed in processor_delays.items()
    ]
    finished, _ = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    for i in finished:
        print(f"Первый завершенный процесс: {i.get_name()}")


##############################################################################################################

dishes = {
    "Куриный суп": 118,
    "Бефстроганов": 13,
    "Рататуй": 49,
    "Лазанья": 108,
    "Паэлья": 51,
    "Утка по-пекински": 41,
    "Суши": 116,
    "Цезарь с курицей": 106,
    "Маргарита пицца": 23,
    "Шпинатный пирог": 29,
    "Карри с курицей": 88,
    "Тирамису": 10,
    "Греческий салат": 18,
    "Фалафель": 102,
    "Буррито": 90,
    "Карбонара": 111,
    "Ризотто с грибами": 79,
    "Фокачча": 38,
    "Шашлык": 121,
    "Газпачо": 95,
    "Блинчики": 118,
    "Сэндвич с авокадо": 67,
    "Кимчи": 80,
    "Табуле": 68,
    "Паста алла норма": 32,
    "Жареный рис": 47,
    "Том Ям": 19,
    "Веганский бургер": 43,
    "Киш с луком": 61,
    "Салат Нисуаз": 97,
}


async def cooking_timer(name, time) -> None:
    print(f"Приготовление {name} начато.")
    await asyncio.sleep(time / 10)
    print(f"Приготовление {name} завершено за {time / 10} секунды.")


async def main():

    tasks: list[asyncio.Task] = [
        asyncio.create_task(cooking_timer(name, time), name=name)
        for name, time in dishes.items()
    ]

    done, pending = await asyncio.wait(tasks, timeout=10)

    if pending:
        for task in pending:
            try:
                task.cancel()
                await task
            except asyncio.CancelledError:
                print(
                    f"{task.get_name()} не успел(а,о) приготовиться и будет отменено."
                )
    print(f"Приготовлено блюд: {len(done)}. Не успели приготовиться: {len(pending)}.")


#############################################################################################
# Когда не нужно дожидаться получения результатов всех задач, а важно реагировать на завершение каждой задачи.
# В ситуациях, когда необходимо выполнять множество независимых задач параллельно и обрабатывать результаты по мере их завершения.
async def task(num):
    await asyncio.sleep(delay := random.random())
    return f"Task {num} completed, {delay=:.3f}"


async def main():
    tasks = [asyncio.create_task(task(i)) for i in range(5)]

    for completed_task in asyncio.as_completed(tasks):
        # completed_task - объект корутины, создаваемый функцией as_completed(), возвращающий результат завершенной задачи.
        result = await completed_task
        print(result)


####################################################################################################
# Ручное управление


async def main():
    print("Корутина завершена")


def event_loop(coro):
    loop = asyncio.new_event_loop()
    try:
        loop.run_until_complete(coro)
        for i in loop.__class__.__dict__:
            if i.startswith("_"):
                pass
            else:
                print(i)
    except Exception:
        pass
    finally:
        loop.close()


event_loop(main())
