names=list()
while 1:
    print("Select an option")
    print("1.Insert")
    print('2.Remove')
    print('3.Print all')
    print('4.Sort')
    print('5.Search')
    print("6.Remove all")
    print("7.Exit")
    x=input()
    if x.isnumeric()==False:
        print("Invalid entry")
        continue
    x=int(x)

    if x==1:
        while 1:
            n=input('Enter the number of entries:')
            if n.isnumeric()==False:
                print("Invalid Entry")
                continue
            break
        n=int(n)
        for i in range(n):
            name=input('Enter the name:')
            number=input('Enter the number')
            if number.isnumeric()==True:
                names.append([name,number])
        print("All entries are added")
    elif x==2:
        name=input('Enter the name to remove:')
        flag = 0
        for i in range(len(names)):
            if name==names[i][0]:
                names.remove(names[i])
                print("Item removed")
                flag=1
                break
        if flag==0:
            print("Not found")
    elif x==3:
        if len(names)==0:
            print("No entry to print")
            continue
        for i in range(len(names)):
            print(i+1,'.',names[i][0],':',names[i][1])
    elif x==4:
        names.sort()
        print("List sorted")
    elif x==5:
        name=input("Enter the number to search:")
        flag = 0
        for i in range(len(names)):
            if name==names[i][0]:
                print("Saved as",i+1,"th entry")
                print("Number:",names[i][1])
                flag=1
                break
        if flag==0:
            print("Not found")
    elif x==6:
        del names[:]
        print("All data is deleted")
    elif x==7:
        break
    else:
        print('Invalid entry')
    a=input('Press \'y\' to continue')
    a.lower()
    if a!='y':
        break
print("Program terminated")