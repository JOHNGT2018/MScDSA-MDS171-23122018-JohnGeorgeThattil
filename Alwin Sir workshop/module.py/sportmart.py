#Create a sportMart class , where you will have
#-> INVENTORY/ shelf of items
#-> Orders of customers 

#create csv file which will store your inventory details and order details 

#with the help of file handling techniques in python, read the file and 
#create an object for trinity store and populate the inventory items and orders into the trinity StopIteration

#To make sure that you have added all the items in your life, use a display method to show your inventory and order history 

class sportMart:
    def __init__(self):
        self.inventory = {}
        self.orders = {}
    
    def createInventory(self, productID,ProductName,Qunatity,Price):
        temp = {
            "productid":productID,
            "productname":ProductName,
            "quantity":Qunatity,
            "price": Price
        }   
        self.inventory[productID] = temp

    def createOrder(self,Orderid,ProductID,Quantity,Price,Total):
        temp = {
            "orderid":Orderid,
            "productid":ProductID,
            "quantity":Quantity,
            "price":Price,
            "total":Total
              }  
        self.orders[Orderid]= temp

    def printOrders(self):
        print(self.orders)

    def printInventory(self):
        print(self.inventory)


trinity = sportMart()
#filename = "orders.csv"
orders = open("orders.csv","r")
o_header = orders.readline()
o_data =orders.readlines()
for data in o_data:
    tmp = data.strip().split(',')
    trinity.createOrder(tmp[0],tmp[1],tmp[2],tmp[3])

trinity.printOrders()   

trinity = sportMart()
inventory = open("inventory.csv","r")
i_header = inventory.readline()
i_data =inventory.readlines()
for data in i_data:
    tmp = data.strip().split(',')
    trinity.createInventory(tmp[0],tmp[1],tmp[2],tmp[3])

trinity.printInventory()  