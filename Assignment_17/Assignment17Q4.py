####################################################################
#
# Description : Write a program which accept one number from the 
#               user & return addition of its factors
#               
# Input       : 12
# Output      : 16
#
####################################################################

####################################################################
#
# FunctionName : SumFactors
# Description  : It is used to return the sum of factors of the  
#                given number
# Author       : Simran Naveen Tejwani
# Date         : 25/01/2026
#
####################################################################

def SumFactors(iNo):
    iSum = 0

    for iCnt in range(1,(iNo // 2)+1):
        if(iNo % iCnt == 0):
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

    print("Enter number : ",end = "")
    iValue = int(input())

    iRet = SumFactors(iValue)

    print("Addition of factors is : ",iRet)

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 