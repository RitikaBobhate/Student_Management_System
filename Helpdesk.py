from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        # First header image
        img = Image.open(r"img\360_F_527974548_QHcZxnZYAOqew0XOP9uTL4ClfqsbVvMs.jpg")
        img = img.resize((400, 130))
        self.photoimg = ImageTk.PhotoImage(img)

        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=400, height=130)

        # Second header image
        img1 = Image.open(r"img\360_F_527974548_QHcZxnZYAOqew0XOP9uTL4ClfqsbVvMs.jpg")
        img1 = img1.resize((400, 130))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lb2 = Label(self.root, image=self.photoimg1)
        f_lb2.place(x=900, y=0, width=400, height=130)

        # Third header image
        img2 = Image.open(r"img\AI-in-Web-Development.webp")
        img2 = img2.resize((510, 130))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lb3 = Label(self.root, image=self.photoimg2)
        f_lb3.place(x=400, y=0, width=510, height=130)

        # Background image
        bg1 = Image.open(r"img\analyst-working-business-analytics-data-600nw-1857484450.webp")
        bg1 = bg1.resize((1366, 768))
        self.photobg1 = ImageTk.PhotoImage(bg1)

        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1366, height=768)

        # Title section
        title_lb1 = Label(bg_img, text="HELP PANEL", font=("verdana", 30, "bold"), bg="white", fg="dark green")
        title_lb1.place(x=0, y=0, width=1366, height=45)

        # Button image
        std_img_btn = Image.open(r"img\AI-in-Web-Development.webp")
        std_img_btn = std_img_btn.resize((900, 180))
        self.std_img1 = ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img, image=self.std_img1, cursor="hand2")
        std_b1.place(x=250, y=200, width=800, height=180)

    
        std_b1_1 = Button(bg_img, text="Click here!!", cursor="hand2", font=("Ritika Bobhate", 15, "bold"), bg="white", fg="navyblue", command=self.show_details)
        std_b1_1.place(x=250, y=380, width=800, height=45)

    def show_details(self):
   
        details_window = Toplevel(self.root)
        details_window.title("Click here!!")
        details_window.geometry("400x300+500+250")
        
        
        details_frame = Frame(details_window, bg="white")
        details_frame.pack(padx=20, pady=20, fill=BOTH, expand=True)

     
        details_title = Label(details_frame, text="About Me", font=("verdana", 20, "bold"), bg="white", fg="navyblue")
        details_title.pack(pady=10)

        details_text = (
            "Name: Ritika Bobhate\n"
            "College: Vidyalankar Institute of Technology\n"
            "Email: ritika.bobhate@vit.edu.in\n"
            "Phone: 8104202383\n"
        )

        details_label = Label(details_frame, text=details_text, font=("verdana", 12), bg="light blue", fg="black")
        details_label.pack(pady=20)

if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()

