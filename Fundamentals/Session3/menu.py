# item1="pho"
# item2="ghe"
# item3="so huyet"
# item4="chao"
# item5="com rang"

# items=[] #empty list
# print(items)
# print(type(items))

# items=["ghe"]
# print(items)

items=["ghe","so huyet","chao"]
# print(items[-1])
# items[0]="ghe to"
# print(items)

# items.pop(1)
# print(items)

# items.remove("so huyet")
# print(items)

i=int(input("Index:"))
new_value=input("New value:")
items[i]=new_value
print(items)