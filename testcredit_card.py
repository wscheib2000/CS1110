import credit_card

print(credit_card.check(1))
if credit_card.check(1):
    print('ERROR: 1 is not valid')

print(credit_card.check(240))
if credit_card.check(240):
    print('GOOD: 240 is valid')

print(credit_card.check(9548))
if credit_card.check(9548):
    print('GOOD: 9548 is valid')

print(credit_card.check(5490123456789129))
if credit_card.check(5490123456789129):
    print('ERROR: 5490123456789129 is not valid')
