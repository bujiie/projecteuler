#!/usr/bin/env python
import sys
import math

n = int(sys.argv[1])
factorial = math.factorial(n)

def digits(number):
  return map(lambda n: int(n), str(number))

sum = reduce(lambda acc, num: acc + num, digits(factorial))
print sum