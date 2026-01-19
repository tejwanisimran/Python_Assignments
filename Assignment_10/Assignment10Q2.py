####################################################################
#
# Description : Write a program which accepts one number & prints
#               Sum of first N natural numbers
# Input       : 5
# Output      : 15
#
####################################################################

####################################################################
#
# FunctionName : SumNatural()
# Description  : It is used to print the sum of first N natural
#                numbers
# Author       : Simran Naveen Tejwani
# Date         : 17/01/2026
#
####################################################################

def SumNatural(iNo):
    iSum = 0

    for iCnt in range(iNo+1):
        iSum = iSum + iCnt
        
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

    iRet = SumNatural(iValue) 

    print("Sum of first N natural numbers is :",iRet)
        
####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 