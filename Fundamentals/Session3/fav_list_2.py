items=["ghe","so huyet","chao"]
print("hi there, here are your favourite things so far")
print(*items,sep="\n")

number=int(input("Name one number you want to get rid"))
items.pop(number-1)
print(*items,sep="\n")