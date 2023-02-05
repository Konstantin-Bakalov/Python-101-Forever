# Example 1

a = 1
b = a

print(id(a) == id(b))

a = 2
print(id(a) == id(b))
print(a, b)


# Example 2

a = [1, 2, 3]
b = a

print(id(a) == id(b))

a = [3, 4, 5]
print(id(a) == id(b))
print(a, b)


# Example 3

a = [1, 2, 3]
b = a

print(id(a) == id(b))

b.append(4)

print(id(a) == id(b))
print(a, b)

a.append(5)
print(id(a) == id(b))
print(a, b)


# is keyword

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)

print(a is b)

print(id(a) == id(b))


a = True
b = True

print(a == b)

print(a is b)

print(id(a) == id(b))


# Example 4

def f(x):
    x.append(4)


a = [1, 2, 3]
f(a)
print(a)