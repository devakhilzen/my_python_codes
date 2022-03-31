stack=[]
choice="y"
while choice =="y":
    print("1 push")
    print("2 pop")
    print("3 display")
    c=int(input("enter a no. between 1,2 and 3: "))
    if c==1:
        a=int(input("enter a no. which is to be pushed: "))
        stack.append(a)
    elif c==2:
        if stack==[]:
            print("underflow")
        else:
            print("deleted no is: ",stack.pop())
    elif c==3:
        for i in range(len(stack)-1,-1,-1):
            print(stack[i])
    else:
        print("wrong")
        choice=input("more")
        break
a=int(input("ener a no"))
print(a)
print(
    "ert"
    )
