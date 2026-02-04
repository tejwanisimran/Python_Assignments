####################################################################
#
# Description :Copy File Contents into a New File (Command Line)
# Problem Statement: Write a program which accepts an existing 
#                    file name through command line arguments, 
#                    creates a new file named Demo.txt, and copies all 
#                    contents from the given file into Demo.txt.
# Input (Command Line): ABC.txt
# Expected Output: Create Demo.txt and copy contents of ABC.txt 
#                  into Demo.txt.
# 
####################################################################

import os
import sys

####################################################################
#
# FunctionName : CopyFile
# Description  : It is used to copy the file contents from one
#                file to another
# Author       : Simran Naveen Tejwani
# Date         : 02/02/2026
#
###################################################################

def CopyFile(Source_File , Destination_File):

    Ret = os.path.exists(Source_File)

    if(Ret == False):
        print("Unable to read the file contents as file doesn't exists...")
        return
    
    fd1 = open(Source_File , "r")

    if(fd1.closed == True):
        print("File is closed...")
    else :
        print("File is sucessfully opened...")

    Data = fd1.read()
    print("Data from the source file is : ",Data)

    fd1.close()

    fd2 = open(Destination_File , "w")

    if(fd2.closed == True):
        print("File is closed...")
    else :
        print("File is sucessfully opened...")

    fd2.write(Data)

    print("Data from the destination file is : ",Data)

    fd2.close()


####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    print("Enter the file name : ",end = "")
    Destination_File = input()
    Source_File = sys.argv[1]

    if(len(sys.argv) != 2):
        print("Invalid number of arguments...")
        print("Specify name of the file...")
        return

    CopyFile(Source_File,Destination_File)

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 