import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
import os
from PIL import Image, ImageTk  # pip install pillow
from hotel1 import HotelManagement

# ---------- Database Config ----------
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "zainaB313@_"   # <-- change to your MySQL password
DB_NAME = "management"
# -------------------------------------


def get_db_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

# ---------- Login Page ----------


class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management Login")
        self.root.state("zoomed")  # full screen
        # self.root.resizable(False, False)

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
        # self.bg = Image.open(
        #     "C:/Users/hp/OneDrive/Desktop/Hotel Management project/header2,bg.png")
        # self.bg = self.bg.resize((self.root.winfo_screenwidth(),
        #                           self.root.winfo_screenheight()))
        # self.bg_photo = ImageTk.PhotoImage(self.bg)
        # bg_label = Label(self.root, image=self.bg_photo)
        # bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # === Login Frame ===
        login_frame = Frame(self.root, bg="#b3c9ba", bd=5, relief=RIDGE)
        login_frame.place(relx=0.5, rely=0.5, anchor="center",
                          width=400, height=350)

        title = Label(login_frame, text="Login", font=(
            "Arial", 20, "bold"), bg="#b3c9ba")
        title.pack(pady=10)

        # Username
        lbl_user = Label(login_frame, text="Username",
                         font=("Arial", 12), bg="#b3c9ba")
        lbl_user.pack(pady=(20, 5))
        self.txt_user = Entry(login_frame, font=("Arial", 12))
        self.txt_user.pack(pady=5, ipady=3, ipadx=5)

        # Password
        lbl_pass = Label(login_frame, text="Password",
                         font=("Arial", 12), bg="#b3c9ba")
        lbl_pass.pack(pady=(20, 5))
        self.txt_pass = Entry(login_frame, font=("Arial", 12), show="*")
        self.txt_pass.pack(pady=5, ipady=3, ipadx=5)

        # Login Button
        btn_login = Button(login_frame, text="Login", font=("Arial", 14, "bold"),
                           bg="#b3c9ba", fg="#004b23", command=self.login_user)
        btn_login.pack(pady=20, ipadx=20, ipady=5)

       # Switch to Register Button
        btn_register = Button(
            login_frame,
            text="Create an Account",
            font=("Arial", 11, "underline"),
            fg="#004b23",
            bg="#b3c9ba",
            bd=0,
            cursor="hand2",
            command=self.open_register
        )
        btn_register.pack(pady=0)

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

    def open_register(self):
        self.new_win = Toplevel(self.root)
        RegisterPage(self.new_win)

# ---------- Register Page ----------


class RegisterPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Register Account")
        self.root.geometry("400x400")
        self.root.config(bg="#b3c9ba")

        title = Label(self.root, text="Register", font=(
            "Arial", 20, "bold"), bg="#b3c9ba")
        title.pack(pady=10)

        # Username
        lbl_user = Label(self.root, text="Username",
                         font=("Arial", 12), bg="#b3c9ba")
        lbl_user.pack(pady=(20, 5))
        self.txt_user = Entry(self.root, font=("Arial", 12))
        self.txt_user.pack(pady=5, ipady=3, ipadx=5)

        # Password
        lbl_pass = Label(self.root, text="Password",
                         font=("Arial", 12), bg="#b3c9ba")
        lbl_pass.pack(pady=(20, 5))
        self.txt_pass = Entry(self.root, font=("Arial", 12), show="*")
        self.txt_pass.pack(pady=5, ipady=3, ipadx=5)

        # Confirm Password
        lbl_cpass = Label(self.root, text="Confirm Password",
                          font=("Arial", 12), bg="#b3c9ba")
        lbl_cpass.pack(pady=(20, 5))
        self.txt_cpass = Entry(self.root, font=("Arial", 12), show="*")
        self.txt_cpass.pack(pady=5, ipady=3, ipadx=5)

        # Register Button
        btn_register = Button(self.root, text="Register", font=("Arial", 14, "bold"),
                              bg="#b3c9ba", fg="#004b23", command=self.register_user)
        btn_register.pack(pady=30, ipadx=20, ipady=5)

    def register_user(self):
        user = self.txt_user.get()
        pwd = self.txt_pass.get()
        cpwd = self.txt_cpass.get()

        if user == "" or pwd == "" or cpwd == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
            return
        if pwd != cpwd:
            messagebox.showerror(
                "Error", "Passwords do not match", parent=self.root)
            return

        try:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO users (username, password) VALUES (%s, %s)", (user, pwd))
            conn.commit()
            conn.close()
            messagebox.showinfo(
                "Success", "Registration successful", parent=self.root)
            self.root.destroy()  # close register window
        except mysql.connector.IntegrityError:
            messagebox.showerror(
                "Error", "Username already exists", parent=self.root)
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", str(e), parent=self.root)


# ---------- Main ----------
if __name__ == "__main__":
    root = tk.Tk()
    app = LoginPage(root)
    root.mainloop()
