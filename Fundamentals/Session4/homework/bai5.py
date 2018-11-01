print("Answer the following algebra question:")
print("If x=8, then what is the value of 4(x+3) ?")
ans=[35,36,40,44]
num=[1,2,3,4]
for i in range(len(ans)):
    print(num[i],ans[i],sep=". ")
yourchoice=int(input('Your choice? '))
if not yourchoice==4:
    print(":(")
    
else:
    print("Bingo")

ans2=[49,81,72,66,52]
num2=[1,2,3,4,5]
print("Estimate this answer (exact calculation not needed):")
print("Jack scored these marks in 5 math tests: 49, 81, 72, 66, 52. What is the mean?")
for i in range(len(ans2)):
    print(num2[i],ans2[i],sep=". ")
yourchoice2=int(input('Your choice? '))
if not yourchoice2==2:
    print(":(")
else:
    print("Bingo")

if yourchoice==4 and yourchoice2==2:
    print("You correctly answer 2 out of 2 questions")
elif yourchoice==4 and not yourchoice2==2:
    print("You correctly answer 1 out of 2 questions")
elif not yourchoice==4 and yourchoice2==2:
    print("You correctly answer 1 out of 2 questions")
else:
    print("You correctly answer 0 out of 2 questions")