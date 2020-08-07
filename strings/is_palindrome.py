def is_palindrome(s):
    return all(s[i] == s[~i] for i in range(len(s) // 2))

words = ["howareyou", "racecar"]
for word in words:
    print(is_palindrome(word))

# Time: O(n), Space: O(1)