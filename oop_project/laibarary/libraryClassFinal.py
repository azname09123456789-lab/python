import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from PIL import Image, ImageTk



class book:
    def __init__(self,name, outhor, langauge, pages, status,price,topic):
        self.name=name
        self.outhor=outhor
        self.language=langauge
        self.pages=pages
        self.status=status
        self.price=price
        self.topic=topic
    def __str__(self):
        return(
            f"The book name: {self.name}\n"
            f"The book outhor: {self.outhor}\n"
            f"The book main Language:  {self.language}\n"
            f"The book pages:  {self.pages}\n"
            f"The Book status is: {self.status}"
            f"The Book price is: {self.price}"
            f"The Book topic is: {self.topic}"
        )






class library:
    def __init__(self):
        self.books=[]
    def add_book(self,book):
        self.books.append(book)
lib1=library()
    