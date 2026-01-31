####################################################################
#
# FunctionName : Add
# Description  : It is used to perfrom Addition
# Author       : Simran Naveen Tejwani
# Date         : 23/01/2026
#
####################################################################

def Add(iNo1 , iNo2):
    iAns = 0
    iAns = iNo1 + iNo2
    return iAns

####################################################################
#
# FunctionName : Sub
# Description  : It is used to perfrom Subtraction
# Author       : Simran Naveen Tejwani
# Date         : 23/01/2026
#
####################################################################

def Sub(iNo1 , iNo2):
    iAns = 0
    iAns = iNo1 - iNo2
    return iAns

####################################################################
#
# FunctionName : Mult
# Description  : It is used to perfrom Multiplication
# Author       : Simran Naveen Tejwani
# Date         : 23/01/2026
#
####################################################################

def Mult(iNo1 , iNo2):
    iAns = 0
    iAns = iNo1 * iNo2
    return iAns

####################################################################
#
# FunctionName : Div
# Description  : It is used to perfrom Division
# Author       : Simran Naveen Tejwani
# Date         : 23/01/2026
#
####################################################################

def Div(iNo1 , iNo2):
    iAns = 0
    try :
        iAns = iNo1 / iNo2
    except ZeroDivisionError as zobj :
        print("Error : ",zobj)

    return iAns


