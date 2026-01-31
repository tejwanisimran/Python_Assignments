####################################################################
#
# FunctionName : CheckPrime
# Description  : It is used to check whether the number is 
#                prime or not 
# Author       : Simran Naveen Tejwani
# Date         : 25/01/2026
#
####################################################################

def CheckPrime(Arr):
    List = list()
    iSum = 0

    for num in Arr:
        if num <= 1:
            continue
        bFlag = True
        for iCnt in range(2,num //2 + 1):
            if(num % iCnt == 0):
                bFlag = False
                break
        if bFlag:
            List.append(num) 
            
    print("Prime numbers from the list are : ",List)

    for iCnt in List:
        iSum = iSum + iCnt

    print("Summation is : ",iSum)


            


