empty_set = set() # empty_dict = {}

a_set = { 'Python', 'Java', 'Java', 'Python' }
another_set = set(['Python', 'Java', 'Java', 'Python', 'Ruby'])

a_set.add('Ruby')
a_set.add('Ruby')

print(a_set)
print(len(a_set))
print(a_set == another_set)


# Size of a set

print(len({1, 2, 3}))


# Boolean value

print(bool(set()))
print(bool({1, 1, 1}))


# Iterating over a set

for item in { 1, 2, 3, 4}:
    print(item)

# Comparing sets

print({ 1, 2 } == { 2, 2, 1 })


# Membership access

print(1 in { 1, 2})
print(1 not in set())


# Intersecting sets

a = { 1, 2, 3 }
b = { 4, 5, 6, 3 }

print(a | b)
print(a & b)
print(a - b)
print(b - a)
print({ 1, 2 } & { 3, 4 })

l = [ 1, 2, 1, 3, 3, 4, 4]
unique = list(set(l))