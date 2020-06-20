from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:

    import math

    if x == 0:
        return '0'

    res = ''
    if x < 0:
        res = '-'
        xa = abs(x)
    else:
        xa = x

    base = 1
    while base <= xa:
        base = base * 10

    while base > 1:
        base = base/10
        ds = '%d' % (math.floor(xa/base))
        res = ''.join([res,ds])
        xa = xa - math.floor(xa/base)*base

    return res


def string_to_int(s: str) -> int:

    dicdig = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    l = len(s)
    neg = False
    ini = 0
    if s[0] == '+':
        ini = 1
    elif s[0] == '-':
        ini = 1
        neg = True
    else:
        pass

    res = 0
    for i in range(ini,l):
        res = 10*res+dicdig[s[i]]

    if neg:
        return -1*res
    else:
        return res



def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
