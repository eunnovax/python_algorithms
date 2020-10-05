def are_parenthesis_balanced(s):
    stack = []
    count = 0
    for item in s:
        if item == '(' or item == '[' or item == '{':
            stack.append(item)
        elif (item == ')' and stack[-1] == '(') or (item == ']' and stack[-1] == '[') or (item == '}' and stack[-1] == '{'):
            stack.pop()
    return len(stack) == 0

s = '[()[]{()()}'
print(are_parenthesis_balanced(s))

# Time - O(n)
            
def is_well_formed(s):
    stack, lookup = [], { '(': ')', '{': '}', '[': ']' }
    for item in s:
        if item in lookup:
            stack.append(item)
        # Not the opening bracket but the stack is empty OR closing br doesn't match stack top
        elif not stack or lookup[stack.pop()] != item:
            return False
    return not stack
