def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)

def fact_digits(n):
    result = 0
    for digit in str(abs(n)):
        result += fact(int(digit))

    return result


tests = [
    (101, 3),
    (111, 3),
    (145, 145),
    (999, 1088640)
]

for input, expected in tests:
    print(fact_digits(input) == expected)