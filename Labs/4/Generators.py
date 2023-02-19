#Exercise 1 - Create a generator that generates the squares of numbers up to some number N.
# n = int(input())
# g = (x**2 for x in range(n+1))
# for i in range(n+1):
#     print(next(g))

# Exercise 2 -Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.

# n = int(input())
# a = (i for i in range(0, n, 2))
# for i in a:
#     print(i, end=",")

# Exercise 3 - Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.

# n = int(input())
# def a(n):
#     for i in range(n):
#         if i%3==0 and i%4==0:
#             yield i

# b = a(n)

# for x in b:
#     print(x)

# Exercise 4 - Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
# a = int(input())
# b = int(input())
# squares = (x**2 for x in range(a,b))
# for x in squares:
#     print(x)

# Exercise 5 - Implement a generator that returns all numbers from (n) down to 0.
# n = int(input())

# a = (x for x in range(n)[::-1])

# for i in a:
#     print(i)