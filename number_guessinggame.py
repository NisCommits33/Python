correct_number = "3"
wrong_answer_message = "Wrong answer"
correct_answer_message = "Correct answer"
numbers =(1,2,3)
chances =  f"You have {numbers} chances to guess the number! "
choose_message = f"Choose a number from 1 - 5: "

print(chances)
guessed_number = int(input(choose_message))
if 1 <= int(guessed_number) <= 5:
    if guessed_number == correct_number:
        print(correct_answer_message)
    else:
        print(wrong_answer_message)
        print(chances)
        guessed_number = input(choose_message)
        if 1 <= int(guessed_number) <= 5:
            if guessed_number == correct_number:
                print(correct_answer_message)
            else:
                print(wrong_answer_message)
                print(chances)
                guessed_number = input(choose_message)
                if 1 <= int(guessed_number) <= 5:
                    if guessed_number == correct_number:
                        print(correct_answer_message)
                else:
                    print(choose_message)
        else:
            print(choose_message)
else:
    print(choose_message + " Try Again")
