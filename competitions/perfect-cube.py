import itertools
import operator
import functools


def is_cube(n):
    cube_root = n**(1./3.)
    if round(cube_root) ** 3 == n:
        return True
    else:
        return False


if __name__ == "__main__":
    x = [2, 3, 3, 6, 3, 12]
    comb = list(itertools.combinations(x, 4))
    count = 0
    for i in comb:
        num = functools.reduce(operator.mul, i, 1)
        if (is_cube(num)):
            count += 1
    print(count)
