correct_number = "3"
print("You have 3 chances to guess the number!")
guessed_number = input("Choose a number from 1 - 5: ")
if guessed_number == correct_number:
    print('correct answer')
else:
    print("Wrong answer")
    guessed_number = input("Choose a number from 1 - 5: ")
    if guessed_number == correct_number:
        print('Correct answer')
    else:
        print("Wrong answer")
        guessed_number = input("Choose a number from 1 - 5: ")
        if guessed_number == correct_number:
            print('Correct answer')