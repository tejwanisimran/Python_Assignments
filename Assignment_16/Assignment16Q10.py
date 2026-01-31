####################################################################
#
# Description : Write a program which accept name from the user & 
#               display length of its name
# Input       : Simran
# Output      : 6
####################################################################

####################################################################
#
# FunctionName : CountLength
# Description  : It is used to count the length of the name given by
#                the user
# Author       : Simran Naveen Tejwani
# Date         : 23/01/2026
#
####################################################################

def CountLength(Name):
    iCount = 0
    
    for iCnt in Name : 
        iCount = iCount + 1

    return iCount        

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    name = None
    iRet = 0

    print("Enter the name : ",end = "")
    name = input()

    iRet = CountLength(name)

    print("Length of given name is : ",iRet)

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 