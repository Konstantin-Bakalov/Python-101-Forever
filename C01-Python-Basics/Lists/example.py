languages = []

languages.append('Java')
languages.append('Python')
languages.append('C#')
languages.append('Ruby')

numbers = [1, 2, 3]
empty = []
mixed = [1, True, 'Three', [], None]

if len(empty) == 0:
    print('Empty list')

if numbers:
    print('Numbers is not empty')

if not empty:
    print('empty is empty')

if 1 in numbers:
    print('1 is in numbers')

if 10 in numbers:
    print('10 is in numbers')

for n in numbers:
    print(n)

print(numbers[0])
numbers[0] = 11
print(numbers)

empty.append('something')

print([] == [])
print([1] == [])
print([1, 2] == [2, 1])