class Stack():
    def __init__(self):
        self.items = []
    def __getitem__(self, number):
        return self.items[number]
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def get_stack(self):
        return self.items
    def is_empty(self):
        return self.items == []
    def peek(self):
        if not self.is_empty():
            return self.items[-1]

def balanced(strin):
    bracket = Stack()
    for item in strin:
        if(not bracket.is_empty()):
            if(item == ')' and bracket[-1] == '('):
                bracket.pop()
            elif (item == ']' and bracket[-1] == '['):
                bracket.pop()
            elif (item == '}' and bracket[-1] == '{'):
                bracket.pop()
        elif (item == '(' or item == '[' or item == '{'):
            bracket.push(item)
        elif (bracket.is_empty() and (item == ')' or item == ']' or item == '}')):
            return False
        else:
            return False
        
    if(bracket.is_empty()):
        return True
    else:
        return False

def reverse(str):
    stack = Stack()
    for i in range(len(str)):
        stack.push(str[i])

    reverse_str = ''
    while not stack.is_empty():
        reverse_str += stack.pop()

    return reverse_str
    
print(balanced('{(almas)}'))
input_str = 'Almas'
print(reverse(input_str))
# s = Stack()
# s.is_empty()
# s.push("A")
# s.push("B")
# # print(s.get_stack())
# s.push("X")
# print(s.get_stack())
# print(s.peek())
# s.pop()
# print(s.peek())
