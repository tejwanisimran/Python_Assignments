####################################################################
#
# Description : Write a program which accept one number from the 
#               user & check whether the given number is prime 
#               or not
# Input       : 5
# Output      : It is a prime number
#
####################################################################

####################################################################
#
# FunctionName : CheckPrime
# Description  : It is used to check whether the given number 
#                is prime or not
# Author       : Simran Naveen Tejwani
# Date         : 25/01/2026
#
####################################################################

def CheckPrime(iNo):
    bFlag = True

    for iCnt in range(2,(iNo // 2)+1):
        if(iNo % iCnt == 0):
            bFlag = False
            break
    return bFlag

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    iValue = 0
    bRet = False

    print("Enter number : ",end = "")
    iValue = int(input())

    bRet = CheckPrime(iValue)

    if(bRet == True):
        print("It is a Prime number...")
    else :
        print("It is not a Prime number...")

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 