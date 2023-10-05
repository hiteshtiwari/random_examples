def parethesis_pair(S):
    stack = []
    pairs  = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    
    for i in S:
        if i in pairs:
            stack.append(i)
        elif len(stack) == 0 or i != pairs[stack.pop()]:
            return False
    return len(stack) == 0

s = '[[]]{}([][])'
print(parethesis_pair(s))
