p1={
    'stt':1,
    'name':'Huy',
    'Hours':30,
    'VND per hour':50,
}
p2={
    'stt':1,
    'name':'Quan',
    'Hours':20,
    'VND per hour':50,
}
p3={
    'stt':3,
    'name':'Duc',
    'Hours':15,
    'VND per hour':35,
}

p_list=[p1,p2,p3]
total = 0
for i in p_list:
    salary=i['Hours']*i['VND per hour']
    total= total + salary
print(total)