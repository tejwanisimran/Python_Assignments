####################################################################
#
# Description : Write a program which accept one number and display 
#               below pattern
# Input       : 5
# Output      : * * * * * 
#               * * * * * 
#               * * * * * 
#               * * * * * 
#               * * * * * 
####################################################################

####################################################################
#
# FunctionName : Display
# Description  : It is used to display the above pattern
# Author       : Simran Naveen Tejwani
# Date         : 24/01/2026
#
####################################################################

def Display(iNo):

    for i in range(iNo):
        for j in range(iNo):
            print("*\t",end = "")
        print("\n")

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    iValue = 0

    print("Enter number :",end = "")
    iValue = int(input())

    Display(iValue)

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 