command = input("Enter your command")

class  Dog:
    def __init__(self,name,breed,owner):
        self.name = name
        self.breed = breed
        self.owner = owner
    def bark(self):
        print(dog1.name + " is barking")
    def sit(self):
        print(dog1.name + " is sitting")
    def introduce(self):
        print("Welcome to the dog world" + "I am " + dog2.name + " I am a " + dog2.breed)
class owner:
    def __init__(self,name,address,number):
        self.name = name
        self.address = address
        self.number = number

owner1 = owner("nischal" , "jarankhu", " 123123")
dog1 = Dog("ani","German",owner1) #creating instance of dog

owner2 = owner("anis" , "nalaju", "141414")
dog2 = Dog("nis","nep", owner2)


if command == "sit":
    dog1.sit()
    print("owner details: "  +   dog1.owner.name )


if command == "bark":
    dog1.bark()
elif command == "intro":
    dog2.introduce()

