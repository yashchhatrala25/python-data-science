# Greatest of 3 Numbers using if else statement
# a=7; b=5; c=13
# if a>b:
#     if a>c:
#         print("a is greater")
#     else:
#         print("c is greater")
# else:
#     if b>c:
#         print("b is greatest")
#     else:
#         print("c is greatest")

opearnd1 = float(input("Enter the first number : "))
opearnd2 = float(input("Enter the second number : "))
user_choice = input("Enter the choice : (A)dd,(S)ubtract,(M)ultiply,(D)ivide : ").upper()
if user_choice == 'A':
    print("Sum of {} and {} = {}".format(opearnd1, opearnd2, opearnd1+opearnd2))
else:
    if user_choice == 'S':
        print("Difference of {} and {} = {}".format(opearnd1, opearnd2, opearnd1-opearnd2))
    else: 
        if user_choice == 'M':
            print("Product of {} and {} = {}".format(opearnd1, opearnd2, opearnd1*opearnd2))
        else:
            if user_choice == 'D':
                print("Divide of {} and {} = {}".format(opearnd1, opearnd2, opearnd1/opearnd2))
            else:
                print("Choose the right choice")
print("Operation Completed!")


# a = 10
# if a < 80:
#     print("0 to 80")
# if a >= 80:
#     print("Above 80")
# else:
#     print("Below 80")
# a. 0 to 80
#    Below 80
# b. 0 to 80
# c. Below 80
# d. Error


# What will be the output?
# x=4
# if x>1 or x<5 and x==3:
#     print("Right")
# else:
#     print("Wrong")
# a. Right
# b. Wrong
# c. No output
# d. Error