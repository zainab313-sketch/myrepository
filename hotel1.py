from tkinter import *
from PIL import Image, ImageTk
import os
from customers import Cust_Win
from room import Room_Booking
from details import RoomDetails


class HotelManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1350x700+0+0")

        # ============ist img ===============
        img_path = r"C:/Users/hp/OneDrive/Desktop/Hotel management system/33.png"

        if os.path.exists(img_path):
            img1 = Image.open(img_path)
            img1 = img1.resize((1550, 130), Image.Resampling.LANCZOS)
            self.photoimg1 = ImageTk.PhotoImage(img1)

            lblimg = Label(self.root, image=self.photoimg1)
            lblimg.place(x=0, y=0, width=1550, height=130)
        else:
            # Fallback if file not found
            lblimg = Label(self.root, text="Image not found!",
                           font=("Arial", 20), fg="red")
            lblimg.place(x=100, y=100)

        # ================logo=================
        img_path = r"C:/Users/hp/OneDrive/Desktop/Hotel management system/maxwell.png"

        if os.path.exists(img_path):
            img2 = Image.open(img_path)
            img2 = img2.resize((240, 130), Image.Resampling.LANCZOS)
            self.photoimg2 = ImageTk.PhotoImage(img2)

            lblimg = Label(self.root, image=self.photoimg2)
            lblimg.place(x=0, y=0, width=240, height=130)

        # =================title=================

        lbl_title = Label(self.root, text="HOTEL MANAGEMENT SYSYTEM",  font=(
            "times new roman", 30, "bold"), bg="#b3c9ba", fg="#004b23", bd=5, relief=RIDGE)
        lbl_title.place(x=0, y=130, width=1360, height=50)

        # ==================main frame=================
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=175, width=1550, height=510)

        # ===========menu=================
        lbl_menu = Label(main_frame, text="MENU",  font=(
            "times new roman", 20, "bold"), bg="#b3c9ba", fg="#004b23", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        # ===========btn frame=================
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=33, width=228, height=230)

        cust_btn = Button(btn_frame, text="CUSTOMER", command=self.cust_details, width=22, font=(
            "times new roman", 13, "bold"), bg="#b3c9ba", fg="#004b23", bd=4, relief=RIDGE, cursor="hand1")
        cust_btn.grid(row=0, column=0, pady=1)

        room_btn = Button(btn_frame, text="ROOM", command=self.roombooking, width=22, font=(
            "times new roman", 13, "bold"), bg="#b3c9ba", fg="#004b23", bd=4, relief=RIDGE, cursor="hand1")
        room_btn.grid(row=1, column=0, pady=1)

        details_btn = Button(btn_frame, text="DETAILS", command=self.roomdetails, width=22, font=(
            "times new roman", 13, "bold"), bg="#b3c9ba", fg="#004b23", bd=4, relief=RIDGE, cursor="hand1")
        details_btn.grid(row=2, column=0, pady=1)

        report_btn = Button(btn_frame, text="REPORT", width=22, font=(
            "times new roman", 13, "bold"), bg="#b3c9ba", fg="#004b23", bd=4, relief=RIDGE, cursor="hand1")
        report_btn.grid(row=3, column=0, pady=1)

        logout_btn = Button(btn_frame, text="LOGOUT", command=self.logout, width=22, font=(
            "times new roman", 13, "bold"), bg="#b3c9ba", fg="#004b23", bd=4, relief=RIDGE, cursor="hand1")
        logout_btn.grid(row=4, column=0, pady=1)

        # ============right side image================
        frame_width = 1050
        frame_height = 480

        img3 = Image.open(
            "C:/Users/hp/OneDrive/Desktop/Hotel management system/main1.png")

        img3 = img3.resize((frame_width, frame_height),
                           Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg1 = Label(main_frame, image=self.photoimg3,
                        bd=4, relief=RIDGE)
        lblimg1.place(x=225, y=0, width=frame_width, height=frame_height)

        # ============down img================

        frame_width = 225
        frame_height = 130

        img4 = Image.open(
            "C:/Users/hp/OneDrive/Desktop/Hotel management system/food.jpg")

        img4 = img4.resize((frame_width, frame_height),
                           Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg1 = Label(main_frame, image=self.photoimg4,
                        bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=230, width=frame_width, height=frame_height)

        frame_width = 225
        frame_height = 130

        img5 = Image.open(
            "C:/Users/hp/OneDrive/Desktop/Hotel management system/R.jpg")

        img5 = img5.resize((frame_width, frame_height),
                           Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg1 = Label(main_frame, image=self.photoimg5,
                        bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=350, width=frame_width, height=frame_height)

    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_Win(self.new_window)

    def roombooking(self):
        self.new_window = Toplevel(self.root)
        self.app = Room_Booking(self.new_window)

    def roomdetails(self):
        self.new_window = Toplevel(self.root)
        self.app = RoomDetails(self.new_window)

    def logout(self):
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = HotelManagement(root)
    root.mainloop()
