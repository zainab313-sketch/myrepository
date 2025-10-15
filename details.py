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


class RoomDetails:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1042x450+224+202")

     # =================variable=================
        self.var_floor = StringVar()
        self.var_roomno = StringVar()
        self.var_roomtype = StringVar()

    # =================title=================

        lbl_title = Label(self.root, text="ROOM BOOKING DETAILS",  font=(
            "times new roman", 20, "bold"), bg="#b3c9ba", fg="#004b23", bd=0, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1043, height=40)

        # ================logo=================
        img_path = r"C:/Users/hp/Downloads/Hotel management pics/maxwell.png"

        if os.path.exists(img_path):
            img3 = Image.open(img_path)
            img3 = img3.resize((160, 40), Image.Resampling.LANCZOS)
            self.photoimg3 = ImageTk.PhotoImage(img3)

            lblimg = Label(self.root, bd=0, image=self.photoimg3)
            lblimg.place(x=0, y=0, width=160, height=40)

         # ============label_frame=================
            labelframeleft = LabelFrame(self.root, bd=3, relief=RIDGE, text="ADD NEW ROOM", font=(
                "times new roman", 12, "bold"), fg="#004b23", padx=3)
            labelframeleft.place(x=5, y=43, width=480, height=350)

        # ===========left side image=================
        img_path = r"C:/Users/hp/Downloads/Hotel management pics/bed2.png"

        if os.path.exists(img_path):
            img0 = Image.open(img_path)
            img0 = img0.resize((400, 120), Image.Resampling.LANCZOS)
            self.photoimg8 = ImageTk.PhotoImage(img0)

            lblimg = Label(self.root, image=self.photoimg8)
            lblimg.place(x=45, y=68, width=400, height=120)

        # ==============labels and entrys=================
        # floor
        lbl_floor = Label(labelframeleft, text="Floor", font=(
            "times new roman", 11, "bold"), fg="#004b23", padx=2, pady=6)
        lbl_floor.grid(column=0, sticky=W)
        lbl_floor.place(x=50, y=140)

        self.var_floor = StringVar()
        entry_floor = ttk.Entry(labelframeleft, textvariable=self.var_floor, width=20, font=(
            "times new roman", 11, "italic"))
        entry_floor.grid(row=0, column=1, sticky=W)
        entry_floor.place(x=150, y=143)

        # ROOMNO
        lbl_roomno = Label(labelframeleft, text="Room No", font=(
            "times new roman", 11, "bold"), fg="#004b23", padx=2, pady=6)
        lbl_roomno.grid(column=0, sticky=W)
        lbl_roomno.place(x=50, y=170)

        self.var_roomno = StringVar()
        entry_roomno = ttk.Entry(labelframeleft, textvariable=self.var_roomno, width=20, font=(
            "times new roman", 11, "italic"))
        entry_roomno.grid(row=1, column=1, sticky=W)
        entry_roomno.place(x=150, y=175)

        # roomtype
        lbl_roomtype = Label(labelframeleft, text="Room Type", font=(
            "times new roman", 11, "bold"), fg="#004b23", padx=2, pady=6)
        lbl_roomtype.grid(column=0, sticky=W)
        lbl_roomtype.place(x=50, y=200)

        self.var_roomtype = StringVar()
        entry_roomtype = ttk.Entry(labelframeleft, textvariable=self.var_roomtype, width=20, font=(
            "times new roman", 11, "italic"))
        entry_roomtype.grid(row=1, column=1, sticky=W)
        entry_roomtype.place(x=150, y=205)

        # ==============btns================
        # BTNADD
        btn_frame = Frame(labelframeleft, bd=3, relief=RIDGE)
        btn_frame.place(x=45, y=290, width=79, height=36)

        btn_add = Button(btn_frame, text="Add", command=self.add_data, font=(
            "times new roman", 11, "bold"), bg="#b3c9ba", fg="#004b23", width=7)
        btn_add.grid(row=11, column=0, sticky=W)
        btn_add.place(x=0, y=0)

        # UPDATE
        btn_frame = Frame(labelframeleft, bd=3, relief=RIDGE)
        btn_frame.place(x=145, y=290)

        btn_update = Button(btn_frame, text="Update", command=self.update, font=(
            "times new roman", 11, "bold"), bg="#b3c9ba", fg="#004b23", width=7)
        btn_update.grid(row=11, column=0, padx=0)

        # Delete
        btn_frame = Frame(labelframeleft, bd=3, relief=RIDGE)
        btn_frame.place(x=245, y=290)

        btn_delete = Button(btn_frame, text="Delete", command=self.mDelete, font=(
            "times new roman", 11, "bold"), bg="#b3c9ba", fg="#004b23", width=7)
        btn_delete.grid(row=11, column=0, padx=0)

        # RESET
        btn_frame = Frame(labelframeleft, bd=3, relief=RIDGE)
        btn_frame.place(x=345, y=290)

        btn_reset = Button(btn_frame, text="Reset", command=self.reset, font=(
            "times new roman", 11, "bold"), bg="#b3c9ba", fg="#004b23", width=7)
        btn_reset.grid(row=11, column=0, padx=0)

        # =============table frame search/show=========
        Table_frame = LabelFrame(self.root, bd=3, relief=RIDGE, text="SHOW ROOM DETAILS", font=(
            "times new roman", 13, "bold"), fg="#004b23", width=7)
        Table_frame.place(x=500, y=43, width=530, height=350)

        scroll_x = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.room_table = ttk.Treeview(Table_frame, columns=(
            "floor", "roomno", "roomtype"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.xview)

        self.room_table.heading("floor", text="Floor")
        self.room_table.heading("roomno", text="Room No")
        self.room_table.heading("roomtype", text="Room Type")

        self.room_table["show"] = "headings"

        self.room_table.column("floor", width=100)
        self.room_table.column("roomno", width=100)
        self.room_table.column("roomtype", width=100)
        self.room_table.pack(fill=BOTH, expand=1)

        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

     # ==============function declaration=================
    # add data
    def add_data(self):
        if self.var_floor.get() == "" or self.var_roomtype.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="zainaB313@_", database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)", (
                    self.var_floor.get(),
                    self.var_roomno.get(),
                    self.var_roomtype.get(),

                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "New Room Added Successfully", parent=self.root)
            except mysql.connector.Error as err:
                messagebox.showwarning(
                    "Warning", f"Database error: {str(err)}", parent=self.root)

    # ============fetch data==========

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="zainaB313@_", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from details")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
        for i in rows:
            self.room_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # ============get cursor==========
    def get_cursor(self, event=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]

        self.var_floor.set(row[0]),
        self.var_roomno.set(row[1]),
        self.var_roomtype.set(row[2])

# update data

    def update(self):
        if self.var_floor.get() == "":
            messagebox.showerror(
                "Error", "Please enter your RoomNo", parent=self.root)
        else:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="zainaB313@_", database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("""
            UPDATE details 
            SET Floor=%s, RoomType=%s 
            WHERE RoomNo=%s
        """, (
                self.var_floor.get(),
                self.var_roomtype.get(),
                self.var_roomno.get()
            ))

            conn.commit()

            if my_cursor.rowcount > 0:  # ✅ check if any row was updated
                self.fetch_data()
                messagebox.showinfo(
                    "Success", "New Room details have been updated successfully", parent=self.root)
            else:
                messagebox.showwarning(
                    "Warning", "No matching RoomNo found. Nothing was updated.", parent=self.root)

        conn.close()

        # reset

    def reset(self):
        self.var_floor.set(""),
        self.var_roomtype.set(""),
        self.var_roomno.set("")

        # delete
    def mDelete(self):
        mDelete = messagebox.askyesno(
            "Hotel Management System", "Do you want to delete this Room Details")
        if mDelete > 0:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="zainaB313@_", database="management")
            my_cursor = conn.cursor()
            query = "Delete from details WHERE RoomNo=%s"
            value = (self.var_roomno.get(),)
            my_cursor.execute(query, value)
            conn.commit()
            self.fetch_data()
            conn.close()
        else:
            return


if __name__ == "__main__":
    root = Tk()
    obj = RoomDetails(root)
    root.mainloop()
