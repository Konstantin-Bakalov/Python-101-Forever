def is_number_balanced(number):
    numbers = list(str(number))
    left = 0
    right = 0
    for i in range(len(numbers) // 2):
        left += int(numbers[i])
        right += int(numbers[len(numbers) - i - 1])

    return left == right

tests = [
    (9, True),
    (4518, True),
    (28471, False),
    (1238033, True),
    (2, True)
]

for input, expected in tests:
    print(is_number_balanced(input) == expected)