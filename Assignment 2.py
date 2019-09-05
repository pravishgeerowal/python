""" Write a Python program that will accept four lists of four values. Then your program
should find the list whose sum of elements is the highest and display the list."""

lista = []
listb = []
listc = []
listd = []

print("please enter numbers of all the lists")
num1 = int(input("first num. lista:"))
num2 = int(input("second num. lista:"))
num3 = int(input("third num.lista:"))
num4 = int(input("fourth num. lista:"))

lista.append(num1)
lista.append(num2)
lista.append(num3)
lista.append(num4)

num1 = int(input("first num.listb:"))
num2 = int(input("second num. listb"))
num3 = int(input("third num. listb"))
num4 = int(input("fourth num. listb"))

listb.append(num1)
listb.append(num2)
listb.append(num3)
listb.append(num4)

num1 = int(input("first num.listc:"))
num2 = int(input("second num. listc"))
num3 = int(input("third num. listc"))
num4 = int(input("fourth num. listc"))

listc.append(num1)
listc.append(num2)
listc.append(num3)
listc.append(num4)


num1 = int(input("first num.listd:"))
num2 = int(input("second num. listd"))
num3 = int(input("third num. listd"))
num4 = int(input("fourth num. listd"))

listd.append(num1)
listd.append(num2)
listd.append(num3)
listd.append(num4)

print ("list 1 is:" ,lista)
print ("list 2 is:",listb)
print ("list 3 is:" ,listc)
print ("list 4 is :",listd)

sum1 = 0
for num1 in lista:
    sum1 += int(num1)

sum2 = 0
for num2 in listb:
    sum2 += int(num2)

sum3 = 0
for num3 in listc:
    sum3 += int(num3)

sum4 = 0
for num4 in listd:
    sum4 += int(num4)

if (sum1 > sum2) and (sum1 > sum3) and (sum1 > sum4):
    largest = sum1
    print("The list with highest sum of elements is:",lista )

elif (sum2 > sum1) and (sum2 > sum3) and (sum2 > sum4):
    largest = sum2
    print("The list with highest sum of elements is:",listb )

elif (sum3 > sum1) and (sum3 > sum2) and (sum3 > sum4):
    largest = sum3
    print("The list with highest sum of elements is:",listc )

else:
    largest = sum4
    print("highest value of list is :",listd)



