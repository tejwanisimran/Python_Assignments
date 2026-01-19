####################################################################
#
# Description : Write a program which accepts one number & prints
#               sum of digits
# Input       : 521
# Output      : 8
#
####################################################################

####################################################################
#
# FunctionName : SumDigits()
# Description  : It is used to calcilate sum  of digits of a given
#                number
# Author       : Simran Naveen Tejwani
# Date         : 17/01/2026
#
####################################################################

def SumDigits(iNo):
    iDigit = 0
    iSum = 0


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
    iRet = 0

    print("Enter the number : ",end = "")
    iValue = int(input())

    iRet = SumDigits(iValue) 

    print("Sum of digits is : ",iRet)

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 