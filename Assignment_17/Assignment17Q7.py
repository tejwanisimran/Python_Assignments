####################################################################
#
# Description : Write a program which accept one number and display 
#               below pattern
# Input       : 5
# Output      : 1 2 3 4 5 
#               1 2 3 4 5 
#               1 2 3 4 5
#               1 2 3 4 5 
#               1 2 3 4 5 
####################################################################

####################################################################
#
# FunctionName : Display
# Description  : It is used to display the above pattern
# Author       : Simran Naveen Tejwani
# Date         : 25/01/2026
#
####################################################################

def Display(iNo):

    for i in range(1 , iNo + 1):
        for j in range(1 , iNo + 1):
            print(j,"\t",end = "")
        print("\n")

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    iValue = 0

    print("Enter number :",end = "")
    iValue = int(input())

    Display(iValue)

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 