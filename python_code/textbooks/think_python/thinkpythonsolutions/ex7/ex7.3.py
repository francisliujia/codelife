# #!/usr/bin/env python3

# """
# Exercise 7.3.
# The mathematician Srinivasa Ramanujan found an infinite series that can be used to
# generate a numerical approximation of 1/pi.

# https://en.wikipedia.org/wiki/Pi#Rapidly_convergent_series

# Write a function called estimate_pi that uses this formula to compute and return
# an estimate of pi. It should use a while loop to compute terms of the summation
# until the last term is smaller than 1e-15 (which is Python notation for 10**-15).
# You can check the result by comparing it to math.pi.

# Solution: http://thinkpython2.com/code/pi.py
# """

# # Couldn't figure this one out.

from __future__ import print_function, division

import math


def factorial(n):
    """Computes factorial of n recursively."""
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result


def estimate_pi():
    """Computes an estimate of pi.
    Algorithm due to Srinivasa Ramanujan, from 
    http://en.wikipedia.org/wiki/Pi
    """
    total = 0
    k = 0
    factor = 2 * math.sqrt(2) / 9801
    while True:
        num = factorial(4*k) * (1103 + 26390*k)
        den = factorial(k)**4 * 396**(4*k)
        term = factor * num / den
        total += term
        
        if abs(term) < 1e-15:
            break
        k += 1

    return 1 / total

print(estimate_pi())