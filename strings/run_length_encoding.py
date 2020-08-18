def run_length_encoding(s):
    result, i = [], 0
    while i < len(s):
        count = 1
        while i+1 < len(s) and s[i] == s[i+1]:
            count += 1
            i += 1
        result.append(str(count) + s[i])
        i += 1
    return ''.join(result)

def run_length_decoding(s):
    result = []
    if len(s) % 2 != 0:
        return print('string is not encoded properly!')
    for i in range(0, len(s), 2):
        result.append(s[i+1]*int(s[i]))
    return ''.join(result)

word = 'bbbrrrtnmpppp'
print(run_length_encoding(word))
decoded = '4a1b3c2a'
print(run_length_decoding(decoded))
# Time: O(n) from look and say algorithm