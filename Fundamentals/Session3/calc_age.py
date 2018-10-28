yob_str=input("year of birth?")
while not yob_str.isdigit():
    print("not ok")
    yob_str=input("year of birth?")
yob=int(yob_str)
age=2018-yob
print(age)