import pickle
def write():
    a=open('file.dat','wb')
    while True:
        name=input('enter name')
        mark=int(input('enter mark'))
        lst=[name,mark]
        ask=input('want to enter more y/n')
        if ask in'n':
            break
    pickle.dump(lst,a)
    a.close()
def read ():
        a=open('file.dat','rb')
        try:
            arc=pickle.load(a)
            for i in arc:
                print(i)
        except EOFError:
            a.close()
#write()
read()            
