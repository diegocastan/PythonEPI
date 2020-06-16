from test_framework import generic_test


def parity(x: int) -> int:
    # PROBLEM 4.1

    result = 0
    # We are in the loop while there is a 1 in x. With XOR we set the parity and then we erase the lowest set bit
    while x:
        result ^= 1
        x = x & (x-1)
        # NOTE: With x&(x-1) the lowest set bit is erased
        # NOTE 2: With x&~(x-1) the lowest set bit is isolated
    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
