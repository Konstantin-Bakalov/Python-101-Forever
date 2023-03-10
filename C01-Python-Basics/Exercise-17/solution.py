import enum

class Direction(enum.Enum):
    HORIZONTAL_LEFT = "HORIZONTAL_LEFT"
    HORIZONTAL_RIGHT = "HORIZONTAL_RIGHT"

    VERTICAL_DOWN = "VERTICAL_DOWN"
    VERTICAL_UP = "VERTICAL_UP"

    DIAGONAL_UP_RIGHT = "DIAGONAL_UP_RIGHT"
    DIAGONAL_UP_LEFT = "DIAGONAL_UP_LEFT"

    DIAGONAL_DOWN_RIGHT = "DIAGONAL_DOWN_RIGHT"
    DIAGONAL_DOWN_LEFT = "DIAGONAL_DOWN_LEFT"

def outside_of_bounds(point, matrix):
    x, y = point

    MIN_X = 0
    MAX_X = len(matrix) - 1

    MIN_Y = 0
    MAX_Y = len(matrix[0]) - 1

    return x < MIN_X or x >MAX_X or y < MIN_Y or y > MAX_Y


def get_word(matrix, n, point, direction):
    dx = 0
    dy = 0

    if direction == Direction.HORIZONTAL_RIGHT:
        dx = 0
        dy = 1

    if direction == Direction.HORIZONTAL_LEFT:
        dx = 0
        dy = -1

    if direction == Direction.VERTICAL_UP:
        dx = -1
        dy = 0

    if direction == Direction.VERTICAL_DOWN:
        dx = 1
        dy = 0

    if direction == Direction.DIAGONAL_UP_RIGHT:
        dx = -1
        dy = 1

    if direction == Direction.DIAGONAL_UP_LEFT:
        dx = -1
        dy = -1

    if direction == Direction.DIAGONAL_DOWN_RIGHT:
        dx = 1
        dy = 1

    if direction == Direction.DIAGONAL_DOWN_LEFT:
        dx = 1
        dy = -1

    start_x, start_y = point
    n_counter = 0
    chars = []

    while n_counter != n:
        if outside_of_bounds((start_x, start_y), matrix):
            return None
        
        chars.append(matrix[start_x][start_y])

        start_x += dx
        start_y += dy

        n_counter += 1

    return ''.join(chars)

def word_counter(matrix, word):
    result = 0

    for row_index in range(len(matrix)):
        for col_index in range(len(matrix[row_index])):
            for direction in Direction:
                found_word = get_word(matrix,
                    len(word),
                    (row_index, col_index),
                    direction)
                
                if found_word == word:
                    result += 1

    if word == word[::-1]:
        result = result // 2
        
    return result

word = "ivan"
matrix = [
    ["i", "v", "a", "n"],
    ["e", "v", "n", "h"],
    ["i", "n", "a", "v"],
    ["m", "v", "v", "n"],
    ["q", "r", "i", "t"]
]

matrix[2][3]
print(word_counter(matrix, word) == 3)

word = "actually"
matrix = [
    ["i", "v", "a", "n", "q", "h", "r", "e", "z", "g", "t", "z", "o", "y", "m"],  # noqa
    ["e", "v", "n", "h", "t", "r", "x", "e", "k", "y", "d", "a", "i", "l", "c"],  # noqa
    ["i", "a", "c", "t", "u", "a", "l", "l", "y", "m", "c", "x", "r", "l", "e"],  # noqa
    ["m", "v", "c", "n", "p", "u", "a", "m", "n", "t", "l", "u", "e", "a", "a"],  # noqa
    ["q", "r", "i", "t", "w", "e", "a", "q", "u", "p", "r", "x", "t", "u", "z"],  # noqa
    ["p", "e", "a", "c", "t", "u", "a", "l", "l", "y", "w", "p", "y", "t", "m"],  # noqa
    ["o", "y", "h", "t", "r", "e", "l", "u", "f", "p", "q", "n", "z", "c", "s"],  # noqa
    ["p", "a", "c", "t", "u", "a", "l", "l", "y", "u", "r", "e", "q", "a", "r"]   # noqa
]
print(word_counter(matrix, word) == 4)

word = "madam"
matrix = [
    ["z", "v", "a", "n", "q", "h", "r", "e", "z", "g", "t", "z"],
    ["e", "v", "m", "h", "t", "r", "x", "e", "k", "y", "m", "a"],
    ["i", "a", "c", "a", "u", "a", "l", "l", "y", "a", "c", "x"],
    ["m", "v", "c", "n", "d", "u", "a", "m", "d", "t", "l", "u"],
    ["q", "t", "i", "t", "w", "a", "a", "a", "u", "p", "r", "x"],
    ["p", "e", "m", "a", "d", "a", "m", "l", "l", "y", "w", "p"],
    ["o", "y", "h", "t", "e", "e", "l", "u", "f", "p", "q", "n"],
    ["p", "a", "c", "t", "u", "a", "l", "l", "y", "u", "r", "e"]
]
print(word_counter(matrix, word) == 3)