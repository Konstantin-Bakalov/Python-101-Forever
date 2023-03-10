def is_prime(n):
    for i in range(2, n // 2 + 1, 1):
        if n % i == 0:
            return False
        
    return True

def goldbach(n):
    if n % 2 == 1:
        return None
    
    result = []
    for i in range(2, n // 2 + 1):
        if is_prime(i) and is_prime(n - i):
            result.append((i, n - i))
    
    return result

tests = [
    (4, [(2,2)]),
    (6, [(3,3)]),
    (8, [(3,5)]),
    (10, [(3,7), (5,5)]),
    (100 ,[(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)]),
    (5, None)
]

for input, expected in tests:
    print(goldbach(input) == expected)