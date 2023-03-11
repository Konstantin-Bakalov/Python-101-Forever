KEYPAD = {
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz"
}

def group(items):
    result = []
    count = 1

    for i in range(len(items) - 1):
        if items[i] == items[i + 1]:
            count += 1
        else:
            result.append([items[i]] * count)
            count = 1
    
    result.append([items[len(items) - 1]] * count)

    return result

def numbers_to_message(pressed_sequence):
    letters = []
    grouped = group(pressed_sequence)
    upper = False

    for grp in grouped:
        key = grp[0]
        pressed = len(grp)

        if key == -1:
            continue

        if key == 1:
            upper = True
            continue

        if key == 0:
            letters.append(' ' * pressed)
            continue

        sequence = KEYPAD[key]
        letter = sequence[(pressed - 1) % len(sequence)]

        if upper:
            letter = letter.upper()
            upper = False

        letters.append(letter)

    return ''.join(letters)

tests = [
    (
        [0, 0, 0, 0],
        "    "
    ),
    (
        [2, -1, 2, 2, -1, 2, 2, 2],
        "abc"
    ),
    (
        [2, 2, 2, 2],
        "a"
    ),
    (
        [1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2],
        "Ivo e Panda"
    ),
    (
        [2, 3, 4, 5, 6, 7, 8, 9],
        "adgjmptw"
    ),
    (
        [2, -1, 3,-1, 4, -1, 5, -1, 6, -1, 7, -1, 8, -1, 9],  # noqa
        "adgjmptw"
    ),
    (
        [0, -1, 0, -1, 0, -1, 0],
        "    "
    ),
    (
        [2, 2, 2, -1, 2],
        "ca"
    ),
]

for sequence, expected in tests:
    result = numbers_to_message(sequence)

    print(result == expected, result)