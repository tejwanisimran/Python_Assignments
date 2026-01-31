####################################################################
#
# Description : Write a program which accept number from the user 
#               & print that number of "*" on screen
# Input       : 5
# Output      : * * * * * 
####################################################################

####################################################################
#
# FunctionName : CheckDivisible
# Description  : It is used to check whether the number is 
#                divisible by 5 or not
# Author       : Simran Naveen Tejwani
# Date         : 23/01/2026
#
####################################################################

def Display(iNo):
    
    for iCnt in range(iNo):
        print("*\t",end = "")
    print("\n")

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    iValue = 0

    print("Enter the number : ")
    iValue = int(input())

    Display(iValue)


####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 