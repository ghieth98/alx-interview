#!/usr/bin/python3
""" The challenge involves determining the winner of a game
    based on the strategic removal of prime numbers and their
    multiples from a set of consecutive integers.
"""


def isWinner(x, nums):
    """Determines the winner based on prime numbers in the list."""
    if not nums or x < 1:
        return None

    max_num = max(nums)
    primes_filter = [True for _ in range(max(max_num + 1, 2))]
    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if not primes_filter[i]:
            continue
        for j in range(i * i, max_num + 1, i):
            primes_filter[j] = False
    primes_filter[0] = primes_filter[1] = False

    # Counting prime numbers and marking their positions
    prime_count = 0
    for i in range(len(primes_filter)):
        if primes_filter[i]:
            prime_count += 1
        primes_filter[i] = prime_count

    # Count odd prime numbers in the list
    odd_primes_count = sum(primes_filter[x] % 2 == 1 for x in nums)

    # return the winner
    if odd_primes_count * 2 == len(nums):
        return None
    if odd_primes_count * 2 > len(nums):
        return "Maria"
    return "Ben"


if __name__ == "__main__":
    assert isWinner(5, [2, 5, 1, 4, 3]) == "Ben", "Expected Ben"
    assert isWinner(
        10, [5, 5, 5, 5, 5, 2, 2, 2, 2, 2]) == "Maria", "Expected Maria"
    assert isWinner(4, [11, 30, 1, 7]) == "Ben", "Expected Ben"
    assert isWinner(6, [1, 1, 0, 0, 1, 8]) == "Ben", "Expected Ben"
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
    print("Winner: {}".format(isWinner(3, [4, 5, 1])))
    print("Winner: {}".format(isWinner(3, [4, 5])))
    print("Winner: {}".format(isWinner(3, [4])))
