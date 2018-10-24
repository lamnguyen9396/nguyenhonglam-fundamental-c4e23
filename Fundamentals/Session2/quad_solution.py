a=int(input("a="))
print(a)
b=int(input("b="))
print(b)
c=int(input("c="))
print(c)
delta=b**2-4*a*c
if delta<0:
    print("vo nghiem")
elif delta==0:
    x=-b/(2*a)
    print("1 nghiem",x)
else:
    x1=(-b+delta**-0.5)/(2*a)
    x2=(-b-delta**-0.5)/(2*a)
    print("2 nghiem", x1, x2)
