# Parallelisierung

# Vorsicht: Kann auch zu einem Overhead führen

import multiprocessing as mp
import numpy as np
import time

print(mp.cpu_count())

np.random.RandomState(100)

arr = np.random.randint(0, 10, size=[10000, 5])
data = arr.tolist()

print(data[-5:])


def how_many_within_range(row, min=4, max=8):
    count = 0

    for n in row:
        if min <= n <= max:
            count += 1

    return count


results = []

start = time.time()

for row in data:
    results.append(how_many_within_range(row))

print('Ergebnis unparallelisiert', time.time() - start)
print(results[:10])

# pool = mp.Pool(mp.cpu_count())
# start = time.time()
# # Massiven Overhead
# results = [pool.apply(how_many_within_range, args=(row, 4, 8)) for row in data]
# print('Ergebnis parallelisiert VERSION 1', time.time() - start)
# print(results[:10])

pool = mp.Pool(mp.cpu_count())

start = time.time()
results = pool.map(how_many_within_range, [row for row in data])
print('Ergebnis parallelisiert VERSION 2 - MAP', time.time() - start)
print(results[:10])

pool.close()


# Async
def how_many_within_range2(i, row, min=4, max=8):
    count = 0

    for n in row:
        if min <= n <= max:
            count += 1

    return (i, count)


results = []


def collect(result):
    global results
    results.append(result)


pool = mp.Pool(mp.cpu_count())

start = time.time()

for i, row in enumerate(data):
    pool.apply_async(how_many_within_range2, args=(i, row), callback=collect)

pool.close()
pool.join()

print('Ergebnis parallelisiert VERSION 3 - ASYNC APPLY', time.time() - start)
print(results[:10])

# map_asnyc
results = []


def collectmap(result):
    global results
    results.append(result)


pool = mp.Pool(mp.cpu_count())
start = time.time()
async_start = pool.map_async(how_many_within_range, data)
results = async_start.get()

print('Ergebnis parallelisiert VERSION 4 - ASYNC MAP', time.time() - start)
print(results[:10])
pool.close()
pool.join()

