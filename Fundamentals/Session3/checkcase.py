s=input("enter a text: ")
if (not s.isdigit()) and (not s.islower()) and (not s.isupper()):
    print("contain both lowercase and uppercase")
else:
    print("NOT OK")