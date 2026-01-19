####################################################################
#
# Description : Write a program which accepts two numbers & prints
#               addition substraction and multiplication
#
####################################################################

####################################################################
#
# FunctionName : Addition()
# Description  : It is used to return addition of a given
#                numbers
# Author       : Simran Naveen Tejwani
# Date         : 19/01/2026
#
####################################################################

def Addition(iNo1,iNo2):
    iAns = 0

    iAns = iNo1 + iNo2

    return iAns

####################################################################
#
# FunctionName : Subtraction()
# Description  : It is used to return subtraction of a given
#                numbers
# Author       : Simran Naveen Tejwani
# Date         : 19/01/2026
#
####################################################################

def Subtraction(iNo1,iNo2):
    iAns = 0

    iAns = iNo1 - iNo2

    return iAns

####################################################################
#
# FunctionName : Multiplication()
# Description  : It is used to return Multiplication of a given
#                numbers
# Author       : Simran Naveen Tejwani
# Date         : 19/01/2026
#
####################################################################

def Multiplication(iNo1,iNo2):
    iAns = 0

    iAns = iNo1 * iNo2

    return iAns

####################################################################
#
# FunctionName : Division()
# Description  : It is used to return Division of a given
#                numbers
# Author       : Simran Naveen Tejwani
# Date         : 19/01/2026
#
####################################################################

def Division(iNo1,iNo2):
    iAns = 0
    try:
        iAns = iNo1 / iNo2
    except ZeroDivisionError as zobj:
        print("Exception :",zobj)

    return iAns

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

    iRet = Addition(iValue1 , iValue2) 
    print("Addition is : ",iRet)

    iRet = Subtraction(iValue1 , iValue2) 
    print("Subtraction is : ",iRet)

    iRet = Multiplication(iValue1 , iValue2) 
    print("Multiplication is : ",iRet)

    iRet = Division(iValue1 , iValue2) 
    print("Division is : ",iRet)

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 