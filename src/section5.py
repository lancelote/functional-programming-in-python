import time
import os
import multiprocessing as mp
from collections import namedtuple
from pprint import pprint as pp
from typing import TypedDict
from datetime import date

Scientist = namedtuple("Scientist", ["name", "field", "born", "nobel"])

scientists = (
    Scientist(name="Ada Lovelace", field="math", born=1815, nobel=False),
    Scientist(name="Emmy Noether", field="math", born=1882, nobel=False),
    Scientist(name="Marie Curie", field="chemistry", born=1867, nobel=True),
    Scientist(name="Tu Youyou", field="physics", born=1930, nobel=True),
    Scientist(name="Ada Yonath", field="chemistry", born=1939, nobel=True),
    Scientist(name="Vera Rubin", field="astronomy", born=1928, nobel=False),
    Scientist(name="Sally Ride", field="physics", born=1951, nobel=False),
)


class NameAge(TypedDict):
    name: str
    age: int


def transform(scientist: Scientist) -> NameAge:
    print(f"Process {os.getpid()} working on record {scientist.name}")
    time.sleep(1)  # simulating slow computation
    result = {
        "name": scientist.name,
        "age": date.today().year - scientist.born
    }
    print(f"Process {os.getpid()} done with record {scientist.name}")
    return result


def main() -> None:
    pp(scientists)
    print()

    start = time.time()
    pool = mp.Pool(processes=4)
    result = pool.map(transform, scientists)
    end = time.time()

    print()
    print(f"Time to complete: {end - start:.2f}s")
    print()
    pp(result)


if __name__ == '__main__':
    main()
