import tkinter as tk
from tkinter import *
import os
from PIL import Image, ImageTk
from tkinter import Label
from tkinter import ttk, messagebox
import mysql.connector
from PIL import Image, ImageTk  # pip install pillow
from hotel1 import HotelManagement

# ---------- Database Config ----------
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "zainab313@_"
DB_NAME = "management"
# -------------------------------------


def get_db_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )


class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management Login")
        self.root.state("zoomed")  # full screen
        self.root.resizable(False, False)

        # === Background image ===
        # put bg.jpg in same folder

        image_path = r"C:/Users/hp/OneDrive/Desktop/Hotel Management project/header2.png"

        if os.path.exists(image_path):
            self.bg = Image.open(image_path)   # ✅ call the function
            self.bg = self.bg.resize((self.root.winfo_screenwidth(),
                                      self.root.winfo_screenheight()))
            self.bg_photo = ImageTk.PhotoImage(self.bg)
            bg_label = Label(self.root, image=self.bg_photo)
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        else:
            # Fallback if file not found
            lblimg = Label(self.root, text="Image not found!",
                           font=("Arial", 20), fg="red")
            lblimg.place(x=0, y=0)

        # === Login Frame ===
        login_frame = Frame(self.root, bg="white", bd=5, relief=RIDGE)
        login_frame.place(relx=0.5, rely=0.5, anchor="center",
                          width=400, height=300)

        title = Label(login_frame, text="Login", font=(
            "Arial", 20, "bold"), bg="white")
        title.pack(pady=10)

        # Username
        lbl_user = Label(login_frame, text="Username",
                         font=("Arial", 12), bg="white")
        lbl_user.pack(pady=(20, 5))
        self.txt_user = Entry(login_frame, font=("Arial", 12))
        self.txt_user.pack(pady=5, ipady=3, ipadx=5)

        # Password
        lbl_pass = Label(login_frame, text="Password",
                         font=("Arial", 12), bg="white")
        lbl_pass.pack(pady=(20, 5))
        self.txt_pass = Entry(login_frame, font=("Arial", 12), show="*")
        self.txt_pass.pack(pady=5, ipady=3, ipadx=5)

        # Button
        btn_login = Button(login_frame, text="Login", font=("Arial", 14, "bold"),
                           bg="#4CAF50", fg="white", command=self.login_user)
        btn_login.pack(pady=30, ipadx=20, ipady=5)

    def login_user(self):
        user = self.txt_user.get()
        pwd = self.txt_pass.get()

        if user == "" or pwd == "":
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute(
                "SELECT * FROM users WHERE username=%s AND password=%s", (user, pwd))
            row = cur.fetchone()
            conn.close()

            if row:
                messagebox.showinfo("Success", f"Welcome {user}!")
                # TODO: Open your hotel dashboard window here
                self .new_window = Toplevel(self.root)
                self.app = HotelManagement(self.new_window)
            else:
                messagebox.showerror("Error", "Invalid Username or Password")
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginPage(root)
    root.mainloop()
