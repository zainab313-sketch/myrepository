# from tkinter import *
# from PIL import Image, ImageTk  # pip install pillow


# class HotelManagementSystem:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Hotel Management System")
#         self.root.geometry("1550x800+0+0")

#         # Load and resize image
#         img1 = Image.open(
#             r"C:/Users/hp/OneDrive/Desktop/Hotel management system/5.jpg"
#         )
#         img1 = img1.resize((1550, 140), Image.ANTIALIAS)
#         self.photoimg1 = ImageTk.PhotoImage(img1)

#         # Place image on label
#         lblimg1 = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
#         lblimg1.place(x=0, y=0, width=1550, height=140)


# if __name__ == "__main__":
#     root = Tk()
#     obj = HotelManagementSystem(root)
#     root.mainloop()


# import mysql.connector

# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="your_password",
#     database="hotel_management"
# )
# print("✅ Connected to MySQL")


# import tkinter as tk
# from tkinter import messagebox

# root = tk.Tk()
# root.withdraw()  # (optional, hides root window if you just want popup)

# messagebox.showerror("Error", "Something went wrong")

from time import strftime
print(strftime("%Y-%m-%d %H:%M:%S"))
