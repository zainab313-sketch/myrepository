from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
import os
import tkinter as tk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1042x450+224+202")

        # ================variable==============
        self.var_ref = StringVar()
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

        self.var_name = StringVar()
        self.var_fathername = StringVar()
        self.var_gender = StringVar()
        self.var_postcode = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_idprooftype = StringVar()
        self.var_idnumber = StringVar()
        self.var_address = StringVar()

        # =================title=================

        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS",  font=(
            "times new roman", 18, "bold"), bg="#b3c9ba", fg="#004b23", bd=0, relief=RIDGE)
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
            labelframeleft = LabelFrame(self.root, bd=3, relief=RIDGE, text="CUSTOMER DETAILS", font=(
                "times new roman", 12, "bold"), fg="#004b23", padx=3)
            labelframeleft.place(x=5, y=43, width=350, height=395)

        # ==============labels and entrys=================
        # cust ref
        lbl_cust_ref = Label(labelframeleft, text="Customer Ref:", font=(
            "times new roman", 11, "bold"), fg="#004b23", padx=1, pady=3)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)

        enty_ref = ttk.Entry(labelframeleft, width=23, textvariable=self.var_ref, state="readonly", font=(
            "times new roman", 11, "italic"))
        enty_ref.grid(row=0, column=1)

        # cust name
        lbl_cust_ref = Label(labelframeleft, text="Name:", font=(
            "times new roman", 11, "bold"), fg="#004b23", padx=1, pady=3)
        lbl_cust_ref.grid(row=1, column=0, sticky=W)

        enty_ref = ttk.Entry(labelframeleft, width=23, textvariable=self.var_name, font=(
            "times new roman", 11, "italic"))
        enty_ref.grid(row=1, column=1)

        # cust fathername
        lbl_cust_ref = Label(labelframeleft, text="Father Name:",  font=(
            "times new roman", 11, "bold"), fg="#004b23", padx=1, pady=3)
        lbl_cust_ref.grid(row=2, column=0, sticky=W)

        enty_ref = ttk.Entry(labelframeleft, width=23, textvariable=self.var_fathername, font=(
            "times new roman", 11, "italic"))
        enty_ref.grid(row=2, column=1)

        # cust gender combobox
        lbl_cust_ref = Label(labelframeleft, text="Gender:", textvariable=self.var_gender, font=(
            "times new roman", 11, "bold"), fg="#004b23", padx=1, pady=3)
        lbl_cust_ref.grid(row=3, column=0, sticky=W)

        combo_gender = ttk.Combobox(labelframeleft, width=21, textvariable=self.var_gender, font=(
            "times new roman", 11, "italic"))
        combo_gender["values"] = ("Male", "Female", "Others")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)

        # cus postcode
        lbl_cust_ref = Label(labelframeleft, text="Postcode:", font=(
            "times new roman", 11, "bold"), fg="#004b23", padx=1, pady=3)
        lbl_cust_ref.grid(row=4, column=0, sticky=W)

        enty_ref = ttk.Entry(labelframeleft, width=23, textvariable=self.var_postcode, font=(
            "times new roman", 11, "italic"))
        enty_ref.grid(row=4, column=1)

        # cust mobile
        lbl_cust_ref = Label(labelframeleft, text="Mobile No.:", font=(
            "times new roman", 11, "bold"), fg="#004b23", padx=1, pady=3)
        lbl_cust_ref.grid(row=5, column=0, sticky=W)

        enty_ref = ttk.Entry(labelframeleft, width=23, textvariable=self.var_mobile, font=(
            "times new roman", 11, "italic"))
        enty_ref.grid(row=5, column=1)

        # Email
        lbl_cust_ref = Label(labelframeleft, text="Email:", font=(
            "times new roman", 11, "bold"), fg="#004b23", padx=1, pady=3)
        lbl_cust_ref.grid(row=6, column=0, sticky=W)

        enty_ref = ttk.Entry(labelframeleft, width=23, textvariable=self.var_email, font=(
            "times new roman", 11, "italic"))
        enty_ref.grid(row=6, column=1)

        # Nationality
        lbl_cust_ref = Label(labelframeleft, text="Nationality:", font=(
            "times new roman", 11, "bold"), fg="#004b23", padx=1, pady=3)
        lbl_cust_ref.grid(row=7, column=0, sticky=W)

        combo_nationality = ttk.Combobox(labelframeleft, width=21,  textvariable=self.var_nationality, font=(
            "times new roman", 11, "italic"))
        combo_nationality["values"] = (
            "Pakistan", "America", "Canada", "India", "UK")
        combo_nationality.current(0)
        combo_nationality.grid(row=7, column=1)

        # idprooftype comboboc
        lbl_cust_ref = Label(labelframeleft, text="Id Proof Type:", font=(
            "times new roman", 11, "bold"), fg="#004b23", padx=1, pady=3)
        lbl_cust_ref.grid(row=8, column=0, sticky=W)

        combo_idprooftype = ttk.Combobox(labelframeleft, width=21, textvariable=self.var_idprooftype, font=(
            "times new roman", 11, "italic"))
        combo_idprooftype["values"] = (
            "CNIC", "Driving Liscence", "Birth Certificate", "Passport")
        combo_idprooftype.current(0)
        combo_idprooftype.grid(row=8, column=1)

        # id number
        lbl_cust_ref = Label(labelframeleft, text="Id Number:",  font=(
            "times new roman", 11, "bold"), fg="#004b23", padx=1, pady=3)
        lbl_cust_ref.grid(row=9, column=0, sticky=W)

        enty_ref = ttk.Entry(labelframeleft, width=23, textvariable=self.var_idnumber, font=(
            "times new roman", 11, "italic"))
        enty_ref.grid(row=9, column=1)

        # address
        lbl_cust_ref = Label(labelframeleft, text="Address:", font=(
            "times new roman", 11, "bold"), fg="#004b23", padx=1, pady=3)
        lbl_cust_ref.grid(row=10, column=0, sticky=W)

        enty_ref = ttk.Entry(labelframeleft, width=23, textvariable=self.var_address,  font=(
            "times new roman", 11, "italic"))
        enty_ref.grid(row=10, column=1)

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

        # =============table frame search/show================
        table_frame = LabelFrame(self.root, bd=3, relief=RIDGE, text="VIEW DEATAILS AND SEARCH SYSTEM", font=(
            "times new roman", 13, "bold"), fg="#004b23", width=7)
        table_frame.place(x=360, y=43, width=680, height=395)

        lbl_searchBy = Label(table_frame, text="Search By:", font=(
            "times new roman", 11, "bold"), bg="#b3c9ba", fg="#004b23", width=8)
        lbl_searchBy.grid(row=0, column=0, sticky=W)

        self.search_var = StringVar()
        combo_search = ttk.Combobox(table_frame, width=20, textvariable=self.search_var, font=(
            "times new roman", 11, "italic"))
        combo_search["values"] = (
            "Mobile", "Ref", "Name")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=5)

        self.txt_search = StringVar()
        txt_search = ttk.Entry(table_frame, width=22, textvariable=self.txt_search, font=(
            "times new roman", 11, "italic"))
        txt_search.grid(row=0, column=2, padx=4)

        # btn_search = Label(table_frame, bd=3, relief=RIDGE)
        # btn_search.place(x=2, y=320, width=160, height=35)

        btn_Search = Button(table_frame, text="Search", command=self.search, font=(
            "times new roman", 10, "bold"), bg="#b3c9ba", fg="#004b23", width=8)
        btn_Search.grid(row=0, column=3, padx=0)

        # btn_show = Label(table_frame, bd=3, relief=RIDGE)
        # btn_show.place(x=82, y=320)

        btn_showall = Button(table_frame, text="Show All", command=self.fetch_data, font=(
            "times new roman", 10, "bold"), bg="#b3c9ba", fg="#004b23", width=8)
        btn_showall.grid(row=0, column=4, padx=1)

        # ============scroll bar=================
        data_table = Frame(table_frame, bd=3, relief=RIDGE)
        data_table.place(x=1, y=50, width=670, height=300)

        scroll_x = ttk.Scrollbar(data_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(data_table, orient=VERTICAL)

        self.Cust_Data = ttk.Treeview(data_table, columns=("ref", "name", "fathername", "gender", "postcode", "mobile",
                                                           "email", "nationality", "idprooftype", "idnumber", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Cust_Data.xview)
        scroll_y.config(command=self.Cust_Data.xview)

        self.Cust_Data.heading("ref", text="Refer No.")
        self.Cust_Data.heading("name", text="Name")
        self.Cust_Data.heading("fathername", text="Father Name")
        self.Cust_Data.heading("gender", text="Gender")
        self.Cust_Data.heading("postcode", text="Postcode")
        self.Cust_Data.heading("mobile", text="Mobile No.")
        self.Cust_Data.heading("email", text="Email")
        self.Cust_Data.heading("nationality", text="Nationality")
        self.Cust_Data.heading("idprooftype", text="Id Proof Type")
        self.Cust_Data.heading("idnumber", text="Id Number")
        self.Cust_Data.heading("address", text="Address")\


        self.Cust_Data["show"] = "headings"

        self.Cust_Data.column("ref", width=100)
        self.Cust_Data.column("name", width=100)
        self.Cust_Data.column("fathername", width=100)
        self.Cust_Data.column("gender", width=100)
        self.Cust_Data.column("postcode", width=100)
        self.Cust_Data.column("mobile", width=100)
        self.Cust_Data.column("email", width=100)
        self.Cust_Data.column("nationality", width=100)
        self.Cust_Data.column("idprooftype", width=100)
        self.Cust_Data.column("idnumber", width=100)
        self.Cust_Data.column("address", width=100)

        self.Cust_Data.pack(fill=BOTH, expand=1)
        self.Cust_Data.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get() == "" or self.var_ref.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="zainaB313@_", database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_ref.get(),
                    self.var_name.get(),
                    self.var_fathername.get(),
                    self.var_gender.get(),
                    self.var_postcode.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_nationality.get(),
                    self.var_idprooftype.get(),
                    self.var_idnumber.get(),
                    self.var_address.get(),

                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Customer has been added", parent=self.root)
            except Exception as es:
                messagebox.showwarning(
                    "Warning", f"Something went wrong:(n{str(es)})")

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="zainaB313@_", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Data.delete(*self.Cust_Data.get_children())
        for i in rows:
            self.Cust_Data.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.Cust_Data.focus()
        content = self.Cust_Data.item(cursor_row)
        row = content["values"]

        self.var_ref.set(row[0]),
        self.var_name.set(row[1]),
        self.var_fathername.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_postcode.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_idprooftype.set(row[8]),
        self.var_idnumber.set(row[9]),
        self.var_address.set(row[10])

    def update(self):
        if self.var_mobile.get() == "":
            messagebox.showerror(
                "Error", "Please enter your Mobile No.", parent=self.root)
        else:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="zainaB313@_", database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("update customer set Name=%s,FatherName=%s,Gender=%s,Postcode=%s,MobileNo=%s,Email=%s,Nationality=%s,IdProofType=%s,IdNumber=%s,Address=%s where Ref=%s", (
                self.var_name.get(),
                self.var_fathername.get(),
                self.var_gender.get(),
                self.var_postcode.get(),
                self.var_mobile.get(),
                self.var_email.get(),
                self.var_nationality.get(),
                self.var_idprooftype.get(),
                self.var_idnumber.get(),
                self.var_address.get(),
                self.var_ref.get()
            ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo(
            "Update", "Customer details has been updated successfully", parent=self.root)

    def mDelete(self):
        mDelete = messagebox.askyesno(
            "Hotel Management System", "Do you want to delete this customer")
        if mDelete > 0:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="zainaB313@_", database="management")
            my_cursor = conn.cursor()
            query = "delete from customer where Ref=%s"
            value = (self.var_ref.get(),)
            my_cursor.execute(query, value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_ref.set(""),
        self.var_name.set(""),
        self.var_fathername.set(""),
        self.var_postcode.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        self.var_idnumber.set(""),
        self.var_address.set("")

        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

    def search(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="zainaB313@_", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer where " +
                          str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        row = my_cursor.fetchall()
        if len(row) != 0:
            self.Cust_Data.delete(*self.Cust_Data.get_children())
            for i in row:
                self.Cust_Data.insert("", END, values=i)
            conn.commit()
        conn.close()


if __name__ == "__main__":
    root = Tk()
    obj = Cust_Win(root)
    root.mainloop()
