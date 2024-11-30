# Input
# -----------------------------------
# print("Enter a Number: ")
# val = input()
# print("Input : ", val, " Type : ", type(val))


# Processing
# Operators
# Decision making statements
# Loops
# ------------------------------------
# Find greatest of two numbers
# ------------------------------------
# val1 = float(input("Enter a number : "))
# val2 = float(input("Enter a number : "))

# if val1 > val2:
#     print(val1, " is greater")
# else:
#     print(val2, " is greater")


# print()
# -------------------------------------
# value:converted to string
# Default:
#   Separator: blank space
#   End Symbol: Newline
#   Output: Standard output
# Does not forcibly flush stream and is buffered
# -------------------------------------
# String Datatype in print()
# -------------------------------------
# Verbatim
# Value in object
# String Expression
# -------------------------------------
# Syntax
# print(value,...,sep='',end='\n',file=sys,stdout,flush=False)
# -------------------------------------
# print("Verbatim")

# val = "Value in String Object"
# print(val)

# print("Input is \""+val+"\" and the string are concatenated")

# -------------------------------------
# Other Datatype in print()
# -------------------------------------
# Type cast : String
# -------------------------------------
# print("There are "+24+" hours in a day")
# print("There are "+24+" hours in a day")
# TypeError: can only concatenate str (not "int") to str

# print("There are "+str(24)+" hours in a day")

# -------------------------------------
# sep in print()
# -------------------------------------
# print("c:","users","python",sep="/")
# print("c:","users","python",sep="\n")
# print("Multi","Line",sep="")

# -------------------------------------
# end in print()
# -------------------------------------
# print("Checking Dependencies...",end="")
# # Perform other process
# print("ok")

# -------------------------------------
# file in print()
# -------------------------------------
# source_file = open("d:\\newFile.txt", "w")
# print("Writing to a file", file=source_file)
# source_file.close()

# -------------------------------------
# Positional Formatting
# -------------------------------------
# a=3; b=4
# print("Sum of %d and %d is %d"%(a,b,a+b))

# -------------------------------------
# format()
# -------------------------------------
# a=3; b=4
# print("Sum of {} and {} is {}".format(a,b,a+b))

# -------------------------------------
# format() with Positional Index
# -------------------------------------
# a=3;b=4
# print("Sum of {1} and {0} is {2}".format(a,b,a+b))

# -------------------------------------
# format() with Keyword Arguments
# -------------------------------------
a = 3
b = 4
print("Sum of {a} and {b} is {sum}".format(a=a,b=b,sum=a+b))



# Quiz
# What datatype does input return by default?
# a. 'int
# b. float
# c. string
# d. 'boolean

# Which among the following results in IndexError?
# a. print("{} + {} = {}".format(3,2,3+2))
# b. print("{} + {} = ".format(3,2,3+2))
# c. print("{} + {} = ".format(3))
# d. print(" + {} = ".format(3))