####################################################################
#
# Description : Write a program which accepts one number & prints
#               that many numbers starting from 1
# Input       : 5
# Output      : 1 2 3 4 5
#
####################################################################

####################################################################
#
# FunctionName : Display()
# Description  : It is used to print number till that number 
#                 starting from 1.
# Author       : Simran Naveen Tejwani
# Date         : 19/01/2026
#
####################################################################

def Display(iNo):
    for iCnt in range(1,iNo+1):
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