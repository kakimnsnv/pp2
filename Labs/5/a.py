import re

text = input()

#Exercise 1 - Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s. 
def test1(text):
    pattern = "ab*"
    m = re.findall(pattern, text)
    print(m)
# WORKING 

#Exercise 2 - Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
def test2(text):
    pattern = "ab{2,3}"
    m = re.findall(pattern, text)
    print(m)
# WORKING

#Exercise 3 - Write a Python program to find sequences of lowercase letters joined with a underscore.
def test3(text):
    m = re.split("_", text)
    result = []
    for i in range(len(m) - 1):
        if m[i] != ' ' and m[i + 1] != ' ' and m[i].islower() and m[i + 1 ].islower():
            result.append(f"{m[i]}_{m[i+1]}")
    print(result)
#WORKING

#Exercise 4 - Write a Python program to find the sequences of one upper case letter followed by lower case letters.
def test4(text):
    pattern = "[A-Z][a-z]+"
    m = re.findall(pattern, text)
    print(m)
#WORKING

#Exercise 5 - Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
def test5(text):
    pattern = "a.+b$"
    m = re.findall(pattern, text)
    print(m)
#WORKING

#Exercise 6 - Write a Python program to replace all occurrences of space, comma, or dot with a colon.
def test6(text):
    m = re.sub("[,. ]", ":", text)
    print(m)
#WORKING

#Exercise 7 - Write a python program to convert snake case string to camel case string.
def test7(text):
    print(''.join(x.capitalize() or '_' for x in text.split('_')))
#WORKING

#Exercise 8 - Write a Python program to split a string at uppercase letters.
def test8(text):
    print(re.findall("[A-Z][^A-Z]*", text))
#WORKING


#Exercise 9 - Write a Python program to insert spaces between words starting with capital letters.
def test9(text):
    m = re.findall("[A-Z][a-z]*", text)
    print(' '.join(m))
#WORKING

#Exercise 10 - Write a Python program to convert a given camel case string to snake case.
def test10(text):
    print('_'.join(
        re.sub('([A-Z][a-z]+)', r' \1',
        re.sub('([A-Z]+)', r' \1',
        text.replace('-', ' '))).split()).lower())
#WORKING
    

# test2(text) #working
# test1(text) #working
# test3(text) #working
# test4(text) #working
# test5(text) #working
# test6(text) #working
# test7(text) #working
# test8(text) #working
# test9(text) #working
# test10(text) #working