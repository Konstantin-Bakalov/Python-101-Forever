def nan_expand(times):
    result = ''
    for i in range(times):
        if i == 0:
            result = 'Not a NaN'
        else:
            result = 'Not a ' + result
    
    return result

tests = [
    (0, ''),
    (1, "Not a NaN"),
    (2, "Not a Not a NaN"),
    (3, "Not a Not a Not a NaN")
]

for input, expected in tests:
    print(nan_expand(input) == expected)