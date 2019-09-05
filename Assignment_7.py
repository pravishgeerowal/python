""" Write a Python program for the stock of a pharmacy, with menu 1. Add an item to
stock pharmacy, 2. Remove item from stock, 3. Insert item at specified position.
Your program should do all the operations. Hint: use list."""


lipharm = ['medcines','bandages','antiseptics','antibiotics','ointments','injections']
print("Example of a pharmacy stock list:",lipharm)
print("")

print("Operations you may perform to pharmacy stock list:")
print("1. Add an item to stock pharmacy")
print("2. Remove item from stock")
print("3. Insert item at specified position")
print("__________________________________________")

choice = int(input("Please enter choice as 1,2,3 only: "))


if choice == 1:
       add = input("Enter the item you wish to add: ")
       lipharm.append(add)
       print(lipharm)

elif choice == 2:
    remove=input("Enter the item you wish to remove: ")
    lipharm.remove(remove)
    print(lipharm)

elif choice == 3:
    position= int(input("Enter list position of the item you wish to add: "))
    itemadd= str(input("Enter item you wish to add: "))



    lipharm.insert(position,itemadd)
    print(lipharm)

else: print("Invalid choice!!!!!")




