import time

def getpercentage(used: int, all1: int):
    return used / all1 * 100

def getping():
    before = time.monotonic_ns()
    count = 1
    for i in range(5000):
        print(i)
        print(count)
        count = count + 1
    time1 = time.monotonic_ns() - before
    return time1 / 1000000
