""" Write a simple program that will prompt user to input a sentence. Your program
will count all lower case alphabets, upper case alphabets, digits, and special
symbols. Then your program will display the all the counts on screen. """


lower_case=0
upper_case=0
digit=0
specialChar=0

x = input(" Please Enter a sentence :")

for a in x:
    if a.islower():
        lower_case+=1

    elif a.isupper():
        upper_case+=1

    elif a.isdigit():
        digit+=1
    else:
        specialChar+=1
print("lower case:", lower_case)
print("upper case:", upper_case)
print("digit:", digit)
print("special character:", specialChar)













