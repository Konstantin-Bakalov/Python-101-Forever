# Multiple assignments

x, y = (1, 2)
print(x, y)

x, y = [3, 4]
print(x, y)

# order not guaranteed
x, y = { 'key1': 'value1', 'key2': 'value2' }
print(x, y)

# order not guaranteed
x, y = { 1, 2 }
print(x, y)

x, y = { 2, 1 }
print(x, y)

# x, y = (1,) ValueError
# x, y = (1, 2, 3) ValueError

for a, b, c in [(1, 2, 3), (4, 5, 6)]:
    print(a, b, c)


# String formatting

a = 10
f_string = f'this is the number ten - {a}'
format_string = 'this is the number ten - {a}'.format(a=a)

print(f_string)
print(format_string)


words = ['A', 'list', 'of', 'strings']
print(' '.join(words))
