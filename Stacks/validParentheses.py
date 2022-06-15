

s = "{([])}"

def isValid(s):
    stack = []
    openToClose = { ')':'(', '}':'{', ']':'[' }
    for i in s:
        if i not in openToClose:
            print(f'1: {stack}')
            stack.append(i)
            print(f'2: {stack}')
        elif stack and openToClose[i] == stack[-1]:
            print(f'3: {stack}')
            stack.pop()
            print(f'4: {stack}')
        else:
            print(f'5: {stack}')
            return False
    return stack == []
print(isValid(s))


