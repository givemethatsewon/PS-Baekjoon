import sys

while True:
    a = input()
    stack = []
    
    if a == '.':
        break
    
    for i in a:
        if i == '(' or i =='[':
            stack.append(i)
        
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop() #¦ ������ �ٷ� stack �����
            else:
                stack.append(']')
                break
        
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop() #¦ ������ �ٷ� �����
            else:
                stack.append(')')  
                break
            
    if len(stack) == 0:
        print('yes')
    else:
        print('no')