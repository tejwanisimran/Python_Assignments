####################################################################
#
# Description : Write a lambda function which accepts 2 numbers
#               and returns the Minimum
#
####################################################################

####################################################################
#
# LambdaFunctionName : Minimum
# Description  : It is used to return the Minimum of the 2 numbers
# Author       : Simran Naveen Tejwani
# Date         : 21/01/2026
#
####################################################################

Minimum = lambda iNo1,iNo2 : iNo1 if(iNo1 < iNo2) else iNo2

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    iValue1 = 0
    iValue2 = 0
    iRet = 0

    print("Enter the first number : ")
    iValue1 = int(input())

    print("Enter the second number : ")
    iValue2 = int(input())

    iRet = Minimum(iValue1,iValue2)

    print("Minimum of the given numbers is : ",iRet)


####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 