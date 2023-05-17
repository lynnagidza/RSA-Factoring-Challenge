#!/usr/bin/python3
"""RSA factoring problem"""
import sys
import math


def factorize(n):
    """Factorize a number using trial division"""
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors


def main():
    """Main function"""
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        return

    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            numbers = file.readlines()
            for number in numbers:
                n = int(number.strip())
                factors = factorize(n)
                print(f"{n} = {'*'.join(map(str, factors))}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")


if __name__ == '__main__':
    main()
