if True:
    print('True is true')

expression = (2 + 1) * 5

if expression:
    print('True')

if expression == 123:
    print('123')

if expression is True:
    print('Expression is true')

a_boolean = True

if a_boolean:
    print('a true')

if a_boolean is True:
    print('a true')

a_null = None

if a_null:
    print('a not None')

if not a_null:
    print('a None')

if a_null is None:
    print('a None')

if a_null is not None:
    print('a not None')

# Falsy values
if []:
    pass

if {}:
    pass

if 0:
    pass

if '':
    pass

today = 'Monday'
hour = '15:00'

if today == 'Monday':
    pass
elif today == 'Tuesday':
    pass
elif today == 'Wednesday':
    pass
else:
    pass

if today == 'Monday':
    if hour == '15:00':
        pass
    else:pass
else:
    pass