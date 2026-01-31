####################################################################
#
# Description : Write a program which accept one number from the 
#               user & return addition of digits in that number
# Input       : 5187934
# Output      : 37
#
####################################################################

####################################################################
#
# FunctionName : SumDigits
# Description  : It is used to sum the digits of the given
#                number 
# Author       : Simran Naveen Tejwani
# Date         : 25/01/2026
#
####################################################################

def SumDigits(iNo):
    iSum = 0
    iDigit = 0

    while(iNo != 0):
        iDigit = iNo % 10
        iSum = iSum + iDigit
        iNo = iNo // 10

    return iSum

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

    iRet = SumDigits(iValue)

    print("Sum of Digits is : ",iRet)
    
####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 