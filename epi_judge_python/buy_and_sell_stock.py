from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    maxprof = 0.0

    # BRUTE FORCE
    # for i in range(len(prices)):
    #     for j in range(i+1,len(prices)):
    #         prof =  prices[j] - prices[i]
    #         if prof > maxprof:
    #             maxprof = prof
    # return maxprof

    # MIN TRACK
    minele = prices[0]
    for i in range(1,len(prices)):
        minele = min(minele,prices[i-1])
        prof = prices[i]-minele
        if prof > maxprof:
            maxprof = prof
    return maxprof



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
