import random

def guess(num):

    random_number  = random.randint(1,num)
    
    get = 0

    while get != random_number:

        get = int(input(f"\nGuess number between 1 to {num} = "))

        if get > random_number:
            print("Number is too high!")
        elif get < random_number:
            print("Number is too low!")    

    print(f"\ncongratulations! You guess the correct number {random_number}\n")



guess(10)   