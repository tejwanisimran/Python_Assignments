####################################################################
#
# Description : Write a program which contains one function named
#               as ChkGreater() that accepts two numbers & print 
#               the greater number.
# Input       : 10 20 
# Output      : 20 is greater
#
####################################################################

####################################################################
#
# FunctionName : ChkGreater()
# Description  : It is used to display the greater number among two
# Author       : Simran Naveen Tejwani
# Date         : 17/01/2026
#
####################################################################

def ChkGreater(iNo1,iNo2):
    iGreater = 0

    if(iNo1 > iNo2):
        iGreater = iNo1
    else:
        iGreater = iNo2

    return iGreater

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    iValue1 = 0
    iValue2 = 0
    iRet = 0

    print("Enter the first number : ",end = "")
    iValue1 = int(input())

    print("Enter the second number : ",end = "")
    iValue2 = int(input())

    iRet = ChkGreater(iValue1,iValue2) 

    print("The greater number is : ",iRet)

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 