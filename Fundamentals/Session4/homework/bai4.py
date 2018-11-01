print("Answer the following algebra question:")
print("If x=8, then what is the value of 4(x+3) ?")
ans=[35,36,40,44]
num=[1,2,3,4]
for i in range(len(ans)):
    print(num[i],ans[i],sep=". ")
yourchoice=int(input('Your choice? '))
while not yourchoice==4:
    print(":(")
    yourchoice=int(input('Your choice? '))
    
else:
    print("Bingo")
