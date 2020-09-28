def shortest_pathname(path):
    if not path:
        raise ValueError('Empty string is not valid for pathname')
    stack = []
    # special case
    if path[0] == '/':
        stack.append('/')
    for item in path:
        if item == '/' and stack[-1] == '/':
            stack.pop()
            print('stack after pop', stack)
        elif item == '/' and stack[-1] == '.' and stack[-2] != '.': # this condition blocks /../
            stack.pop()
            print('stack after pop', stack)
            continue
        elif item == '/' and stack[-1] == '.' and stack[-2] == '.':
            for _ in range(3):
                stack.pop()
                print('stack after pop in loop', stack)
            while not( len(stack) == 0 or stack[-1] == '/'):
                stack.pop()
                print('stack after pop ..', stack, 'stack length', len(stack))
            continue
        stack.append(item)
        print('stack append', stack)
    new_s = "".join(stack)
    return new_s

word = 'scripts//./../scripts/awkscripts/././'
word2 = '/usr/lib/../bin/gcc'
word3 = 'sc//./../tc/awk/././'
print(shortest_pathname(word3))

# Time - O(n)

