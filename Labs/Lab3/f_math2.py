from random import randint, choice

op_list=['+','-','*','/']
op=choice(op_list)
from random import randint
x=randint(0,10)
y=randint(0,10)
error=randint(-1,1)
z=eval(str(x)+op+str(y)+str(error))
print(x,op,y,'=',z) #string formating
a=input('(y/n)?').upper()
if a=="Y":
    if error==0:
        print('correct')
    else:
        print('false')
if a=="N":
    if error==0:
        print('false')
    else:
        print('correct')