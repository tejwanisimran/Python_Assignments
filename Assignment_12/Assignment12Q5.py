####################################################################
#
# Description : Write a program which accepts one number & prints
#               that many numbers in reverse order
# Input       : 5
# Output      : 5 4 3 2 1 
#
####################################################################

####################################################################
#
# FunctionName : Display()
# Description  : It is used to print number numbers in reverse
#                 order
# Author       : Simran Naveen Tejwani
# Date         : 19/01/2026
#
####################################################################

def Display(iNo):
    for iCnt in range(iNo , 0 , -1):
        print(iCnt)

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    iValue = 0

    print("Enter the number : ",end = "")
    iValue = int(input())

    Display(iValue)

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 