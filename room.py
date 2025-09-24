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


class Room_Booking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1042x450+224+202")

    # =================variable=================
        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomno = StringVar()
        self.var_meal = StringVar()
        self.var_staydays = StringVar()
        self.var_paidtax = StringVar()
        self.var_subtotal = StringVar()
        self.var_totalcost = StringVar()

    # =================title=================

        lbl_title = Label(self.root, text="ROOM BOOKING DETAILS",  font=(
            "times new roman", 20, "bold"), bg="#b3c9ba", fg="#004b23", bd=0, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1043, height=40)

        # ================logo=================
        img_path = r"C:/Users/hp/OneDrive/Desktop/Hotel management system/maxwell.png"

        if os.path.exists(img_path):
            img3 = Image.open(img_path)
            img3 = img3.resize((160, 40), Image.Resampling.LANCZOS)
            self.photoimg3 = ImageTk.PhotoImage(img3)

            lblimg = Label(self.root, bd=0, image=self.photoimg3)
            lblimg.place(x=0, y=0, width=160, height=40)

         # ============label_frame=================
            labelframeleft = LabelFrame(self.root, bd=3, relief=RIDGE, text="BOOKING DETAILS", font=(
                "times new roman", 12, "bold"), fg="#004b23", padx=3)
            labelframeleft.place(x=5, y=43, width=350, height=395)

        # ==============labels and entrys=================
        # customer contact
        contact = Label(labelframeleft, text="Contact:", font=(
            "times new roman", 11, "bold"), fg="#004b23", padx=1, pady=3)
        contact.grid(row=0, column=0, sticky=W)

        entry_contact = ttk.Entry(labelframeleft, width=16, textvariable=self.var_contact, font=(
            "times new roman", 11, "italic"))
        entry_contact.grid(row=0, column=1, padx=0, sticky=W)
        # fetch data button
        btn_fetch = Button(labelframeleft, command=self.fetch_details, text="Fetch Data",  font=(
            "times new roman", 8, "bold"), bg="#b3c9ba", fg="#004b23", width=9)
        btn_fetch.place(x=255, y=2)
        # checkindate
        check_in_date = Label(labelframeleft, text="Check in date:", font=(
            "times new roman", 11, "bold"), fg="#004b23", padx=1, pady=3)
        check_in_date.grid(row=1, column=0, sticky=W)

        entry_checkin = ttk.Entry(labelframeleft, width=26, textvariable=self.var_checkin,  font=(
            "times new roman", 11, "italic"))
        entry_checkin.grid(row=1, column=1)
        # checkoutdate
        check_out_date = Label(labelframeleft, text="Check out date:", font=(
            "times new roman", 11, "bold"), fg="#004b23", padx=1, pady=3)
        check_out_date.grid(row=2, column=0, sticky=W)

        entry_checkout = ttk.Entry(labelframeleft, width=26, textvariable=self.var_checkout, font=(
            "times new roman", 11, "italic"))
        entry_checkout.grid(row=2, column=1)
        # room type
        room_type = Label(labelframeleft, text="Room Type:", font=(
            "times new roman", 11, "bold"), fg="#004b23", padx=1, pady=3)
        room_type.grid(row=3, column=0, sticky=W)

        conn = mysql.connector.connect(
            host="localhost", username="root", password="zainaB313@_", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomType from details")
        ide = my_cursor.fetchall()

        combo_type = ttk.Combobox(labelframeleft, width=24, textvariable=self.var_roomtype, font=(
            "times new roman", 11, "italic"))
        combo_type["values"] = ide
        combo_type.current(0)
        combo_type.grid(row=3, column=1)

        # room available
        room_available = Label(labelframeleft, text="Room:", font=(
            "times new roman", 11, "bold"), fg="#004b23", padx=1, pady=3)
        room_available.grid(row=4, column=0, sticky=W)

        conn = mysql.connector.connect(
            host="localhost", username="root", password="zainaB313@_", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows = my_cursor.fetchall()

        combo_no = ttk.Combobox(labelframeleft, width=24, textvariable=self.var_roomno, font=(
            "times new roman", 11, "italic"))
        combo_no["values"] = rows
        combo_no.current(0)
        combo_no.grid(row=4, column=1)
        # entry_available = ttk.Entry(labelframeleft, width=26, textvariable=self.var_roomno, font=(
        #     "times new roman", 11, "italic"))
        # entry_available.grid(row=4, column=1)
        # meal
        meal_no = Label(labelframeleft, text="Meal:", font=(
            "times new roman", 11, "bold"), fg="#004b23", padx=1, pady=3)
        meal_no.grid(row=5, column=0, sticky=W)

        entry_meal = ttk.Entry(labelframeleft, width=26, textvariable=self.var_meal, font=(
            "times new roman", 11, "italic"))
        entry_meal.grid(row=5, column=1)
        # stay days
        stay_days = Label(labelframeleft, text="Stay Days:", font=(
            "times new roman", 11, "bold"), fg="#004b23", padx=1, pady=3)
        stay_days.grid(row=6, column=0, sticky=W)

        entry_days = ttk.Entry(labelframeleft, width=26, textvariable=self.var_staydays, font=(
            "times new roman", 11, "italic"))
        entry_days.grid(row=6, column=1)
        # paid tax
        paid_tax = Label(labelframeleft, text="Paid Tax:", font=(
            "times new roman", 11, "bold"), fg="#004b23", padx=1, pady=3)
        paid_tax.grid(row=7, column=0, sticky=W)

        entry_tax = ttk.Entry(labelframeleft, textvariable=self.var_paidtax, width=26, font=(
            "times new roman", 11, "italic"))
        entry_tax.grid(row=7, column=1)
        # sub total
        sub_total = Label(labelframeleft, text="Sub Total:", font=(
            "times new roman", 11, "bold"), fg="#004b23", padx=1, pady=3)
        sub_total.grid(row=8, column=0, sticky=W)

        entry_total = ttk.Entry(labelframeleft, textvariable=self.var_subtotal, width=26, font=(
            "times new roman", 11, "italic"))
        entry_total.grid(row=8, column=1)
        # total cost
        total_cost = Label(labelframeleft, text="Total Cost:", font=(
            "times new roman", 11, "bold"), fg="#004b23", padx=1, pady=3)
        total_cost.grid(row=9, column=0, sticky=W)

        entry_cost = ttk.Entry(labelframeleft, textvariable=self.var_totalcost, width=26, font=(
            "times new roman", 11, "italic"))
        entry_cost.grid(row=9, column=1)

    #  ===========bill button==========
        btn_frame = Frame(labelframeleft, bd=1, relief=RIDGE)
        btn_frame.place(x=2, y=270, width=75, height=33)

        btn_reset = Button(btn_frame, text="Bill", command=self.total, font=(
            "times new roman", 11, "bold"), bg="#b3c9ba", fg="#004b23", width=7)
        btn_reset.grid(row=10, column=0)

     # ==============btns=================
        btn_frame = Frame(labelframeleft, bd=3, relief=RIDGE)
        btn_frame.place(x=4, y=320, width=79, height=36)

        btn_add = Button(btn_frame, text="Add", command=self.add_data,  font=(
            "times new roman", 11, "bold"), bg="#b3c9ba", fg="#004b23", width=7)
        btn_add.grid(row=11, column=0, padx=0)

        btn_frame = Frame(labelframeleft, bd=3, relief=RIDGE)
        btn_frame.place(x=85, y=320)

        btn_update = Button(btn_frame, text="Update", command=self.update, font=(
            "times new roman", 11, "bold"), bg="#b3c9ba", fg="#004b23", width=7)
        btn_update.grid(row=11, column=0, padx=0)

        btn_frame = Frame(labelframeleft, bd=3, relief=RIDGE)
        btn_frame.place(x=166, y=320)

        btn_delete = Button(btn_frame, text="Delete", command=self.mDelete, font=(
            "times new roman", 11, "bold"), bg="#b3c9ba", fg="#004b23", width=7)
        btn_delete.grid(row=11, column=0, padx=0)

        btn_frame = Frame(labelframeleft, bd=3, relief=RIDGE)
        btn_frame.place(x=250, y=320)

        btn_reset = Button(btn_frame, text="Reset", command=self.reset, font=(
            "times new roman", 11, "bold"), bg="#b3c9ba", fg="#004b23", width=7)
        btn_reset.grid(row=11, column=0, padx=0)

    # ===========right side image=================
        img_path = r"C:/Users/hp/OneDrive/Desktop/Hotel management system/bed3.png"

        if os.path.exists(img_path):
            img8 = Image.open(img_path)
            img8 = img8.resize((330, 200), Image.Resampling.LANCZOS)
            self.photoimg8 = ImageTk.PhotoImage(img8)

            lblimg = Label(self.root, image=self.photoimg8)
            lblimg.place(x=690, y=40, width=330, height=230)

    # =============table frame search/show=========
        table_frame = LabelFrame(self.root, bd=3, relief=RIDGE, text="VIEW DEATAILS AND SEARCH SYSTEM", font=(
            "times new roman", 13, "bold"), fg="#004b23", width=7)
        table_frame.place(x=360, y=238, width=680, height=200)

        lbl_searchBy = Label(table_frame, text="Search By:", font=(
            "times new roman", 11, "bold"), bg="#b3c9ba", fg="#004b23", width=8)
        lbl_searchBy.grid(row=0, column=0, sticky=W)

        self.search_var = StringVar()
        combo_search = ttk.Combobox(table_frame, width=20, textvariable=self.search_var, font=(
            "times new roman", 11, "italic"))
        combo_search["values"] = (
            "Contact", "Room", "Check_in")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=5)

        self.txt_search = StringVar()
        txt_search = ttk.Entry(table_frame, width=22, textvariable=self.txt_search, font=(
            "times new roman", 11, "italic"))
        txt_search.grid(row=0, column=2, padx=4)

        btn_Search = Button(table_frame, text="Search", command=self.search, font=(
            "times new roman", 10, "bold"), bg="#b3c9ba", fg="#004b23", width=8)
        btn_Search.grid(row=0, column=3, padx=0)

        btn_showall = Button(table_frame, text="Show All", command=self.fetch_data, font=(
            "times new roman", 10, "bold"), bg="#b3c9ba", fg="#004b23", width=8)
        btn_showall.grid(row=0, column=4, padx=1)

        # ============scroll bar=================
        data_table = Frame(table_frame, bd=3, relief=RIDGE)
        data_table.place(x=1, y=36, width=670, height=140)

        scroll_x = ttk.Scrollbar(data_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(data_table, orient=VERTICAL)

        self.room_table = ttk.Treeview(data_table, columns=("contact", "checkindate", "checkoutdate", "roomtype", "roomno", "meal",
                                                            "staydays"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.xview)

        self.room_table.heading("contact", text="Contact")
        self.room_table.heading("checkindate", text="Check in date")
        self.room_table.heading("checkoutdate", text=" Check out date")
        self.room_table.heading("roomtype", text="Room Type")
        self.room_table.heading("roomno", text="Room No")
        self.room_table.heading("meal", text="Meal")
        self.room_table.heading("staydays", text="Stay Days")

        self.room_table["show"] = "headings"

        self.room_table.column("contact", width=100)
        self.room_table.column("checkindate", width=100)
        self.room_table.column("checkoutdate", width=100)
        self.room_table.column("roomtype", width=100)
        self.room_table.column("roomno", width=100)
        self.room_table.column("meal", width=100)
        self.room_table.column("staydays", width=100)

        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()

    # ==============function declaration=================
    # add data
    def add_data(self):
        if self.var_contact.get() == "" or self.var_checkin.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="zainaB313@_", database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_contact.get(),
                    self.var_checkin.get(),
                    self.var_checkout.get(),
                    self.var_roomtype.get(),
                    self.var_roomno.get(),
                    self.var_meal.get(),
                    self.var_staydays.get()

                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Room Booked", parent=self.root)
            except mysql.connector.Error as err:
                messagebox.showwarning(
                    "Warning", f"Database error: {str(err)}", parent=self.root)

# ============fetch data==========

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="zainaB313@_", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room")
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

        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomno.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_staydays.set(row[6])

    # update data

    def update(self):
        if self.var_contact.get() == "":
            messagebox.showerror(
                "Error", "Please enter your Contact", parent=self.root)
        else:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="zainaB313@_", database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("""
            UPDATE room 
            SET CheckInDate=%s, CheckOutDate=%s, RoomType=%s, Room=%s, Meal=%s, StayDays=%s 
            WHERE Contact=%s
        """, (
                self.var_checkin.get(),
                self.var_checkout.get(),
                self.var_roomtype.get(),
                self.var_roomno.get(),
                self.var_meal.get(),
                self.var_staydays.get(),
                self.var_contact.get()
            ))

            conn.commit()

            if my_cursor.rowcount > 0:  # ✅ check if any row was updated
                self.fetch_data()
                messagebox.showinfo(
                    "Success", "Room details have been updated successfully", parent=self.root)
            else:
                messagebox.showwarning(
                    "Warning", "No matching contact found. Nothing was updated.", parent=self.root)

        conn.close()

        # except Exception as e:
        #     messagebox.showerror("Error", f"Due to{str(e)}")

    # reset

    def reset(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_roomno.set(""),
        self.var_meal.set(""),
        self.var_staydays.set(""),
        self.var_paidtax.set(""),
        self.var_subtotal.set(""),
        self.var_totalcost.set("")

    # delete
    def mDelete(self):
        mDelete = messagebox.askyesno(
            "Hotel Management System", "Do you want to delete this Room")
        if mDelete > 0:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="zainaB313@_", database="management")
            my_cursor = conn.cursor()
            query = "Delete from room WHERE Contact=%s"
            value = (self.var_checkin.get(),)
            my_cursor.execute(query, value)
            conn.commit()
            self.fetch_data()
            conn.close()
        else:
            return

  #   search sys

    def search(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="zainaB313@_", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from Room where " +
                          str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        row = my_cursor.fetchall()
        if len(row) != 0:
            self.room_table.delete(*self.room_table.get_children())
        for i in row:
            self.room_table.insert("", "end", values=i)
        conn.commit()
        conn.close()

    # ==============all data============

    def fetch_details(self):
        if self.var_contact.get() == "":
            messagebox.showerror(
                "Error", "Please enter contact number", parent=self.root)
        else:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="zainaB313@_", database="management")
            my_cursor = conn.cursor()
            query = ("select Name from customer where MobileNo=%s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror(
                    "Error", "This number not found", parent=self.root)
            else:
                conn.commit()
                conn.close()

                showdataframe = Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showdataframe.place(x=360, y=53, width=250, height=178)

                lblName = Label(showdataframe, text="Name:",
                                font=("italic", 11, "bold"))
                lblName.place(x=0, y=0)

                lbl = Label(showdataframe, text=row, font=("italic", 11))
                lbl.place(x=90, y=0)
    # ============Gender=================
            conn = mysql.connector.connect(
                host="localhost", username="root", password="zainaB313@_", database="management")
            my_cursor = conn.cursor()
            query = ("select Gender from customer where MobileNo=%s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            lblGender = Label(showdataframe, text="Gender:",
                              font=("italic", 11, "bold"))
            lblGender.place(x=0, y=30)

            lbl2 = Label(showdataframe, text=row, font=("italic", 11))
            lbl2.place(x=90, y=30)

    # ============Email=================
            conn = mysql.connector.connect(
                host="localhost", username="root", password="zainaB313@_", database="management")
            my_cursor = conn.cursor()
            query = ("select Email from customer where MobileNo=%s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            lblEmail = Label(showdataframe, text="Email:",
                             font=("italic", 11, "bold"))
            lblEmail.place(x=0, y=60)

            lbl3 = Label(showdataframe, text=row, font=("italic", 11))
            lbl3.place(x=90, y=60)

    # ============Nationality=================
            conn = mysql.connector.connect(
                host="localhost", username="root", password="zainaB313@_", database="management")
            my_cursor = conn.cursor()
            query = ("select Nationality from customer where MobileNo=%s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            lblNationality = Label(showdataframe, text="Nationality:",
                                   font=("italic", 11, "bold"))
            lblNationality.place(x=0, y=90)

            lbl4 = Label(showdataframe, text=row, font=("italic", 11))
            lbl4.place(x=90, y=90)

    # ============Address=================
            conn = mysql.connector.connect(
                host="localhost", username="root", password="zainaB313@_", database="management")
            my_cursor = conn.cursor()
            query = ("select Address from customer where MobileNo=%s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            lblAddress = Label(showdataframe, text="Address:",
                               font=("italic", 11, "bold"))
            lblAddress.place(x=0, y=120)

            lbl5 = Label(showdataframe, text=row, font=("italic", 11))
            lbl5.place(x=90, y=120)

    # total billing

    def total(self):
        inDate = datetime.strptime(self.var_checkin.get(), "%d/%m/%Y")
        outDate = datetime.strptime(self.var_checkout.get(), "%d/%m/%Y")
        self.var_staydays.set(abs(outDate - inDate).days)

        if (self.var_meal.get() == "Breakfast" and self.var_roomtype.get() == "Luxury"):
            q1 = 300
            q2 = 60000
            q3 = float(self.var_staydays.get())
            q4 = q1 + q2
            q5 = q3 * q4

            self.var_paidtax.set("Rs." + str("%.2f" % (q5 * 0.09)))
            self.var_subtotal.set("Rs." + str("%.2f" % q5))
            self.var_totalcost.set("Rs." + str("%.2f" % (q5 + (q5 * 0.09))))

        elif (self.var_meal.get() == "Breakfast" and self.var_roomtype.get() == "Single"):
            q1 = 300
            q2 = 30000
            q3 = float(self.var_staydays.get())
            q4 = q1 + q2
            q5 = q3 * q4

            self.var_paidtax.set("Rs." + str("%.2f" % (q5 * 0.09)))
            self.var_subtotal.set("Rs." + str("%.2f" % q5))
            self.var_totalcost.set("Rs." + str("%.2f" % (q5 + (q5 * 0.09))))

        elif (self.var_meal.get() == "Breakfast" and self.var_roomtype.get() == "Double"):
            q1 = 500
            q2 = 55000
            q3 = float(self.var_staydays.get())
            q4 = q1 + q2
            q5 = q3 * q4

            self.var_paidtax.set("Rs." + str("%.2f" % (q5 * 0.09)))
            self.var_subtotal.set("Rs." + str("%.2f" % q5))
            self.var_totalcost.set("Rs." + str("%.2f" % (q5 + (q5 * 0.09))))

        elif (self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Single"):
            q1 = 500
            q2 = 30000
            q3 = float(self.var_staydays.get())
            q4 = q1 + q2
            q5 = q3 * q4

            self.var_paidtax.set("Rs." + str("%.2f" % (q5 * 0.09)))
            self.var_subtotal.set("Rs." + str("%.2f" % q5))
            self.var_totalcost.set("Rs." + str("%.2f" % (q5 + (q5 * 0.09))))

        elif (self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Double"):
            q1 = 600
            q2 = 55000
            q3 = float(self.var_staydays.get())
            q4 = q1 + q2
            q5 = q3 * q4

            self.var_paidtax.set("Rs." + str("%.2f" % (q5 * 0.09)))
            self.var_subtotal.set("Rs." + str("%.2f" % q5))
            self.var_totalcost.set("Rs." + str("%.2f" % (q5 + (q5 * 0.09))))

        elif (self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Luxury"):
            q1 = 600
            q2 = 60000
            q3 = float(self.var_staydays.get())
            q4 = q1 + q2
            q5 = q3 * q4

            self.var_paidtax.set("Rs." + str("%.2f" % (q5 * 0.09)))
            self.var_subtotal.set("Rs." + str("%.2f" % q5))
            self.var_totalcost.set("Rs." + str("%.2f" % (q5 + (q5 * 0.09))))

        elif (self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Single"):
            q1 = 700
            q2 = 30000
            q3 = float(self.var_staydays.get())
            q4 = q1 + q2
            q5 = q3 * q4

            self.var_paidtax.set("Rs." + str("%.2f" % (q5 * 0.09)))
            self.var_subtotal.set("Rs." + str("%.2f" % q5))
            self.var_totalcost.set("Rs." + str("%.2f" % (q5 + (q5 * 0.09))))

        elif (self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Double"):
            q1 = 700
            q2 = 55000
            q3 = float(self.var_staydays.get())
            q4 = q1 + q2
            q5 = q3 * q4

            self.var_paidtax.set("Rs." + str("%.2f" % (q5 * 0.09)))
            self.var_subtotal.set("Rs." + str("%.2f" % q5))
            self.var_totalcost.set("Rs." + str("%.2f" % (q5 + (q5 * 0.09))))

        elif (self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Luxury"):
            q1 = 700
            q2 = 60000
            q3 = float(self.var_staydays.get())
            q4 = q1 + q2
            q5 = q3 * q4

            self.var_paidtax.set("Rs." + str("%.2f" % (q5 * 0.09)))
            self.var_subtotal.set("Rs." + str("%.2f" % q5))
            self.var_totalcost.set("Rs." + str("%.2f" % (q5 + (q5 * 0.09))))


if __name__ == "__main__":
    root = Tk()
    obj = Room_Booking(root)
    root.mainloop()
