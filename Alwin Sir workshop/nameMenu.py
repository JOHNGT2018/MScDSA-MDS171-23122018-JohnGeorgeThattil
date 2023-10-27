nameList = []

def storeName():  # to store name in list
    name = input("Enter the name to be saved :")
    name = name.strip().title()
    nameList.append(name)
    return name

def listNames():   #to list names entered in the list
    print("*"*30)
    print("Names in the list")
    print("*"*30)
    for name in nameList:
        print(name)
    print("*"*30)    

def searchName(search):   # search the names in list
    search = search.strip().title()  # first letter capital
    
    found = False  # using this while checking name in the  list & if its not in the list
    for name in nameList:
        if name == search:
            found = True
            break
    if found == True:    
            print("name exist in the list") 
    else:
        print("name does no exist...!")           

print("*"*30)
print("Name management system")
print("*"*30)
while True:
    print("*"*30)
    print("1. Enter a name")
    print("2. List the names")
    print("3. Search for a name")
    print("4. Exit")
    print("*"*30)

    choice = input ("Enter your choice ?")    # the choice part
    print("you have entered choice :",choice)

    if int(choice) == 1:
        name = storeName()
        print("Name {} added succesfully!". format(name))
    elif int(choice) == 2:
        listNames()
    elif int(choice) == 3:
        name = input("Enter a name to be searched")
        searchName(name)
    elif int(choice) == 4:
        exit()
    else:
        print("Invalid option....!")             