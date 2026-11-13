def prime_factors(n):
    """Return the prime factors of a given number n as a list."""
    factors = []
    divisor = 2
    while divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 1

    return factors


prime_factors_of_60 = prime_factors(60)
print(prime_factors_of_60)
