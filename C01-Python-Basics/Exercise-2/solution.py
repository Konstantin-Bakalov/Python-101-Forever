def sum_of_digits(n):
     result = 0
     for num in list(str(abs(n))):
        result += int(num)

     return result

    
tests = [
    (1325132435356, 43),
    (123, 6),
    (6, 6),
    (-10, 1)
]

for n, expected in tests:
    result = sum_of_digits(n)

    print(result == expected)