def enter(no):
    if no%2!=0:
        return ("weird")
    else:
        if (no>=2) and (no<=5):
            return ("not weird")
        elif (no>=6)and (no<=20):
            return ("weird")
        elif no>20:
            return ("not weird")
print (enter(int(input("enter"))))
