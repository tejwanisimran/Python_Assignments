####################################################################
#
# Description : Write a lambda function using filter() which accepts 
#               list of numbers and returns a list of even numbers
#
####################################################################

####################################################################
#
# LambdaFunctionName : CheckEven
# Description  : It is used to check the even numbers from a list
# Author       : Simran Naveen Tejwani
# Date         : 20/01/2026
#
####################################################################
CheckEven = lambda iNo : (iNo % 2 == 0)

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    iSize = 0
    iValue = 0
    FData = 0

    print("Enter number of elements : ")
    iSize = int(input())

    Data = list()

    print("Enter the elements : ")

    for iCnt in range(iSize):
        iValue = int(input())
        Data.append(iValue)

    FData = list(filter(CheckEven , Data))

    print("Even numbers from the list is : ",FData)

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 