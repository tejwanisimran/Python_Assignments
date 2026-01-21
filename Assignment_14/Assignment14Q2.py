####################################################################
#
# Description : Write a lambda function  which accepts 1 number
#               and returns cube of that number
#
####################################################################

####################################################################
#
# LambdaFunctionName : Cube
# Description  : It is used to cube the given number
# Author       : Simran Naveen Tejwani
# Date         : 21/01/2026
#
####################################################################

Cube = lambda iNo : iNo * iNo * iNo

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

    iRet = Cube(iValue)

    print("Cube of the given number is : ",iRet)


####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 