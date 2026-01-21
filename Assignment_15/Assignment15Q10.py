####################################################################
#
# Description : Write a lambda function using filter() which accepts 
#               list of numbers and returns count of all even elements
#
####################################################################

####################################################################
#
# LambdaFunctionName : CountEven
# Description  : It is used to count all the even elements from the
#                list
# Author       : Simran Naveen Tejwani
# Date         : 21/01/2026
#
####################################################################

CountEven = lambda iNo : iNo % 2 == 0

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

    FData = list(filter(CountEven , Data))

    print("Even numbers from the list is : ",len(FData))

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 