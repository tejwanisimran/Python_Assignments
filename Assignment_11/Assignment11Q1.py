####################################################################
#
# Description : Write a program which accepts one number & checks
#               whether that number is prime or not
# Input       : 11
# Output      : Prime Number
#
####################################################################

####################################################################
#
# FunctionName : CheckPrime()
# Description  : It is used to check whether the given number is 
#                prime or not
# Author       : Simran Naveen Tejwani
# Date         : 17/01/2026
#
####################################################################

def CheckPrime(iNo):
    bFlag = True

    for iCnt in range(2,(iNo// 2)+1):
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

    print("Enter the number : ",end = "")
    iValue = int(input())

    bRet = CheckPrime(iValue) 

    if(bRet == True):
        print("Prime Number")
    else:
        print("Not a Prime Number")

        
####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 