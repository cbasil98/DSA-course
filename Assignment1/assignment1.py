class Names(list):
    def add(self):
        while 1:
            n=input('Enter the number of entries:')
            if n.isnumeric()==False:
                print("Invalid Entry")
                continue
            break
        n=int(n)
        for i in range(n):
            name=input('Enter the name:')
            number=input('Enter the number:')
            if number.isnumeric()==True:
                names.append([name,number])
            else:
                print("Invalid number")
    def removeit(self,name):
        flag=0
        print(self[0][0])
        for i in range(len(self)):
            if name==self[i][0]:
                names.remove(self[i])
                print("Item removed")
                flag=1
                break
        if flag==0:
            print("Not found")
    def printall(self):
        if len(names)==0:
            print("No entry to print")
        for i in range(len(names)):
            print(i+1,'.',names[i][0],':',names[i][1])
    def search(self,name):
        for i in range(len(self)):
            if name == self[i][0]:
                return i
        return -1
    def searchprint(self,name):
        i=self.search(name)
        if i==-1:
            print("Item not found")
        else:
            print("Saved as", i + 1, "th entry")
            print("Number:", names[i][1])
    def update(self,name,number):
        i=self.search(name)
        if i==-1:
            print("Invalid entry")
        else:
            self[i][1]=number

names=Names()
while 1:
    print("Select an option")
    print("1.Insert")
    print('2.Remove')
    print('3.Print all')
    print('4.Sort')
    print('5.Search')
    print("6.Remove all")
    print("7.Update number")
    print("8.Exit")
    x=input()
    if x.isnumeric()==False:
        print("Invalid entry")
        continue
    x=int(x)

    if x==1:
        names.add()
    elif x==2:
        name=input('Enter the name to remove:')
        names.removeit(name)
    elif x==3:
        names.printall()
    elif x==4:
        names.sort()
        print("List sorted")
    elif x==5:
        name=input("Enter the name to search:")
        names.searchprint(name)
    elif x==6:
        del names[:]
        print("All data is deleted")
    elif x==7:
        name=input("Enter the name:")
        number=input("Enter new number:")
        if number.isnumeric()==False:
            print("Invalid number")
        names.update(name,number)
    elif x==8:
        break
    else:
        print('Invalid entry')
    a=input('Press \'y\' to continue')
    a.lower()
    if a!='y':
        break
print("Program terminated")