####################################################################
#
# Description : Write a program which accepts one number & 
#               counts of digits in that number 
# Input       : 7521
# Output      : 4
#
####################################################################

####################################################################
#
# FunctionName : CountDigits()
# Description  : It is used to count number of digits in a given 
#                number
# Author       : Simran Naveen Tejwani
# Date         : 17/01/2026
#
####################################################################

def CountDigits(iNo):
    iCount = 0

    while(iNo != 0):
        iNo = iNo // 10
        iCount = iCount + 1

    return iCount

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    iValue = 0
    iRet = 0

    print("Enter the number : ",end = "")
    iValue = int(input())

    iRet = CountDigits(iValue) 

    print("Number of digits in an given number is : ",iRet)

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 