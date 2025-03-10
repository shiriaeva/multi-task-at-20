from hashlib import md5
from random import choice
import concurrent.futures
from datetime import datetime


def generate_hash(n):
    while True:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("00000"):
            return s + ',' + h


def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=100) as executor:
        for s in executor.map(generate_hash, range(10)):
            print(s)


if __name__ == '__main__':
    start = datetime.now()
    main()
    end = datetime.now()
    print(end - start)