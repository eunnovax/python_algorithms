# s is a string encoded as bytearray
def reverse_words(s):
    # s = s.encode('utf-8')
    # reverse the whole s
    s.reverse()
    # reverse individual words 
    def reverse_word(s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start, end = start + 1, end - 1

    #find the end of a word and apply reverse_word method
    start = 0
    while True:
        end = s.find(b' ', start)
        if end < 0:
            break
        # reverse each word in the string
        reverse_word(s, start, end - 1)
        start = end + 1
    # reverse the last word since s.find(b'', start) doesn't find the last word
    # because of the end of a string has no space ''
    reverse_word(s, start, len(s) - 1)
    s = s.decode('utf-8')
    return s

s = "ABCD EFGH"
b = bytearray()
b.extend(map(ord, s))

print(reverse_words(b))