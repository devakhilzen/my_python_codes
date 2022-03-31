import csv
def write():
    a=open('brave.csv','w',newline='')
    x=csv.writer(a)
    x.writerow(['name','rollno','fav no'])
    while True:
        b=input('enter name')
        c=int(input('enter roll no'))
        d=int(input('enter fav no'))
        lst=[b,c,d]
        y=input('more y/n')
        if y in 'n':
            break
                
    x.writerow(lst)
    a.close()
write()
