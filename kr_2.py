import random
import time
from multiprocessing import Pool


def func():
    array = []
    for i in range(10 ** 6):
        array.append(random.randint(-100, 100))
    if sum(array) % 2 == 0:
        print("Четная сумма")
    else:
        print("Нечетная сумма")


def main():
    func()


if __name__ == '__main__':
    print("При последовательном (4 раза) запуске:")
    start = time.time()
    for _ in range(4):
        func()
    ending = time.time() - start
    print(round(ending, 2), 'секунд\n')

    print('При параллельном - по одному разу в 4 процессах:')
    start = time.time()

    with Pool(4) as pool:
        r = []
        for _ in range(4):
            r.append(pool.apply_async(func))
        for a in r:
            a.wait()

    end = time.time() - start
    print(round(end, 2), 'секунд')