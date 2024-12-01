# a=7; b=5; c=13

# if a>b and a>c:
#     print("a is greatest")
# if b>c and b>a:
#     print("b is greatest")
# if c>b and c>a:
#     print("c is greatest")


# Arithmetic Operations
opearnd1 = float(input("Enter the first number : "))
opearnd2 = float(input("Enter the second number : "))
user_choice = input("Enter the choice : (A)dd,(S)ubtract,(M)ultiply,(D)ivide : ").upper()
if user_choice == 'A':
    print("Sum of {} and {} = {}".format(opearnd1, opearnd2, opearnd1+opearnd2))
if user_choice == 'S':
    print("Difference of {} and {} = {}".format(opearnd1, opearnd2, opearnd1-opearnd2))
if user_choice == 'M':
    print("Product of {} and {} = {}".format(opearnd1, opearnd2, opearnd1*opearnd2))
if user_choice == 'D':
    print("Division of {} and {} = {}".format(opearnd1, opearnd2, opearnd1/opearnd2))
if user_choice != 'A' and user_choice != 'S' and user_choice != 'M' and user_choice != 'D':
    user_choice = input("Please enter valid choice : (A)dd,(S)ubtract,(M)ultiply,(D)ivide : ").upper()

print("Opeartion Completed")



# a = 10
# if a < 80:print("0 to 80")
# a. 0 to 80 is printed
# b. No output
# c. Syntax Error
# d. Runtime Error


# What does the following code print?
# if True:
#     print(1)
# else:
#     print(2)
# a. 1
# b. 2
# c. TRUE
# d. FALSE