#!/usr/bin/python3
"""Module for Prime Game"""


def isWinner(x, nums):
    """
    Determines the winner of a set of prime number removal games.

    Args:
        x (int): The number of rounds.
        nums (list of int): A list of integers representing the
        upper bounds of each set.

    Returns:
        str: The name of the player who won the most rounds ("Ben" or "Maria").
        None: If the winner cannot be determined.
    """
    if not _validate_input(x, nums):
        return None

    max_num = max(nums)
    primes = _sieve_of_eratosthenes(max_num)

    ben_score = sum(1 for n in nums if sum(primes[:n+1]) % 2 == 0)
    maria_score = x - ben_score

    if ben_score > maria_score:
        return "Ben"
    elif maria_score > ben_score:
        return "Maria"
    else:
        return None


def _validate_input(x, nums):
    """Validate the input parameters."""
    return x > 0 and nums is not None and x == len(nums)


def _sieve_of_eratosthenes(n):
    """
    Generate a list of prime numbers up to n using the Sieve of
    Eratosthenes algorithm.

    Args:
        n (int): The upper bound of the range to check for primes.

    Returns:
        list: A list where index i is 1 if i is prime, 0 otherwise.
    """
    sieve = [1] * (n + 1)
    sieve[0] = sieve[1] = 0

    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i*i::i] = [0] * len(sieve[i*i::i])

    return sieve


if __name__ == "__main__":
    # Add any test cases or main execution code here
    pass
