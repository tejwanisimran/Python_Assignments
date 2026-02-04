####################################################################
#
# Description :Compare Two Files (Command Line)
# Problem Statement: Write a program which accepts two file names 
#                    through command line arguments and compares the 
#                    contents of both files.
#                    If both files contain the same contents, 
#                    display Success Otherwise display Failure
# Input (Command Line): Demo.txt Hello.txt
# Expected Output: Success OR Failure
# 
####################################################################

import os
import sys

####################################################################
#
# FunctionName : CompareFiles
# Description  : It is used to comapre two files
# Author       : Simran Naveen Tejwani
# Date         : 02/02/2026
#
###################################################################

def CompareFiles(First_File , Second_File):
    Ret = os.path.exists(First_File)
    if(Ret == False):
        print("Error : There is no such file or directory...")
        return
    
    Ret = os.path.exists(Second_File)
    if(Ret == False):
        print("Error : There is no such file or directory...")
        return
    
    fobj1 = open(First_File,"r")
    fobj2 = open(Second_File,"r")

    if(fobj1.closed == True and fobj2.closed == True):
        print("File is closed...")
    else :
        print("FIles gets sucessfully opened")

    Data = fobj1.read()
    print("Data from the first file is : ",Data)

    Content = fobj2.read()
    print("Data from the second file is : ",Content)

    if(Data == Content):
        print("Sucess...")
    else:
        print("Failure...")    

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    First_File = sys.argv[1]
    Second_File = sys.argv[2]

    if(len(sys.argv) != 3):
        print("Invalid number of arguments...")
        print("Specify name of the file...")
        return

    CompareFiles(First_File,Second_File)

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 