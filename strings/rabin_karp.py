import functools

def rabin_karp(t, s):
    if len(s) > len(t):
        return -1 #s is not a substring of t
    BASE = 26 # alphabet base conversion
    t_hash = functools.reduce(lambda h, c: h * BASE + ord(c), t[:len(s)], 0)
    s_hash = functools.reduce(lambda h, c: h * BASE + ord(c), s, 0)
    power_s = BASE**max(len(s) - 1, 0)

    for i in range(len(s), len(t)):
        if t_hash == s_hash and t[i-len(s): i] == s:
            return i - len(s) # found a match
        
        # use rolling hash to compute the hash code
        t_hash -= ord(t[i-len(s)]) * power_s
        t_hash = t_hash * BASE + ord(t[i])

    # tries to match s and t[-len(s):]
    if t_hash == s_hash and t[-len(s):] == s:
        return len(t) - len(s)
    return -1 #s is not a substring of t



# 26 characters in an alphabet
BASE = 26
t = 'abhcrdocdcjkt'
s = 'crd'
print(rabin_karp(t,s))
# i = 3
# t_hash = functools.reduce(lambda h, c: h * BASE + ord(c), t[:len(s)], 0)
# s_hash = functools.reduce(lambda h, c: h * BASE + ord(c), s, 0)
# power_s = BASE**max(len(s) - 1, 0)
# print('t_hash', t_hash)
# print('s_hash', s_hash)
# print('power_s', power_s)
# t_hash -= ord(t[i-len(s)]) * power_s
# print('t_hash1', t_hash)
# t_hash = t_hash * BASE + ord(t[i])
# print('t_hash2', t_hash)

