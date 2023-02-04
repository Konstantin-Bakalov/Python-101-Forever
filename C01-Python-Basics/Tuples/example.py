a_list = [1, 2, 3]
a_tuple = (1, 2, 3)

empty_typle = ()
one_element = (1,)

another_tuple = 1, 2, 3
another_one_element = 1,

print(a_tuple == another_tuple)
print(one_element == another_one_element)


# Enumerate

for index, value in enumerate(['a', 'b', 'c', 'd']):
    print(index, value)


# Length

print(len(empty_typle))
print(len(a_tuple))


# Boolean value

print(bool(empty_typle) is False)
print(bool(a_tuple) is True)


# Iterating over tuples

for index in range(len(a_tuple)):
    print(a_tuple[index])


# Comparing tuples

print(() == ())
print((1,) == (1,))
print((1, 2) == (1,))
print((1, 2) == (2, 1))

# ()[1] IndexError


# Concatinating tuples

print((1, 2) + (3, 4))


# Member access

print(1 in (1, 2))
print(1 in ())
print(1 not in ())