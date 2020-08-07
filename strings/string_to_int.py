import string, functools

def int_to_str(x):
    is_negative = False
    if x < 0:
        x, is_negative = -x, True

    s=[]
    while True:
        # chr(ord('0') + <0..9>) - to convert from integer to string
        # x % 10 - to get the last element in integer
        s.append(chr(ord('0') + x % 10))
        # to remove the last element
        x //= 10
        # out-of-loop condition
        if x == 0:
            break
    # ''.join(s) - s = should be a list of strings!
    return ('-' if is_negative else '') + ''.join(reversed(s))

def str_to_int(s):
    #string.digits.index(c) - to convert from string to integer
    return functools.reduce(lambda cumul_sum, c: cumul_sum * 10 + string.digits.index(c), s[s[0] == '-':], 0) * (-1 if s[0] == '-' else 1)

x = 123
print(type(int_to_str(x)))
s = '345'
print(type(str_to_int(s)))

print(type(string.digits.index('6')))