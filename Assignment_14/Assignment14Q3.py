####################################################################
#
# Description : Write a lambda function which accepts 2 numbers
#               and returns the maximum
#
####################################################################

####################################################################
#
# LambdaFunctionName : Maximum
# Description  : It is used to return the maximum of the 2 numbers
# Author       : Simran Naveen Tejwani
# Date         : 21/01/2026
#
####################################################################

Maximum = lambda iNo1,iNo2 : iNo1 if(iNo1 > iNo2) else iNo2

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

    iRet = Maximum(iValue1,iValue2)

    print("Maximum of the given numbers is : ",iRet)


####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 