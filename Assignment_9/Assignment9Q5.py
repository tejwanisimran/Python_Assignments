####################################################################
#
# Description : Write a program which accepts one number & checks
#               whether that number is divisible by 3 & 5 or not
# Input       : 15
# Output      : Divisible by 3 & 5
#
####################################################################

####################################################################
#
# FunctionName : CheckDivisible()
# Description  : It is used to check whether the given number is 
#                divisible by 3 & 5 or not
# Author       : Simran Naveen Tejwani
# Date         : 17/01/2026
#
####################################################################

def CheckDivisible(iNo):
    bFlag = False

    if((iNo % 3 == 0) and (iNo % 5 == 0)):
        bFlag = True
    
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

    bRet = CheckDivisible(iValue) 

    if(bRet == True):
        print("The given number is divisible by 3 & 5")
    else:
        print("The given number is not divisible 3 & 5")
        
####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 