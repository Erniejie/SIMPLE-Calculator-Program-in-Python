# SIMPLE Calculator Program in Python
#Computer Programming Tutor- Feb 01 2022


# Function to add two Numbers
def add(no1,no2):
    return no1 + no2
# Function to subtract two Numbers
def subtract(no1,no2):
    return no1 - no2

# Function to multiply wo Numbers
def multiply(no1,no2):
    return no1*no2
# Function to divide two Numbers
def divide(no1,no2):
    return no1/no2

print("Please Enter Option Operation  -\n" \
      "1.Add\n" \
      "2.Subtract\n" \
      "3.Multiply\n" \
      "4.Divide\n"
      )

#Take Input from the User:

option = int(input("Option Operation Form 1,2,3,4:"))
n1= int(input("Enter First Number: "))
n2= int(input("Enter Second Number: "))

if option == 1:
        print(n1,"+",n2,"=",
                               add(n1,n2))


elif option == 2:
        print(n1,"-",n2,"=",
                               subtract(n1,n2))

elif option == 3:
        print(n1,"*",n2,"=",
                               multiply(n1,n2))

elif option == 4:
        print(n1,"/",n2,"=",
                               divide(n1,n2))

else:
    print("Invalid Input")









