import math
# 1 Write a Python program with builtin function to multiply all the numbers in a list
# list = [1,2,3,4,5,6,7,8,9,10,11]
# print(math.prod(list))

# 2 Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
def test2(text):
    u = 0
    l = 0
    for i in text:
        if i.isupper():
            u += 1
        elif i.islower():
            l += 1
    print(f"upper = {u}, lower = {l}")

# 3 Write a Python program with builtin function that checks whether a passed string is palindrome or not.
def test3(text):
    if text[::-1] == text:
        print("Yes")
    else: print("No")
# 4 Write a Python program that invoke square root function after specific milliseconds
def test4():
    num = int(input())
    time = int(input())
    res = math.sqrt(num)
    print(f"Square root of {num} after {time} miliseconds is {res}")

# 5 Write a Python program with builtin function that returns True if all elements of the tuple are true.
def test5(tuple):
    print(all(tuple))

# text = input()

# test1(text)
# test2(text)
# test3(text)
# test4()
# test5((True, True, True))
# test5((False, False, False))
# test5((True, False, False))
