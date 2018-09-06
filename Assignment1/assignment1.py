names=list()
a='y'
while a=='y':
    x=int(input('Select an option:\n1. Insert\n2. Remove\n3. Print all\n4.Remove all\n'))
    if x==1:
        name=input('Enter the name')
        names.append(name)
    elif x==2:
        name=input('Enter the name to remove')
        names.remove(name)
    elif x==3:
        print(names)
    elif x==4:
        del names[:]
    else:
        print('Invalid entry')
    a=input('Do you want to continue?(y/press any other key)')

