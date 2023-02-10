def anagrams(word1, word2):
    list1 = word1.lower().replace(' ', '')
    list2 = word2.lower().replace(' ', '')

    return sorted(list1) == sorted(list2)


tests = [
    ("listen", "silent", True),
    ("LISTEN", "silent", True),
    ("python", "ruby", False),
    ("New York Times", "monkeys write", True),
    ("snake", "sssnakee", False)
]

for word1, word2, expected in tests:
    print(anagrams(word1, word2) == expected)