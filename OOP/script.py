command = input("Enter your command")

class  Dog:
    def bark(self):
        print("Welcome to the Dog!")
    def sit(self):
        print("dog is sitting!")
dog1 = Dog() #creating instance of dog


if command == "sit":
    dog1.sit()
if command == "bark":
    dog1.bark()

