####################################################################
#
# Display File Line by Line
# Problem Statement : Write a program which accepts a file name from 
#                     the user and displays the contents of the file 
#                     line by line on the screen.
# Input : Demo.txt
# Expected Output : Display each line of Demo.txt one by one.
# 
####################################################################

import os
import sys

####################################################################
#
# FunctionName : DisplayFileLineByLine
# Description  : It is used to display file line by line
# Author       : Simran Naveen Tejwani
# Date         : 04/02/2026
#
###################################################################
def DisplayFileLineByLine(File_Name):
    Ret = os.path.exists(File_Name)
    if(Ret == False):
        print("Error : There is no such file or directory...")
        return
    
    fobj = open(File_Name,"r")


    Data = fobj.read()

    print("Data from the file is : ",Data)

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    File_Name = sys.argv[1]

    if(len(sys.argv) != 2):
        print("Invalid number of arguments...")
        print("Specify name of the file...")
        return

    DisplayFileLineByLine(File_Name)

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 