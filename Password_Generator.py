import random
lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
upper_alphabet = lower_alphabet.upper()
numbers = '1234567890'
symbols = '!@#$%^&*)(_-=+";:.,?'
all = list(lower_alphabet + upper_alphabet + numbers + symbols)
random.shuffle(all)
def generate(length):
    password = []
    for i in range(length):
        password.append(random.choice(all))
    random.shuffle(password)
    print(''.join(password))
