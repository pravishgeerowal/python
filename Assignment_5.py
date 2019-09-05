""" Write a Python program that will find the H.C.F of two input number."""

num1 = int(input("please enter first number:"))
num2 = int(input("please enter second number:"))

def hcf(num1,num2):
    if num1 > num2:
        a = num2
    else:
        a = num1
    for i in range (1, a+1):
        if  (num1 % i == 0) and (num2 % i == 0):
             a = i


print("hcf of both numbers are:",hcf(num1,num2))






