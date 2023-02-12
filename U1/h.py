p = ['5','6','2','+', '*' ,'12', '4', '/', '-']
stack=[]
op=['+','-','/','*','^']
for i in range (len(p)):
    if p[i] in op:
        if p[i] == '+':
            B=int(stack.pop())
            A=int(stack.pop())
            c= A+B
            stack.append(c)
        elif p[i] == '*':
            B=int(stack.pop())
            A=int(stack.pop())
            c=A*B
            stack.append(c)
        elif p[i] == '/':
            B=int(stack.pop())
            A=int(stack.pop())
            c= A/B
            stack.append(c)
        elif p[i] == '-':
            B=int(stack.pop())
            A=int(stack.pop())
            c= A-B
            stack.append(c)
        elif p[i] == '^':
            B=int(stack.pop())
            A=int(stack.pop())
            c= A**B
            stack.append(c)
    else:
        stack.append(p[i])
value = stack.pop()
print(value)

