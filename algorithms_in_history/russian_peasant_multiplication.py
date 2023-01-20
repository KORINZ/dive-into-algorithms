import pandas as pd


def RPM(n1: int, n2: int) -> int:
    halving = [n1]
    doubling = [n2]

    while min(halving) > 1:
        halving.append(min(halving) // 2)

    while len(doubling) < len(halving):
        doubling.append(max(doubling) * 2)

    half_double = pd.DataFrame(zip(halving, doubling), columns=['half', 'double'])
    print(half_double)

    # the product of n1 and n2 is the sum of the 'double' excluding the rows where the 'half' is an even number
    return sum(half_double.loc[half_double['half'] % 2 == 1]['double'])


if __name__ == '__main__':
    print(RPM(17, 374))  # the product of 17 and 374 is 6358
