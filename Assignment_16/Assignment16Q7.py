####################################################################
#
# Description : Write a program which contains one function that accept
#               one number from the user and returns true if number is 
#               divisible by 5  otherwise returns false
# Input       : 8 
# Output      : False
####################################################################

####################################################################
#
# FunctionName : CheckDivisible
# Description  : It is used to check whether the number is 
#                divisible by 5 or not
# Author       : Simran Naveen Tejwani
# Date         : 23/01/2026
#
####################################################################

def CheckDivisible(iNo):
    return(iNo % 5 == 0)

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    iValue = 0
    iRet = 0

    print("Enter the number : ")
    iValue = int(input())

    iRet = CheckDivisible(iValue)

    print(iRet)

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 