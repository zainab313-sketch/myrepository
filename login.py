import tkinter as tk
from PIL import Image, ImageTk
import os
from tkinter import Label
from tkinter import Frame
from tkinter import RIDGE
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
import hashlib
from hotel1 import HotelManagement


# def main():
#     win = Tk()
#     app = Login_page(win)
#     win.mainloop()

#     class Login_page:
#         def __init__(self, root):
#             self.root = root
#             self.root.title("LOGIN")
#             self.root.geometry("1350x700+0+0")

#             self.bg = ImageTk.PhotoImage(
#                 file=r"C:/Users/hp/OneDrive/Desktop/Hotel management system/33.png")
#             lbl_bg = Label(self.root, image=self.bg)
#             lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

#             frame = Frame(self.root, bg="#b3c9ba")
#             frame.place(x=610, y=170, width=1350, height=700)

#             img_path = r"C:/Users/hp/OneDrive/Desktop/Hotel management system/loginicon.jpeg"

#         if os.path.exists(img_path):
#             img1 = Image.open(img_path)
#             img1 = img1.resize((1550, 130), Image.Resampling.LANCZOS)
#             self.photoimg1 = ImageTk.PhotoImage(img1)

#             lblimg = Label(self.root, image=self.photoimg1)
#             lblimg.place(x=730, y=170, width=90, height=90)

#         else:
#             # Fallback if file not found
#             lblimg = Label(self.root, text="Image not found!",
#                            font=("Arial", 20), fg="red")
#             lblimg.place(x=100, y=100)

#             get_str = Label(frame, text="Get Started", font=(
#                 "times new roman", 12, "bold"), fg="#004b23", bg="#b3c9ba", relief=RIDGE)
#             get_str.place(x=95, y=85)


# ---------- Config: update these to match your MySQL setup ----------
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'zainaB313@_'   # <-- set your MySQL root password or user password here
DB_NAME = 'management'
# --------------------------------------------------------------------


# def main():
#     win = Tk()
#     app = Login_page(win)
#     win.mainloop()

# class Login_page:
# def __init__(self, root):
#     self.root = root
#     self.root.title("LOGIN")
#     self.root.geometry("1350x700+0+0")

#     self.bg = ImageTk.PhotoImage(
#         file=r"C:/Users/hp/OneDrive/Desktop/Hotel management system/33.png")
#     lbl_bg = Label(self.root, image=self.bg)
#     lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

#     frame = Frame(self.root, bg="#b3c9ba")
#     frame.place(x=610, y=170, width=1350, height=700)

#     img_path = r"C:/Users/hp/OneDrive/Desktop/Hotel management system/loginicon.jpeg"

# if os.path.exists(img_path):
#     img1 = Image.open(img_path)
#     img1 = img1.resize((1550, 130), Image.Resampling.LANCZOS)
#     self.photoimg1 = ImageTk.PhotoImage(img1)

#     lblimg = Label(self.root, image=self.photoimg1)
#     lblimg.place(x=730, y=170, width=90, height=90)

# else:
#     # Fallback if file not found
#     lblimg = Label(self.root, text="Image not found!",
#                    font=("Arial", 20), fg="red")
#     lblimg.place(x=100, y=100)

#     get_str = Label(frame, text="Get Started", font=(
#         "times new roman", 12, "bold"), fg="#004b23", bg="#b3c9ba", relief=RIDGE)
#     get_str.place(x=95, y=85)

def get_db_connection():
    """Return a new MySQL connection. Caller should close it."""
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        auth_plugin='mysql_native_password'
    )


def hash_password(password: str) -> str:
    """Returns a SHA-256 hex digest of the password (not ideal for production).

    For production use a strong KDF like bcrypt/scrypt/argon2. This is kept
    simple for tutorial purposes to match beginner-friendly videos.
    """
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("")
        self.root.geometry("1350x700+0+0")

    # def __init__(self, root):
    #     self.root = root
    #     root.title('Login System')
    #     root.geometry('420x320+400+200')

        self.bg = ImageTk.PhotoImage(
            file=r"C:/Users/hp/OneDrive/Desktop/Hotel management system/33.png")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="#b3c9ba")
        frame.place(x=610, y=170, width=1350, height=700)

        img_path = r"C:/Users/hp/OneDrive/Desktop/Hotel management system/loginicon.jpeg"

        if os.path.exists(img_path):
            img1 = Image.open(img_path)
            img1 = img1.resize((1550, 130), Image.Resampling.LANCZOS)
            self.photoimg1 = ImageTk.PhotoImage(img1)

            lblimg = Label(self.root, image=self.photoimg1)
            lblimg.place(x=730, y=170, width=90, height=90)

        else:
            # Fallback if file not found
            lblimg = Label(self.root, text="Image not found!",
                           font=("Arial", 20), fg="red")
            lblimg.place(x=100, y=100)

            get_str = Label(frame, text="Get Started", font=(
                "times new roman", 12, "bold"), fg="#004b23", bg="#b3c9ba", relief=RIDGE)
            get_str.place(x=95, y=85)

    def __init__(self, root):
        self.root = root
        root.title('Login System')
        root.geometry('420x320+400+200')

        # Notebook to switch between Login and Register (similar UX to videos)
        self.nb = ttk.Notebook(root)
        self.frame_login = ttk.Frame(self.nb)
        self.frame_register = ttk.Frame(self.nb)
        self.nb.add(self.frame_login, text='Login')
        self.nb.add(self.frame_register, text='Register')
        self.nb.pack(expand=True, fill='both')

        self.build_login()
        self.build_register()

    def build_login(self):
        pad = {'padx': 12, 'pady': 8}
        lbl_title = ttk.Label(self.frame_login, text='Login',
                              font=('Helvetica', 16, 'bold'))
        lbl_title.pack(pady=10)

        frm = ttk.Frame(self.frame_login)
        frm.pack(pady=5)

        ttk.Label(frm, text='Username:').grid(
            row=0, column=0, sticky='w', **pad)
        self.login_username = ttk.Entry(frm, width=30)
        self.login_username.grid(row=0, column=1, **pad)

        ttk.Label(frm, text='Password:').grid(
            row=1, column=0, sticky='w', **pad)
        self.login_password = ttk.Entry(frm, width=30, show='*')
        self.login_password.grid(row=1, column=1, **pad)

        btn_login = ttk.Button(
            self.frame_login, text='Login', command=self.login_user)
        btn_login.pack(pady=12)

    def build_register(self):
        pad = {'padx': 12, 'pady': 6}
        lbl_title = ttk.Label(self.frame_register,
                              text='Register', font=('Helvetica', 16, 'bold'))
        lbl_title.pack(pady=10)

        frm = ttk.Frame(self.frame_register)
        frm.pack(pady=5)

        ttk.Label(frm, text='Full Name:').grid(
            row=0, column=0, sticky='w', **pad)
        self.reg_name = ttk.Entry(frm, width=30)
        self.reg_name.grid(row=0, column=1, **pad)

        ttk.Label(frm, text='Email:').grid(row=1, column=0, sticky='w', **pad)
        self.reg_email = ttk.Entry(frm, width=30)
        self.reg_email.grid(row=1, column=1, **pad)

        ttk.Label(frm, text='Username:').grid(
            row=2, column=0, sticky='w', **pad)
        self.reg_username = ttk.Entry(frm, width=30)
        self.reg_username.grid(row=2, column=1, **pad)

        ttk.Label(frm, text='Password:').grid(
            row=3, column=0, sticky='w', **pad)
        self.reg_password = ttk.Entry(frm, width=30, show='*')
        self.reg_password.grid(row=3, column=1, **pad)

        ttk.Label(frm, text='Confirm Password:').grid(
            row=4, column=0, sticky='w', **pad)
        self.reg_password2 = ttk.Entry(frm, width=30, show='*')
        self.reg_password2.grid(row=4, column=1, **pad)

        btn_register = ttk.Button(
            self.frame_register, text='Create Account', command=self.register_user)
        btn_register.pack(pady=12)

    def login_user(self):
        username = self.login_username.get().strip()
        password = self.login_password.get().strip()

        if not username or not password:
            messagebox.showerror(
                'Error', 'Please enter both username and password')
            return

        hashed = hash_password(password)

        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                'SELECT id, name FROM users WHERE username=%s AND password=%s', (username, hashed))
            result = cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid Username and password")
            else:
                open_main = messagebox.askyesno("YesNot", "Access only admin")
                if open_main > 0:
                    self .new_window = Toplevel(self.root)
                    self.app = HotelManagement(self.new_window)
                else:
                    if not open_main:
                        return

            cursor.close()
            conn.close()

            if result:
                user_id, name = result
                messagebox.showinfo('Success', f'Welcome, {name}!')
                self.open_dashboard(name)
            else:
                messagebox.showerror(
                    'Login Failed', 'Wrong username or password')
        except mysql.connector.Error as err:
            messagebox.showerror(
                'Database Error', f'Error connecting to database:\n{err}')

    def register_user(self):
        name = self.reg_name.get().strip()
        email = self.reg_email.get().strip()
        username = self.reg_username.get().strip()
        pwd = self.reg_password.get().strip()
        pwd2 = self.reg_password2.get().strip()

        if not (name and email and username and pwd and pwd2):
            messagebox.showerror('Error', 'All fields are required')
            return

        if pwd != pwd2:
            messagebox.showerror('Error', 'Passwords do not match')
            return

        hashed = hash_password(pwd)

        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users (name, email, username, password) VALUES (%s, %s, %s, %s)',
                           (name, email, username, hashed))
            conn.commit()
            cursor.close()
            conn.close()
            messagebox.showinfo(
                'Success', 'Account created successfully. You can now login.')

            # clear form
            self.reg_name.delete(0, tk.END)
            self.reg_email.delete(0, tk.END)
            self.reg_username.delete(0, tk.END)
            self.reg_password.delete(0, tk.END)
            self.reg_password2.delete(0, tk.END)

            # switch to login tab
            self.nb.select(self.frame_login)
        except mysql.connector.IntegrityError as ie:
            # duplicate username or email
            messagebox.showerror('Error', f'Duplicate entry: {ie}')
        except mysql.connector.Error as err:
            messagebox.showerror(
                'Database Error', f'Error connecting to database:\n{err}')

    def open_dashboard(self, name):
        dash = tk.Toplevel(self.root)
        dash.title('Dashboard')
        dash.geometry('350x200')
        ttk.Label(dash, text=f'Hello, {name}',
                  font=('Helvetica', 14)).pack(pady=20)
        ttk.Button(dash, text='Logout', command=dash.destroy).pack(pady=10)


if __name__ == '__main__':
    # Quick check: try to connect to DB and create tables if needed
    try:
        conn = mysql.connector.connect(
            host=DB_HOST, user=DB_USER, password=DB_PASSWORD)
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        cur.execute(f"USE {DB_NAME}")
        cur.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(150) UNIQUE NOT NULL,
                username VARCHAR(50) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
        ''')
        cur.close()
        conn.close()
    except mysql.connector.Error as err:
        print('Could not initialize database:', err)

    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
