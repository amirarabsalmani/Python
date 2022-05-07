#!/usr/local/bin/python3.4

#Main method
def main():
    for n in primes():
        if n > 100: break
        print(n)


def isprime(n):
    return False if n == 1 else all(n % x != 0 for x in range(2, n))

#Generator
def primes(n = 1):
   while(True):
       if isprime(n): yield n #Generator keyword
       n += 1

if __name__ == "__main__": main()
