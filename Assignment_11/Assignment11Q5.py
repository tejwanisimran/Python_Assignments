####################################################################
#
# Description : Write a program which accepts one number & checks
#               whether the given number is palindrome or not
# Input       : 121
# Output      : Palindrome
#
####################################################################

####################################################################
#
# FunctionName : CheckPalindrome()
# Description  : It is used to check the given number is palindrome 
#                or not 
# Author       : Simran Naveen Tejwani
# Date         : 17/01/2026
#
####################################################################

def CheckPalindrome(iNo):
    iDigit = 0
    iRev = 0
    iTemp = iNo
    bFlag = False

    while(iNo != 0):
        iDigit = iNo % 10
        iRev = iRev * 10 + iDigit
        iNo = iNo // 10

    if(iTemp == iRev):
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

    bRet = CheckPalindrome(iValue) 

    if(bRet == True):
        print("Number is Palindrome...")
    else:
        print("Number is not Palindrome")


####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 