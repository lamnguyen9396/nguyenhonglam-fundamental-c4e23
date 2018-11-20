a=int(input('a='))
b=int(input('b='))
c=a+b
print('c=a+b=',c)

x=int(input('x='))
y=int(input('y='))
op=input('operations(+,-,*,/):')
if op=='+':
    z=x+y
elif op=='-':
    z=x-y
elif op=='*':
    z=x*y
elif op=='/':
    z=x/y
print(z)