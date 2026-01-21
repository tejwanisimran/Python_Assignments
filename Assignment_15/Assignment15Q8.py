####################################################################
#
# Description : Write a lambda function using filter() which accepts 
#               list of numbers and returns list of numbers that
#               are divisible by 3 & 5
#
####################################################################


####################################################################
#
# LambdaFunctionName : CheckDivisible
# Description  : It is used to check whether the divisible by 
#                3 & 5 or not
# Author       : Simran Naveen Tejwani
# Date         : 20/01/2026
#
####################################################################

CheckDivisible = lambda iNo : (iNo % 3 == 0 and iNo % 5 == 0)

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

    FData = list(filter(CheckDivisible , Data))

    print("Numbers from the list that are divisible by 3 & 5 are : ",FData)
    
####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 