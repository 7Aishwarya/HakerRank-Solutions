from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook(Book):
    def __init__(self,title,author,price):
        self.price = price
        Book.__init__(self,title,author)
    def display(self):
        print("Title: ", end = "")
        print(self.title)
        print("Author: ", end = "")
        print(self.author)
        print("Price: ", end = "")
        print(self.price)

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()