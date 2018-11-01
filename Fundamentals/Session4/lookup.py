tienganh={
    "dog":"cho",
    "cat":"meo",
    "snake":"ran",
    "tiger":"ho",

}
while True:
    yourcode=input("your code? ")
    if yourcode in tienganh:
        print(tienganh[yourcode])
    else:
        print("your code does not exist")
        y_n=input("Do you want to contribute? (Y/N)? ")
        if y_n=="y":
            newvalue=input("New value? ")
            tienganh[yourcode]=newvalue
        elif y_n=="n":
            print("ok")
        else:
            y_n=input("Do you want to contribute? (Y/N)? ")
        print(tienganh)
