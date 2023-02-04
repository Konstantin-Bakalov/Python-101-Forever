empty_dictionary = {}

extensions = {
    'Python': '.py'
}

extensions['Java'] = '.java'

python_extension = extensions['Python']
python_extension = extensions.get('Python')

# js_extension = extensions['JavaScript'] # KeyError
jsextension = extensions.get('JavaScript') # None


# Iterating over dictionaries

for key in extensions:
    print(key)

for value in extensions.values():
    print(value)

for key, value in extensions.items():
    print(key, value)


# Membership access

'Java' in extensions
'JavaScript' not in extensions


# Size of dictionary

len(extensions)


# Boolean value

bool(empty_dictionary)
bool(extensions)


# Compare dictionaries

{} == {} # True
{ 'foo': 1 } == { 'foo': 1 } # True
{ 'a': 1, 'b': 2 } == { 'b': 2, 'a': 1 } # True
{ 'a': {} } == { 'a': { } } # True