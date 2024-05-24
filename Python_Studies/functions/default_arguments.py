import time


def count(end, start=0):  # write default value after any positional argument
    for x in range(start, end + 1):
        print(x)
        time.sleep(1)
    print("DONE")


count(10)
