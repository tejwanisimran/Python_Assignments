####################################################################
#
# Description : Write a program which contains one function named as 
#               ChkNum() which accept one parameter as number. 
#               If number is even then it should display "Even number"
#               otherwise "Odd number " on console.
# Input       : 11
# Output      : Odd Number
#
####################################################################

####################################################################
#
# FunctionName : ChkNum
# Description  : It is used to check whether the number is even or odd
# Author       : Simran Naveen Tejwani
# Date         : 23/01/2026
#
####################################################################

def ChkNum(iNo):
    bFlag = False

    if(iNo % 2 == 0):
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

    print("Enter the number : ")
    iValue = int(input())

    bRet = ChkNum(iValue)

    if(bRet == True):
        print("Even Number...")
    else :
        print("Odd Number...")

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 