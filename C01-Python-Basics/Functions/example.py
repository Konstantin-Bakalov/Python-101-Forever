# Args

def sum1(x):
    result = 0

    for item in x:
        result += item

    return result

print(sum1([1, 2, 3, 4]))


def sum2(*x):
    result = 0
    
    for item in x:
        result += item
    
    return result

print(sum2(1, 2, 3, 4))
print(sum2(*[1, 2, 3, 4])) # splat
print(sum2())


# Kwargs

def keys1(d):
    result = []

    for key in d:
        result.append(key)

    return result

print(keys1({
    'a': 1,
    'b': 2
}))

def keys2(**d):
    result = []

    for key in d:
        result.append(key)

    return result

print(keys2(a=1, b=2))

d = {
    'a': 1,
    'b': 2
}

print(keys2(**d))

def f(*args, **kwargs):
    print(args)
    print(kwargs)

f()
f(1,)
f(1, 2, a=2)