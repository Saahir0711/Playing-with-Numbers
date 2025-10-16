largest_number = int(input("Enter largest number: "))
smallest_number = int(input("Enter smallest number: "))

for loop in range (1, largest_number * smallest_number):
    LCM = largest_number * loop
    if LCM % smallest_number == 0:
        break

print ("LCM is: ", LCM)