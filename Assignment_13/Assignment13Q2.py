####################################################################
#
# Description : Write a program which accepts radius of circle &
#               prints area of circle
#
####################################################################

import math

####################################################################
#
# FunctionName : CalculateAreaOfCircle()
# Description  : It is used to print the area of a circle
# Author       : Simran Naveen Tejwani
# Date         : 19/01/2026
#
####################################################################

def CalculateAreaOfCircle(iRadius):
    iArea = 0

    iArea = (math.pi) * (iRadius ** 2)

    return iArea

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    iRadius = 0
    iRet = 0

    print("Enter the radius : ",end = "")
    iRadius = int(input())

    iRet = CalculateAreaOfCircle(iRadius)

    print("Area of Circle is : ",iRet)

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 