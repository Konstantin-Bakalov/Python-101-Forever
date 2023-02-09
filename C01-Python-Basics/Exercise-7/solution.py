from enum import Enum


class Monotonicity(Enum):
    INCREASING = 1
    DECREASING = 2
    NONE = 3

def increasing_or_decreasing(ns):
    increasing = True
    decreasing = True

    for i in range(len(ns) - 1):
        if ns[i] >= ns[i + 1]:
            increasing = False

        if ns[i] <= ns[i + 1]:
            decreasing = False

    if len(ns) <= 1:
        return Monotonicity.NONE
        
    return Monotonicity.INCREASING if increasing else (Monotonicity.DECREASING if decreasing else Monotonicity.NONE) 

tests = [
    ([1, 2, 3, 4, 5], Monotonicity.INCREASING),
    ([5, 6, -10], Monotonicity.NONE),
    ([1, 1, 1, 1], Monotonicity.NONE),
    ([9, 8, 7, 6], Monotonicity.DECREASING),
    ([], Monotonicity.NONE),
    ([1], Monotonicity.NONE),
    ([1, 100], Monotonicity.INCREASING),
    ([1, 100, 100], Monotonicity.NONE),
    ([100, 1], Monotonicity.DECREASING),
    ([100, 1, 1], Monotonicity.NONE),
    ([100, 1, 2], Monotonicity.NONE)
]

for input, expected in tests:
    print(increasing_or_decreasing(input) == expected)