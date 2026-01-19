####################################################################
#
# Description : Write a program which accepts one number & checks 
#               whether the number is a perfect number or not
# Input       : 6
# output      : Perfect Number...
#
####################################################################

####################################################################
#
# FunctionName : CheckPerfect()
# Description  : It is used to check whether the given number 
#                is Perfect number or not
# Author       : Simran Naveen Tejwani
# Date         : 19/01/2026
#
####################################################################

def CheckPerfect(iNo):
    iSum = 0
    bFlag = False

    for iCnt in range(1 , (iNo//2)+1):
        if(iNo % iCnt == 0):
            iSum = iSum + iCnt
    
    if(iSum == iNo):
        bFlag = True
    
    return bFlag

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    iValue = 0
    bRet = True

    print("Enter the number : ",end = "")
    iValue = int(input())

    bRet = CheckPerfect(iValue)

    if(bRet == True):
        print("Perfect Number...")
    else : 
        print("Not a Perfect Number...")

    

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 