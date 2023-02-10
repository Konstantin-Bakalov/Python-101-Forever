def is_credit_card_valid(number):
    num = str(number)
    list = []
    counter = 1
    for i in range(len(num) - 1, -1, -1):
        if counter % 2 == 0:
            double = int(num[i]) * 2
            if double > 9:
                list.append(double % 10 + double // 10)
            else:
                list.append(double)
        else:
            list.append(int(num[i]))

        counter += 1
    
    return sum(list) % 10 == 0

tests = [
    (79927398713, True),
    (79927398715, False),
    (4417123456789113, True)
]

for number, expected in tests:
    print(is_credit_card_valid(number) == expected)