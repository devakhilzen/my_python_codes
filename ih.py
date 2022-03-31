weight=int(input("enter weight"))
unit=input("kg(k) or lb(L)")
if (unit in "k" or "K"):
    print( weight*2.2,"weight in pounds")
elif (unit in "l"or "L"):
    print (weight/2.2)
    
