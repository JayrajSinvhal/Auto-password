from math import sin
import string
import random


if __name__ == '__main__':
    s1 = string.ascii_uppercase
    # print(s1)
    s2 = string.ascii_lowercase
    # print(s2)
    s4 = string.digits
    # print(s2)
    s3 = string.punctuation
    # print(s3)

    pse = int(input("Enter passowrd length\n"))
    psei = int(input("Do you want numbers in this password? 0 = no 1 =yes\n"))
    s = []
    s.extend(list(s1))
    s.extend(list(s3))
    s.extend(list(s2))
    s.extend(list(s4))
    # print(s)
    random.shuffle(s)
    # print(s)

    sn = []
    sn.extend(list(s1))
    sn.extend(list(s2))
    sn.extend(list(s3))

    # print(sn)

    random.shuffle(sn)

    if psei == 0:
        print(''.join(sn[0:pse]))
    else:
        print(''.join(s[0:pse]))
