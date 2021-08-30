
from sys import stdin


def isBalanced(expression) :
    data = []
    
    for i in expression:
        if i=="(":
            data.append('(')
            
        else:
            if len(data) != 0:
                data.pop()
            
    if len(data) == 0:
        return True
    else:
        False



#main
expression = stdin.readline().strip()

if isBalanced(expression) :
	print("true")

else :
	print("false")
