import random

# def guess(x):
#     random_number= random.randint(1, x)
#     guess = 0
#     while guess != random_number:
#         guess = int (input(f"Guess a number between 1 and {x}:"))
#         if guess < random_number:
#             print ('sorry, guess again. Too low')
#         elif guess > random_number:
#             print ("sorry, guess again. Too Hight") 
            
#     print (f'Yaa,congratulation , you have the guess the number {random_number} correctly')    
    
def guess(x):
    low = 1
    High = x
    feedback = ''
    while feedback != "c":
        if low != High:
            guess = random.randint(low, High)
        else:
            guess = low 
        feedback = input(f"Is {guess} too high, too low (L), or correct (c)??").lower()
        if feedback == "h":
            High = guess - 1
        elif feedback == '1':
            low = guess + 1
            
    print(f'Yay! The computer guessed your number, {guess}, correctly')

guess(10)
            
    

        
