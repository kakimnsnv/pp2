# Exercise 1

# def toOunces(grams:float):
#     return 28.3495231 * grams


# Exercise 2

# C = (5 / 9) * (F – 32)
# def toCelcium(fahrenheit:float):
#     return ((5/9) * (fahrenheit - 32))

# Exercise 3
# import math
# def solve(numheads, numlegs):
    # chikens = (numlegs - (4 * numheads)) / -2
    # rabits = numheads - chikens
    # return f"Rabits: {int(rabits)}\nChikens: {int(chikens)}"


# Exercise 4     WRONG!!!!!
# import math
# def filter_prime(list:list):
#     l = []
#     for i in list:
#         cnt = 0
#         if i ==2:
#             l.append(i)
#             continue
#         elif i == 1:
#             continue
#         for j in range(2, round(math.sqrt(i))):
#             if i%j == 0:
#                 cnt += 1
#         if cnt == 0:
#              l.append(i)
#     return l

# a = list(range(1, 1000))
# print(filter_prime(a))

# Exercise 5
# import itertools

# def permutations(string):
#   perms = [''.join(p) for p in itertools.permutations(string)]
#   print(*perms, sep=' ')
        
# # Exercise 6
# def reverseSentence(s):
#     s = s.split(" ")
#     l = list(s)
#     l.reverse()
#     for i in l:
#         print(i, end = ' ')

# # Exercise 7
# def has_33(nums):
#     for i in len(nums-1):
#         if nums[i] == 3 and nums[i+1] == 3:
#             return True
#     return False

# print(has_33([1,3,4]))
# print(has_33([1,3,3]))
# print(has_33([3,1,3]))

# Exercise 8


# Exercise 9
# def volume(r):
#     return (4/3) * 3.14 * r**3


# Exercise 10
# def unique(my_list):
#     d = {}
#     l = []
#     for i in my_list:
#         if(i not in d):
#             d[i] = 1
#         else:
#             d[i] += 1

#     for x, y in d.items():
#         if(y == 1):
#             l.append(x)
#     return l

# Exercise 11
# def palindrome(string):
#     s = string[::-1]
#     if(s == string):
#         return True
#     return False

# Exercise 12
# def histogram(my_list): 
#     for i in my_list:
#         for j in range(i):
#             print("*", end = "")
#         print()

# Exercise 13
# import random
# def Guess_the_number():
#     cnt = 0
#     print("Hello! What is your name?")
#     name = input()
#     print()
#     print("Well, KBTU, I am thinking of a number between 1 and 20.")
#     num = random.randint(1,20)
#     guess = int(21)
#     while guess != num :
#         print("Take a guess.")
#         guess = int(input())
#         msg = "Your guess is too low." if guess < num else "Your guess is too high."
#         print(msg)
#         cnt += 1
#     print(f"Good job, {name}! You guessed my number in {cnt} guesses!")

# Guess_the_number()

# Exercise 14
# import guess
# from pp2.Labs.3.guess import Guess_the_number()
