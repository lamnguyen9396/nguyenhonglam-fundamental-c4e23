#1. Generate quiz:
from random import randint,choice
# from random import * # * là import tất cả
import function_intro #cach 1
from function_intro import eval #cach 2

def generate_quiz():
    x=randint(0,10)
    y=randint(0,10)
    error=randint(-1,1)
    o=choice(["+","-","*","/"])

# s=function_intro.eval(x,y,op) #cach 1
    r=eval(x,y,o)+error
    return x,y,o,r
a,b,op,r=generate_quiz()

print(a,op,b,'=',r) #string formating
n=input('(y/n)?').upper()
if n=="Y":
    if error==0:
        print('correct')
    else:
        print('false')
if n=="N":
    if error==0:
        print('false')
    else:
        print('correct')
