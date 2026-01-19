####################################################################
#
# Description : Write a program which accepts marks & displays grades
# Conditional : >= 75 --> Distinction
# Statement   : >= 60 --> First Class
#             : >= 50 --> Second class
#             : < 50 -->  Fail
#
####################################################################

####################################################################
#
# FunctionName : DisplayGrades()
# Description  : It is used to display grades
# Author       : Simran Naveen Tejwani
# Date         : 19/01/2026
#
####################################################################

def DisplayGrades(fMarks):

    if(fMarks < 0 or fMarks > 100):
        print("Invalid input...!!")
        return -1
    
    if(fMarks >= 75):
        print("First Class With Distinction...")
    elif(fMarks >= 60):
        print("First Class...")
    elif(fMarks >= 50):
        print("Second Class...")
    elif(fMarks < 50):
        print("Fail...!!!")


####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    fValue = 0
    iRet = 0

    print("Enter the marks : ",end = "")
    fValue = float(input())

    DisplayGrades(fValue)

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 