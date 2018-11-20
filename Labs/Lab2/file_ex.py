
content='''
Tieu de,
Noi dung
'''

with open("content.txt","r") as f:
    c=f.read()
    print(c)



# content="Van ban rat quy"
# #2 cách:
# #Cách 1:
# with open("content.txt","w") as f:
#     f.write(content)

# # #Cách 2:
# #1. Open file
# f=open("content.txt","w") # w là viết tắt của write
# #2. Write file
# f.write(content)
# #3. Close file
# f.close()
