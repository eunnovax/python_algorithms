def is_palindrome_pure_string(s):
    return all(s[i] == s[~i] for i in range(len(s) // 2))

def is_palindrome(s):
    i,j = 0, len(s) - 1
    while i < j:
        # i & j both skip non-alphanumeric characters
        while not s[i].isalnum() and i<j:
            i += 1
        while not s[j].isalnum() and i<j:
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i,j = i+1, j-1
    return True
words = ["howareyou", "race!car"]
for word in words:
    print(is_palindrome(word))

# Time: O(n), Space: O(1)