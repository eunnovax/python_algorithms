def remove_and_replace(size, s):
    # forward iteration to delete b's and count a's:
    write_idx, a_count = 0, 0
    for i in range(size):
        if s[i] != 'b':
            s[write_idx] = s[i]
            write_idx += 1
        if s[i] == 'a':
            a_count += 1

    # backward iteration to replace a's with dd's from the end
    current_idx = write_idx - 1
    write_idx += a_count - 1
    while current_idx >= 0:
        if s[current_idx] == 'a':
            s[write_idx-1:write_idx+1] = 'dd'
            write_idx -= 2
        else:
            s[write_idx] = s[current_idx]
            write_idx -= 1
        current_idx -= 1

    return s

str_arr = ['a','d','p','e','d','a','a','b','e','b','r','c']
size = 10
print(remove_and_replace(size, str_arr))

#time: O(n), space: O(1)