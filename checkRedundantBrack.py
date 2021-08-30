
from sys import stdin


def checkRedundantBrackets(expression):
    stk = list()
    for i in range(len(expression)) :
        if (expression[i] == '(') or (find(expression[i])) :
            stk.append(expression[i])
        elif expression[i] == ')' :
            hasOperator = False
            while not isEmpty(stk) and top(stk) != '(' :
                stk.pop()
                hasOperator = True
            if not hasOperator :
                return True
            if not isEmpty(stk) :
                stk.pop()
    return False








def find(ch) :
    if ch =='+' or ch=='-' or ch=='*' or ch=='/':
        return True
    return False

def isEmpty(stack) :
    return len(stack) == 0

def top(stack) :
    return stack[len(stack) - 1]



#main
expression = stdin.readline().strip()

if checkRedundantBrackets(expression) :
	print("true")

else :
	print("false")
