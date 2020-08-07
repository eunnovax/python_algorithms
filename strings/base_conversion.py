import functools, string

def convert_base(num_string, b1, b2):
    # deconstruct a string of base1 to an integer of base 10
    is_negative = num_string[0] == '-'
    # string.hexdigit.index(str) - convert from hexdigit string to integer
    num_int = functools.reduce(lambda sum, c: sum*b1 + string.hexdigits.index(c.lower()), num_string[is_negative:], 0)

    # construct a string of base b2
    s=[]
    while True:
        # string.hexdigits[] - convert from integer to hexdigit string
        # x % base b2 - to get the last element in base b2 integer
        s.append(string.hexdigits[num_int % b2].upper())
        # to remove the last element
        num_int //= b2
        # out-of-loop condition
        if num_int == 0:
            break
    # ''.join(s) - s = should be a list of strings!
    return ('-' if is_negative else '') + ''.join(reversed(s))


print(convert_base("1A7", 13, 7))
# Time O(n)
print(type(string.hexdigits[10]))
