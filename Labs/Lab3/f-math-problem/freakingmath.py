from random import *

def generate_quiz():
    x=randint(0,10)
    y=randint(0,10)
    error=randint(-1,1)
    o=choice(["+","-","*","/"])

    r=eval(str(x)+o+str(y)+str(error))
    return [x, y, o, r]

def check_answer(x, y, op, result, user_choice):
    pass
    
