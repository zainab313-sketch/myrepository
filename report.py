from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
import os
import tkinter as tk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class Report:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1042x450+224+202")


if __name__ == "__main__":
    root = Tk()
    obj = Report(root)
    root.mainloop()
