from test_framework import generic_test


def convert_base(num_as_string: str, b1: int, b2: int) -> str:

    if num_as_string[0] == '-':
        neg = True
        numstr = num_as_string[1:]
    else:
        neg = False
        numstr = num_as_string

    # convert to decimal
    numint = 0
    for e,i in enumerate(reversed(range(len(numstr)))):
        numint += int(numstr[i])*(b1**e)

    # convert to new base
    res = []
    while numint > 0:
        res.append(hex(numint % b2)[2:])
        numint = numint // b2

    if neg:
        res.insert(0,'-')
    return ''.join(res)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
