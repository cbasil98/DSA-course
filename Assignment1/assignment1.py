names=list()
a='y'
while a=='y':
    print("Select an option")
    print("1.Insert")
    print('2.Remove')
    print('3.Print all')
    print('4.Sort')
    print('5.Remove all')
    x=int(input())
    if x==1:
        n=int(input('Enter the number of entries:'))
        for i in range(n):
            name=input('Enter the name:')
            names.append(name)
    elif x==2:
        name=input('Enter the name to remove:')
        names.remove(name)
    elif x==3:
        for i in range(len(names)):
            print(i+1,'.',names[i])
    elif x==4:
        names.sort()
    elif x==5:
        del names[:]
    else:
        print('Invalid entry')
    a=input('Do you want to continue?(y/press any other key)')

