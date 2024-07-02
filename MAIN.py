from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_recognition
from attendance import Attendance
from Helpdesk import Help
from developer import Developer
from tkinter import messagebox



class Face_recognition_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x630+0+0")
        self.root.title("Face_recognition_systems")
        
        # First Image
        img = Image.open(r"img\1516603302phpz0SEMq.jpeg")
        img = img.resize((500, 170))
        self.photoimg = ImageTk.PhotoImage(img)
        
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=450, height=200)
        
        # Second Image
        img1 = Image.open(r"img\facialrecognition.png")
        img1 = img1.resize((500, 130))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=450, y=0, width=450, height=100)
        
        # Third Image
        img2 = Image.open(r"img\1516603302phpz0SEMq.jpeg")
        img2 = img2.resize((500, 130))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=900, y=0, width=450, height=100)
        
        # Background Image
        img3 = Image.open(r"img\gradient.jpg")
        img3 = img3.resize((1500, 1330))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=100, width=1300, height=510)
        
        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 28, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1270, height=30)
        
        
        #Student Button
        img4 = Image.open(r"img\infrastructure_image1.png")
        img4 = img4.resize((220, 220))
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=80,width=220,height=130)
        
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_1.place(x=100,y=220,width=220,height=30)


       #Detect face
        img5 = Image.open(r"img\Face.jpg")
        img5 = img5.resize((220, 220))
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=390,y=80,width=220,height=130)
        
        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_1.place(x=390,y=220,width=220,height=30)
        
         #Attendance button
        img6 = Image.open(r"img\website-attandence-features-page.png")
        img6 = img6.resize((220, 220))
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=680,y=80,width=220,height=130)
        
        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_1.place(x=680,y=220,width=220,height=30)
        
         #Assisstance button
        img7 = Image.open(r"img\shutterstock_1918663886.png")
        img7 = img7.resize((220, 220))
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=960,y=80,width=220,height=130)
        
        b1_1=Button(bg_img,text="Help desk",cursor="hand2",command=self.help_data,font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_1.place(x=960,y=220,width=220,height=30)
        
        #tRAIN 
        img8 = Image.open(r"img\analyst-working-business-analytics-data-600nw-1857484450.webp")
        img8 = img8.resize((220, 220))
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=100,y=280,width=220,height=130)
        
        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_1.place(x=100,y=420,width=220,height=30)
        
       
       #Photos
        img9 = Image.open(r"img\cam-gallery-logo")
        img9 = img9.resize((220, 220))
        self.photoimg9 = ImageTk.PhotoImage(img9)
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=390,y=280,width=220,height=130)
        
        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_1.place(x=390,y=420,width=220,height=30)

       
       #Developer button
        img10 = Image.open(r"img\AI-in-Web-Development.webp")
        img10 = img10.resize((220, 220))
        self.photoimg10 = ImageTk.PhotoImage(img10)
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=680,y=280,width=220,height=130)
        
        b1_1=Button(bg_img,text="Developer tool",cursor="hand2",command=self.developer_data,font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_1.place(x=680,y=420,width=220,height=30)
        
        #Exit button
        img11 = Image.open(r"img\how-to-install-a-push-to-exit-button-5cdb0c96f0de0fcbfef2c1ca.webp")
        img11 = img11.resize((220, 220))
        self.photoimg11 = ImageTk.PhotoImage(img11)
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.I_Exit)
        b1.place(x=960,y=280,width=220,height=130)
        
        b1_1=Button(bg_img,text="Exit!!",cursor="hand2",command=self.I_Exit,font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_1.place(x=960,y=420,width=220,height=30)




    def open_img(self):
        os.startfile("data")


    def I_Exit(self):
        self.I_Exit=messagebox.askyesno("Face recognition","Are you sure you want to exit?")
        if self.I_Exit >0:
            self.root.destroy()
        else:
            return    



#======Function buttons===========

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)  
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)  
        
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)    
        
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)  
        
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)    
            


if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition_system(root)
    root.mainloop()


