items=["ghe","so huyet"]
print("hi there, here are your favourite things so far")
print(*items,sep=", ")
new_item=(input("Name one thing you want to add?"))
items.append(new_item)
print(*items,sep=", ")