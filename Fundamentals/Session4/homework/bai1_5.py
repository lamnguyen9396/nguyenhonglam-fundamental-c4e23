size=[5,10,11,48,65,99,16]
for i in range(3):
    print("Month",i+1,sep=" ")
    print("Hello, my name is Lam and these are my sheeps' sizes",size,sep="\n")

    print("Now my biggest sheep has size",max(size),"let's shear it",sep=" ")

    a=size.index(max(size))
    size[a]=8
    print("After sheering, here is my flock",size,sep="\n")

    for i in range(len(size)):
        size[i]=size[i]+50
        print("One month has passed, now here is my flock",size,sep="\n")
        print()
