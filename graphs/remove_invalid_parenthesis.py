def isBalanced(s):
        counter = 0
        for x in s:
            if x == '(':
                counter += 1
            elif x == ')':
                counter -= 1
            if counter < 0 :
                return False
        return True

def removeInvalidParenthesis(s):
    q = list()
    distance = 0
    visit = {}
    balanced = list()
    q.append(s)
    found = 0
    while len(q) > 0:
        u = q.pop(0)
        if visit.get(u, 0):
            continue
        visit[u] = 1
        if isBalanced(u):
            found = 1
            balanced.append(u)
        if found:
            continue
        for i in range(len(u)):
            if u[i] == '(' or u[i] == ')':
                v = u[0:i] + u[i+1:]
                q.append(v)
    return balanced

word = "(a)())()"
print(removeInvalidParenthesis(word))