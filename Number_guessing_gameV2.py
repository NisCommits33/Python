Correct_Number = 5
isGuessed_Correct_Number = False
Incorrect_Message = "-----The Number You Guessed is incorrect-----"
Correct_Message = f"---------Your Guessed Number is Correct-------"
guess_chances = 3

for attempt in range(guess_chances):
    Guessed_Number = int(input("Enter your number: "))
    if 1 <= Guessed_Number <=10:
        if Guessed_Number == 5:
            print(Correct_Message)
            break
        else:
            print(Incorrect_Message)
            remaining = guess_chances - (attempt + 1)
            if remaining > 0:
                print(f"You have {remaining} remaining")
    else:
        #print(f"You have {remaining} remaining")
        print("Enter from 1-10")
    if attempt == guess_chances-1:
        print("You Lose")