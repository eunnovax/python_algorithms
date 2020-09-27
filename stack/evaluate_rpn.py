def evaluate_rpn(expr):
    x = []
    delimiter = ','
    operators = {
        '+': lambda x,y: x + y,
        '-': lambda x,y: x - y,
        '*': lambda x,y: x * y,
        '/': lambda x,y: x / y
    }
    for item in expr.split(delimiter):
        if item in operators:
            x.append(operators[item](x.pop(), x.pop()))
        else: # item is a number
            x.append(int(item))
    return x[-1]

prnw = '3,4,+,2,*,1,+'
print(evaluate_rpn(prnw))

# Time - O(n)