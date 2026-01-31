####################################################################
#
# Description : Write a program which accepts one number from the 
#               user & check whether the number is +ve , -ve , or zero
# Input       : 10  --> +ve
#               -9  --> -ve
#               0  --> zero
#
####################################################################

####################################################################
#
# FunctionName : CheckPositive
# Description  : It is used to check whether the number is 
#                positive , negative or zero
# Author       : Simran Naveen Tejwani
# Date         : 23/01/2026
#
####################################################################

def CheckPositive(iNo):

    if(iNo > 0):
        print("Positive Number...")
    elif(iNo < 0):
        print("Negative Number...")
    elif(iNo == 0):
        print("Zero..")

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    iValue = 0

    print("Enter the number : ")
    iValue = int(input())

    CheckPositive(iValue)

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 