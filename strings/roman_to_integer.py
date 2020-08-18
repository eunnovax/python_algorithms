import functools

def roman_to_integer(s):
    T = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    for i in range(len(s)):
        if i == len(s) - 1:
            sum += T[s[i]]
        else:
            if T[s[i]] < T[s[i+1]]:
                sum -= T[s[i]]
                print('roman numeral', T[s[i]])
                print('sum after subtract', sum)
            else:
                sum += T[s[i]]
                print('roman numeral', T[s[i]])
                print('sum after addition', sum)
    return sum
    # return functools.reduce(lambda sum, i: sum + (-T[s[i]] if T[s[i]] < T[s[i+1]] else T[s[i]] ), range(len(s)-1), T[s[-1]])

print(roman_to_integer('MCMX'))