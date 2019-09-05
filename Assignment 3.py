""" Write a Python program that will accept a number. If you reverse the given number
and it is the same as the original number then the program should return true"""

n =int(input("please enter a number:"))

def reverse(n):
    rev = 0

    while (n > 0):
        a = n % 10
        rev = rev * 10 + a
        n = n // 10

    return rev

x = reverse(n)

print("is a = reverse")

if n == x:
    print("true")
else:
    print("false")
