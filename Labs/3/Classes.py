# # Exercise 1
# def getString():
#     a = input()

# def printString(a:str):
#     print(a.upper())

# # Exercise 2

class Shape:
    def __init__(self) -> None:
        pass
    def area(self):
        return 0
    
somhsdihg = Shape()
# class Sqare(Shape):
#     def __init__(self,length) -> None:
#         super().__init__()
#         self.l = length
#     def area(self):
#         return self.l * self.l
# p = Sqare(int(input()))
# print(p.area())

# # Exercise 3

# class Rectangle(Shape):
#     def __init__(self, length, width) -> None:
#         super().__init__()
#         self.l = length
#         self.w = width

#     def area(self):
#         return self.l * self.w

# x = int(input())
# y = int(input())
# p = Rectangle(x, y)
# print(p.area())

# # Exercise 4
# import math
# class Point():
#     def __init__(self) -> None:
#         self.x = 0
#         self.y = 0

#     def __init__(self, x, y) -> None:
#         self.x = x
#         self.y = y
    
#     def show(self):
#         print(self.x, self.y)
    
#     def move(self, dx, dy):
#         self.x += dx
#         self.y += dy

#     def dist(self, x, y):
#         dx = self.x - x
#         dy = self.y - y
#         print(math.sqrt(dx**2 + dy**2))

# a = int(input())
# b = int(input())

# pt = Point(a, b)

# pt.show()
# pt.move(int(input()), int(input()))
# pt.show()
# pt.dist(int(input()), int(input()))

# # Exercise 5

# class Account:
#     def __init__(self) -> None:
#         self.owner = "Not setted Yet."
#         self.balance = 0

#     def __init__(self, owner, balance) -> None:
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         if self.balance >= amount :
#             self.deposit = amount
    
#     def withdraw(self, amount):
#         if self.balance > amount:
#             print("Here are you're withdraw")
#             self.balance -= amount
#         else:
#             print(f"Ooops, there is no enough money in your balance. You can report a withdraw less than {self.balance}.")

# p1 = Account("Kakimbek", 20000)

# print(p1.balance)
# p1.deposit(int(input()))
# print(p1.balance)
# p1.withdraw(int(input()))
# print(p1.balance)

# Exercise 6
