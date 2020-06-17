import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index]

    ## SOLUTION WITH ADDITIONAL SPACE O(n) -- not accepted

    # minor = []
    # equal = []
    # greater = []
    # for ele in A:
    #     if ele < pivot:
    #         minor.append(ele)
    #     elif ele > pivot:
    #         greater.append(ele)
    #     else:
    #         equal.append(ele)
    # A = minor + equal + greater

    ## SOLUTION WITH SPACE COMPLEXITY O(1) AND COMPUTATIONAL COMPLEXITY O(2N)
    # smaller elements
    ini = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[ini], A[i] = A[i], A[ini]
            ini += 1
    # greater elements
    end = len(A)-1
    for i in reversed(range(len(A))):
        if A[i] > pivot:
            A[end], A[i] = A[i], A[end]
            end -= 1
    return


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
    # A = [1, 0, 2, 0, 2, 1, 2, 1, 2, 0, 0, 0, 1, 0, 2, 1, 0, 2, 0, 1, 0, 2, 1, 0, 2, 1, 2, 0, 2, 1, 1, 2, 2, 0, 1, 1, 0, 1, 1, 1, 2, 1, 0, 1, 2, 1, 2, 1, 2, 2, 2, 0, 1, 0, 1, 1, 2, 1, 1, 2, 2, 1, 1, 1, 0, 2, 0, 1, 2, 1, 1, 1, 0, 2, 0, 1, 2, 1, 1, 2, 1, 2, 2, 1, 0, 1, 2, 2, 1, 2, 2, 1, 1, 2, 0, 1, 0, 1, 2, 0, 2, 1, 2, 1, 1, 1, 2, 2, 2, 0, 0, 0, 1, 2, 0, 0, 0, 0]
    # pivot_idx = 101
    # A = [1, 1, 0, 2]
    # pivot_idx = 1
    # dutch_flag_partition(pivot_idx,A)