import os
names=list()
while 1:
    print("Select an option")
    print("1.Insert")
    print('2.Remove')
    print('3.Print all')
    print('4.Sort')
    print('5.Search')
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
        print("List sorted")
    elif x==5:
        name=input("Enter the number to search:")
        for i in range(len(names)):
            flag = 0
            if name==names[i]:
                print("Saved as ",i+1,"th entry")
                flag=1
                break
        if flag==0:
            print("Not found")
    elif x==6:
        del names[:]
    else:
        print('Invalid entry')
    a=input('Do you want to continue?(y/press any other key)')
    if a!='y':
        break;
    os.system('cls')


