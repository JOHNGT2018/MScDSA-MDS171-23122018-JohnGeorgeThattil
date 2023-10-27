class john:
    def __init__(self):
        self.dic1 = {}
        

    def createDic(self,Name,PhoneNo,CustComplaint,Status):
        temp = {
            "name":Name,
            "phoneno":PhoneNo,
            "custmcompl":CustComplaint,
            "stats":Status
              }    
        self.dic1[Name]= temp
        print(self.dic1)

    def search(self,searchName):
        for key in self.dic1.keys():
            flag = True
            if key == searchName:
                print(self.dic1[key])
                break
            else:
                flag = False
        if flag == False:
            print("invalid")

    def statsupdtae(self):
        name = input("Enter the name:")
        update = input ("enter the status")
        self.dic1[name]["stats"]=update
        print(self.dic1)

# Name = input("Enter the name:")
# PhoneNo = int(input("Enter the phoneno:"))
# CustComplaint = input("Enter the complaint:")
# Status = "Not Resolved"
# searchName = input("Enter the name to search :")

ard = john()
# ard.createDic(Name,PhoneNo,CustComplaint,Status)
# ard.search(searchName)
# ard.statsupdtae()


while True:
    choice = int(input("enter ur choice"))
    if choice == 1:
        Name = input("Enter the name:")
        PhoneNo = int(input("Enter the phoneno:"))
        CustComplaint = input("Enter the complaint:")
        Status = "Not Resolved"
        ard.createDic(Name,PhoneNo,CustComplaint,Status)
    elif choice == 2:
        searchName = input("Enter the name to search :")
        ard.search(searchName)
    elif choice == 3:
        ard.statsupdtae()
    elif choice == 4:
        exit()
    else:
        print("invalid choice")    






    # def search(self,searchName):
    #     for key in self.dic1.keys():
    #         flag = True
    #         if key == searchName:
    #             print(self.dic1[key])
    #             break
    #         else:
    #             flag = False
    #     if flag == False:
    #         print("invalid")    


        