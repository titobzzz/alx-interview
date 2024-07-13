#!/usr/bin/python3
""" Prime--Game task 0Prime Game
"""


def findPrimesToN(n):
    """
    Returns list of primesup toparameter value n, in ascending-order
    """

    if (type(n) is not int or n < 0):
        return None

    primes = []
    for candidate in range(2, n + 1):
        prime = True
        for divisor in range(2, candidate):
            if (candidate % divisor == 0):
                prime = False
                break
        if (prime):
            primes.append(candidate)
    return primes


def isWinner(x, nums):
    """
    stimulgame
    """
    if (type(nums) is not list or not all([type(n) is int for n in nums]) or
            not all([n > -1 for n in nums])):
        return None

    if (type(x) is not int or x != len(nums)):
        return None
    nums.sort()
    primes = findPrimesToN(nums[-1])
    if (primes is None):
        return None

    Maria_wins = 0
    Ben_wins = 0
    for n in nums:
        prime_ct = 0
        for prime in primes:
            if (prime <= n):
                prime_ct += 1
            else:
                break
        if prime_ct % 2 == 0:
            Ben_wins += 1
        else:
            Maria_wins += 1

    if (Maria_wins > Ben_wins):
        return "Maria"
    elif (Ben_wins > Maria_wins):
        return "Ben"
    else:
        return None

