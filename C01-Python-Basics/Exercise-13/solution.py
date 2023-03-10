def prime_factorization(n):
    result = []
    i = 2
    while n > 1:
        times = 0
        while n % i == 0:
            n = n // i
            times = times + 1

        if times > 0:
            result.append((i, times))

        i = i + 1

    return result
            
tests = [
    (10, [(2, 1), (5, 1)]),
    (14, [(2, 1), (7, 1)]),
    (356, [(2, 2), (89, 1)]),
    (89, [(89, 1)]),
    (1000, [(2, 3), (5, 3)])
]

for input, expected in tests:
    print(prime_factorization(input) == expected)