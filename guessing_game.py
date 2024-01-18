import random as r
def guess_game():
    user_input=int(input("enter a number(1-5):"))
    print("user_value is:",user_input)
    ran_num=r.randint(1,5)
    print("system value is :",ran_num)

    while user_input!=ran_num:
        print("your guess wrong.try again")
        user_input = int(input("enter a number(1-5):"))
        if user_input>ran_num:
            print("your guess greater than system value!")
        elif user_input<ran_num:
            print("your guess lesser than system value!")
        else:
            print("congrats! your Guess correct.")

    return 'Sanjay'
result=guess_game()
print(result)
