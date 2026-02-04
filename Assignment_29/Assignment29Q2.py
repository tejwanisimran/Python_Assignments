####################################################################
#
# Description :  Display File Contents
# Problem Statement: Write a program which accepts a file name from 
#                    the user, opens that file, and displays the entire 
#                    contents on the console.
# Input: Demo.txt
# Expected Output : Display contents of Demo.txt on console.
# 
####################################################################

import os

####################################################################
#
# FunctionName : DisplayFile
# Description  : It is used to display all file contents of the file
# Author       : Simran Naveen Tejwani
# Date         : 02/02/2026
#
###################################################################

def DisplayFile(File_Name):

    Ret = os.path.exists(File_Name)

    if(Ret == False):
        print("Unable to read the file contents as file doesn't exists...")
        return
    
    fobj = open(File_Name , "r")

    if(fobj.closed == True):
        print("File is closed...")
    else :
        print("File is sucessfully opened...")

    Data = fobj.read()

    print("Data from the file is : ",Data)

    fobj.close()


####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    print("Enter the file name : ",end = "")
    File_Name = input()

    DisplayFile(File_Name)

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 