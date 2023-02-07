def iban_formatter(iban):
    list = []
    counter = 0

    for character in iban:
        if character == ' ':
            continue

        if counter == 4:
            list.append(' ')
            counter = 0

        list.append(character)
        counter += 1

    return ''.join(list)


tests = [
    ("BG80BNBG96611020345678", "BG80 BNBG 9661 1020 3456 78"),
    ("BG80 BNBG 9661 1020 3456 78", "BG80 BNBG 9661 1020 3456 78"),
    ("BG14TTBB94005362446381", "BG14 TTBB 9400 5362 4463 81"),
    ("BG91UNCR70001864961754", "BG91 UNCR 7000 1864 9617 54")
]

for input, expected in tests:
    print(iban_formatter(input) == expected)