#!/usr/bin/python3
"""RSA factoring problem"""
import sys
import sympy


def main():
    """Main function"""
    if len(sys.argv) != 2:
        print("Usage: factor_prime <number>")
        return

    n = int(sys.argv[1])
    factors = list(sympy.primerange(2, int(n ** 0.5) + 1))
    for factor in factors:
        if n % factor == 0:
            print(f"{n} = {factor} * {n // factor}")
            return
    print(f"{n} is prime.")


if __name__ == '__main__':
    main()
