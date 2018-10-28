items=["T-Shirt","Sweater"]
crud=input("Welcome to our shop, what do you want (C, R, U, D)? ")
while (not crud=="C") and (not crud=="R") and (not crud=="U") and (not crud=="D"):
    print("Input only one letter which is C,R,U or D")
    crud=input("Welcome to our shop, what do you want (C, R, U, D)? ")
while crud=="R":
    print("Our items:",end=' ')
    print(*items,sep=", ")
    crud=input("Welcome to our shop, what do you want (C, R, U, D)? ")
while crud=="C":
    newitem=input("Enter new item: ")
    items.append(newitem)
    print("Our items:",end=' ')
    print(*items,sep=", ")
    crud=input("Welcome to our shop, what do you want (C, R, U, D)? ")
while crud=="U":
    i=int(input("Update position? "))
    updateitem=input("New item? ")
    items[i-1]=updateitem
    print("Our items:",end=' ')
    print(*items,sep=", ")
    crud=input("Welcome to our shop, what do you want (C, R, U, D)? ")    
while crud=="D":
    n=int(input("Deleted position? "))
    items.pop(n-1)
    print("Our items:",end=' ')
    print(*items,sep=", ")
    crud=input("Welcome to our shop, what do you want (C, R, U, D)? ")    
