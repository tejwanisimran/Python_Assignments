####################################################################
#
# Description : Write a lambda function which accepts 3 numbers
#               and returns Largest numbers
#
####################################################################

####################################################################
#
# LambdaFunctionName : LargestNumber
# Description  : It is used to return the LargestNumber of 3 numbers
# Author       : Simran Naveen Tejwani
# Date         : 21/01/2026
#
####################################################################

LargestNumber = lambda iNo1 , iNo2 , iNo3 : iNo1 if(iNo1 > iNo2 and iNo1 > iNo3) else(iNo2 if(iNo2 > iNo1 and iNo2 > iNo3) else iNo3)

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    iValue1 = 0
    iValue2 = 0
    iValue3 = 0
    iRet = 0

    print("Enter the first number : ")
    iValue1 = int(input())

    print("Enter the second number : ")
    iValue2 = int(input())

    print("Enter the third number : ")
    iValue3 = int(input())

    iRet = LargestNumber(iValue1 , iValue2,iValue3)

    print("LargestNumber is : ",iRet)

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 