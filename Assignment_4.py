""" . Write a Python program that will find the L.C.M. of two input number."""

def lcm(num1,num2):
    if num1 > num2:
        a = num2
    else:
        a = num2

        while (1):
            if (a % num1 == 0) and ( a % num2 == 0):
                break
                a += 1
                return a

            print("lcm of both numbers is :",lcm(num1,num2))




















