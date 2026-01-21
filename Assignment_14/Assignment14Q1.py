####################################################################
#
# Description : Write a lambda function which accepts 1 number
#               and returns square of that number
#
####################################################################

####################################################################
#
# LambdaFunctionName : Square
# Description  : It is used to quare the given number
# Author       : Simran Naveen Tejwani
# Date         : 21/01/2026
#
####################################################################

Square = lambda iNo : iNo * iNo

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

    iRet = Square(iValue)

    print("Square of the given number is : ",iRet)


####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 