####################################################################
#
# Description : Write a program which accept one number from the 
#               user & return number of digits in the given number
# Input       : 5896547
# Output      : 7
#
####################################################################

####################################################################
#
# FunctionName : ContDigits
# Description  : It is used to count number of digits in an given 
#                number 
# Author       : Simran Naveen Tejwani
# Date         : 25/01/2026
#
####################################################################

def CountDigits(iNo):
    iCount = 0
    iDigit = 0

    while(iNo != 0):
        iDigit = iNo % 10
        iCount = iCount + 1
        iNo = iNo // 10

    return iCount

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    iValue = 0
    iret = 0

    print("Enter number : ",end = "")
    iValue = int(input())

    iRet = CountDigits(iValue)

    print("Number of Digits are : ",iRet)
    
####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 