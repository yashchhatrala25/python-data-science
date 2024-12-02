opearnd1 = float(input("Enter the first number : "))
opearnd2 = float(input("Enter the second number : "))
user_choice = input("Enter the choice : (A)dd,(S)ubtract,(M)ultiply,(D)ivide : ").upper()
if user_choice == 'A':
    print("Sum of {} and {} = {}".format(opearnd1, opearnd2, opearnd1+opearnd2))
elif user_choice == 'S':
    print("Difference of {} and {} = {}".format(opearnd1, opearnd2, opearnd1-opearnd2))
elif user_choice == 'M': 
    print("Product of {} and {} = {}".format(opearnd1, opearnd2, opearnd1*opearnd2))
elif user_choice == 'D':
    print("Divide of {} and {} = {}".format(opearnd1, opearnd2, opearnd1/opearnd2))
else:
    print("Choose the right choice")
print("Operation Completed!")


# What will be the output? 
# a = b = -1
# if a <= 0:
#     b = b +1
# else:
#     a = a + 1
# if a > 0 and b > 0:
#     print ("A")
# elif a > 0:
#     print("B")
# if b > 0:
#     print("C")
# else:
#     print("D")
# a. A
# b. B
# c. C
# d. D


# a = 10
# if a < 80:
#     print("0 to 80")
# elif a >= 80:
#     print("Above 80")
# else:
#     print("Below 80")
# a. 0 to 80
#    Below 80
# b. 0 to 80
# c. Below 80
# d. Error