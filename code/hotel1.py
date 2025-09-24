from tkinter import Tk, Label, RIDGE
from PIL import Image, ImageTk  # pip install pillow


class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        # Load and resize image
        img1 = Image.open(
            r"C:/Users/hp/OneDriv/Desktop/Hotel management system"
        )
        img1 = img1.resize((1550, 140), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        # Place image on label
        lblimg1 = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=0, width=1550, height=140)


if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()
