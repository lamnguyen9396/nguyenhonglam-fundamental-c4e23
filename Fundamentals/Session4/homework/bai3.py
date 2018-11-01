price={
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
stock={
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
total=0
for i in price.keys():
    print(i)
    print("price:",price[i])
    print("stock:",stock[i])
    print()
    total=price[i]*stock[i]+total
print(total)
