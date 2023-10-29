
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self,element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def gettop(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None
    
    def is_empty(self):
        return len(self.stack) == 0
# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.gettop()

def brace_match(s):
    match = {'(':')','[':']','{':'}'}
    stack = Stack()
    for ch in s:
        if ch in {'(','[','{'}:
            stack.push(ch)
        elif ch == ')':
            if stack.gettop() == '(':
                stack.pop()
            else:
                print('多余的括号为:'+ ch)
                return False  
        elif ch == ']':
            if stack.gettop() == '[':
                stack.pop()
            else:
                print('多余的括号为:'+ ch)
                return False
        elif ch == '}':
            if stack.gettop() == '{':
                stack.pop()
            else:
                print('多余的括号为:'+ ch)
                return False
    if len(stack.stack) == 0:
        print('书写合法')
    else:
        print('书写有误,多余的括号为')
        print(stack.stack)

# s = '([)])'
# brace_match(s)

def simple_brace_match(s):
    match = {')':'(',']':'[','}':'{'}
    stack = Stack()
    for ch in s:
        if ch in {'(','[','{'}:
            stack.push(ch)
        else:  #ch in {')',']','}'}
            if stack.is_empty():
                return False
            elif stack.gettop() == match[ch]:
                stack.pop()
            else:
                return False
    if stack.is_empty():
        return True
    else:
        return False

print(simple_brace_match('[{()}{()}]'))