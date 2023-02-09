def group(items):
    result = []

    if len(items) == 0:
        return []

    prev = items[0]
    result.append([prev])

    for i in range(1, len(items)):
        if items[i] == prev:
            result[len(result) - 1].append(items[i])
        else:
            result.append([items[i]])

        prev = items[i]
    
    return result

tests = [
    ([1, 1, 1, 2, 3, 1, 1], [[1, 1, 1], [2], [3], [1, 1]]),
    ([1, 2, 1, 2, 3, 3], [[1], [2], [1], [2], [3, 3]]),
    ([], []),
    ([1], [[1]]),
    ([1, 1, 1, 1], [[1, 1, 1, 1]]),
    ([1, 2, 3, 4, 4, 4, 5, 4, 3, 3, 2, 1, 1], [[1], [2], [3], [4, 4, 4], [5], [4], [3, 3], [2], [1, 1]])
]

for input, expected in tests:
    print(group(input) == expected)