def palindromes_count(n):
    result = 0
    for i in range(10, n + 1):
        if is_palindrome(i):
            result += 1

    return result

def is_palindrome(n):
    arr = list(str(n))

    for i in range(len(arr) // 2):
        if arr[i] != arr[len(arr) - i - 1]:
            return False

    return True

tests = [
    (10, 0),
    (20, 1),
    (101, 10),
    (92009, 1009),
    (99999, 1089)
]

for input, expected in tests:
    print(palindromes_count(input) == expected)