#!/usr/local/bin/python3.4

def isprime(n):
    if n == 1:
        print("1 is special")
        return False
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} x {n // x}")
            return False
    print(n, "is a prime number")
    return True

for n in range(1, 20):
    isprime(n)


