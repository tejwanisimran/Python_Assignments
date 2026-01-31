####################################################################
#
# Description :  Write a Python program to implement a class named 
#                BookStore with the following specifications:
#                The class should contain two instance variables:
#                Name (Book Name)
#                Author (Book Author)
#                The class should contain one class variable:
#                NoOfBooks (initialize it to 0)
#                Define a constructor (__init__) that accepts Name 
#                and Author and initializes instance variables.
#                Inside the constructor, increment the class variable 
#                NoOfBooks by 1 whenever a new object is created.
#                Implement an instance method:
#                Display() – should display book details in the format:
#                <BookName> by <Author>. No of Books : <NoOfBooks>
#                
####################################################################


####################################################################
#
# ClassName : BookStore
# Description  : It is used to display the info about the books 
#                inside the bookstore
# Author       : Simran Naveen Tejwani
# Date         : 30/01/2026
#
###################################################################
class BookStore:
    NoOfBooks = 0

    def __init__(self , name , author):
        self.name = name
        self.author = author
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

    def Display(self):
        print(f"{self.name} by {self.author}. NoOf books : {BookStore.NoOfBooks}")

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    bobj1 = BookStore("LSP" , "Robert Love")
    bobj1.Display()

    bobj2 = BookStore("C Programming" , "Denis Ritchie ")
    bobj2.Display()

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 