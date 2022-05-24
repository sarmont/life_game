import string
import random

letters = set(string.ascii_letters) - set('lIoO')
digits = set(string.digits) - set('10')
let_dig = letters | digits


def generate_password(m):
    pas = ''.join(random.sample(list(let_dig), k=m))
    return pas


def main(n, m):
    passes = set()
    while len(passes) != n:
        f1 = False
        f2 = False
        f3 = False
        pa = generate_password(m)
        for el in pa:
            if el in string.ascii_letters.upper():
                f1 = True
            elif el in string.ascii_letters.lower():
                f2 = True
            elif el in string.digits:
                f3 = True
        if f1 is True and f2 is True and f3 is True:
            passes.add(pa)
    return list(passes)



print(main(1,3))