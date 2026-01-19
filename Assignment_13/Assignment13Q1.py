####################################################################
#
# Description : Write a program which accepts length & width of 
#               a rectangle and prints area
#
####################################################################

####################################################################
#
# FunctionName : CalculateAreaOfRectangle()
# Description  : It is used to print the area of a rectangle
# Author       : Simran Naveen Tejwani
# Date         : 19/01/2026
#
####################################################################

def CalculateAreaOfRectangle(iLength , iWidth):
    iArea = 0

    iArea = iLength * iWidth

    return iArea

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    iLength = 0
    iWidth = 0
    iRet = 0

    print("Enter the length : ",end = "")
    iLength = int(input())

    print("Enter the width : ",end = "")
    iWidth = int(input())

    iRet = CalculateAreaOfRectangle(iLength , iWidth)

    print("Area of Rectangle is : ",iRet)

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 