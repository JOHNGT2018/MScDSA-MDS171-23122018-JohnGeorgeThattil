#create a petstore class where you hav the details of pets available and thier details. 
#the class will have methods
#store a new pet detailss
# search for a pet
#sell a pet
#list all pets 

# importing your petstore class , create a petstoremain file, where you will implement a menu driven program
# for Admin - who will manage the stotre & User who will see the pets and buy pets 

class pets:
    def __init__(self):
        self.pets = []

    def additem(self,breed,age):
        self.breed = breed
        self.age = age
        print(self.breed,self.age)

    def search(self,breed):
        n = input("Enter the breed")
        if breed ==n:
            print("Found")
        else:    