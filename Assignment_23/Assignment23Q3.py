####################################################################
#
# Description :  Write a Python program to implement a class named 
#                Numbers with the following specifications:
#                The class should contain one instance variable:
#                Value
#                Define a constructor (__init__) that accepts a number 
#                from the user and initializes Value.
#                Implement the following instance methods:
#                ChkPrime() – returns True if the number is prime, 
#                otherwise returns False
#                ChkPerfect() – returns True if the number is perfect, 
#                otherwise returns False
#                Factors() – displays all factors of the number
#                SumFactors() – returns the sum of all factors
#                (You may use this method as a helper in ChkPerfect() 
#                if required)
#                Create multiple objects and call all methods.
#               
####################################################################


####################################################################
#
# ClassName : Numbers
# Description  : It is used to do the mathematical operations
# Author       : Simran Naveen Tejwani
# Date         : 30/01/2026
#
###################################################################
class Numbers:

    def __init__(self,iValue):
        self.iValue = iValue

    def CheckPrime(self):
        bFlag = True
        for iCnt in range(2 , (self.iValue // 2)+ 1 ,1):
            if(self.iValue % iCnt == 0):
                bFlag = False
                break

        return bFlag

    def CheckPerfect(self):
        iSum = 0
        bFlag = False

        for iCnt in range(1,(self.iValue // 2)+1 , 1):
            if(self.iValue % iCnt == 0):
                iSum = iSum + iCnt

        if(iSum == self.iValue):
            bFlag = True

        return bFlag
    
    def Factors(self):
        List = list()

        for iCnt in range(1,(self.iValue // 2)+1 , 1):
            if(self.iValue % iCnt == 0):
                List.append(iCnt)

        print("Factors are : ",List)

    def SumFactors(self):
        iSum = 0
        List = list()

        for iCnt in range(1,(self.iValue // 2)+1 , 1):
            if(self.iValue % iCnt == 0):
                List.append(self.iValue)
                iSum = iSum + iCnt

        return iSum

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    iRet = 0

    nobj1 = Numbers(6)

    iRet = nobj1.CheckPrime()

    if(iRet == True):
        print("It is prime...")
    else :
        print("It is not prime...")

    iRet = nobj1.CheckPerfect()

    if(iRet == True):
        print("It is perfect...")
    else : 
        print("It is not perfect...")

    nobj1.Factors()

    iRet = nobj1.SumFactors()

    print("Sumation is : ",iRet)

    print("------------------------------------------------")

    nobj2 = Numbers(5)

    iRet = nobj2.CheckPrime()

    if(iRet == True):
        print("It is prime...")
    else :
        print("It is not prime...")

    iRet = nobj2.CheckPerfect()

    if(iRet == True):
        print("It is perfect...")
    else : 
        print("It is not perfect...")

    nobj2.Factors()

    iRet = nobj2.SumFactors()

    print("Sumation is : ",iRet)

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 