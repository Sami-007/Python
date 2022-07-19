import random

def guess(num):
    
    num1 = 1
    num2 = num

    feed_back = ''

    while feed_back !='c':

        guess = random.randint(num1,num2)
        feed_back = input(f"\n Is {guess} too high 'h' to low 'l' or correct 'c'  = ")

        if feed_back == 'h':
            num2 = guess -1;
        elif feed_back == 'l':
            num1 = guess+1      

        if num1 == num2:
            guess = num1
            break
        
         
    print(f"\nThe computer guessed your number {guess}\n")




guess(100)