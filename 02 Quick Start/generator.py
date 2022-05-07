#!/usr/local/bin/python3.4

def isprime(n):
    return False if n == 1 else all(n % x != 0 for x in range(2, n))

def primes(n = 1):
   while(True):
       if isprime(n): yield n
       n += 1

for n in primes():
    if n > 100: break
    print(n)

