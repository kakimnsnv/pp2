import random, cProfile, pstats 
def Guess_the_number():
    cnt = 0
    print("Hello! What is your name?")
    name = input()
    print()
    print("Well, KBTU, I am thinking of a number between 1 and 20.")
    num = random.randint(1,20)
    guess = int(21)
    while guess != num :
        print("Take a guess.")
        guess = int(input())
        msg = "Your guess is too low." if guess < num else "Your guess is too high."
        print(msg)
        cnt += 1
    print(f"Good job, {name}! You guessed my number in {cnt} guesses!")


Guess_the_number()