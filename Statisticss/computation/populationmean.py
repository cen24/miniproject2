from Calculator.computation.addition import add
from Calculator.computation.division import div


def mean(list):
    n = len(list)
    total = 0
    for var in range(0, n, 1):
        total = float(add(total, list[var]))
    z = float(div(n, total))
    return z