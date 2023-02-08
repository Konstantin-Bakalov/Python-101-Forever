def sum_matrix(m):
    result = 0
    for item in m:
        for element in item:
            result += element

    return result

m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
m3 = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]

tests = [
    ([], 0),
    ([[]], 0),
    (m1, 45),
    (m2, 0),
    (m3, 55)
]

for input, expected in tests:
    print(sum_matrix(input) == expected)