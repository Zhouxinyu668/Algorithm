 

def f(stack):
    result = stack.pop()
    if len(stack) == 0:
        return result
    else:
        last = f(stack)
        stack.append(result)
        return last

def reverse(stack):
    if len(stack) == 0:
        return
    last = f(stack)
    reverse(stack)
    stack.append(last)