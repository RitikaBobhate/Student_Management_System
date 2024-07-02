from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x630+0+0")
        self.root.title("Student_Management_System")
        
        
        title_lbl = Label(self.root, text="++ TRAIN DATA SET ++", font=("times new roman", 28, "bold"), bg="light blue", fg="purple")
        title_lbl.place(x=0, y=0, width=1270, height=100)
        
        top_img = Image.open(r"img/analyst-working-business-analytics-data-600nw-1857484450.webp")
        top_img = top_img.resize((1270, 300))  
        self.top_photoimg = ImageTk.PhotoImage(top_img)
        
        f_lbl = Label(self.root, image=self.top_photoimg , bg="white", anchor=W)
        f_lbl.place(x=0, y=100, relwidth=1, height=300)
        
        
        
        b1_1=Button(self.root,text="TRAIN DATA BUTTON",command=self.train_classifier,cursor="hand2",font=("times new roman", 20, "bold"), bg="navy blue", fg="white")
        b1_1.place(x=0,y=300,relwidth=1,height=80)
        
        
        
        bottom_img = Image.open(r"img/train_data_ai.webp")
        bottom_img = bottom_img.resize((1270, 300))  
        self.bottom_photoimg = ImageTk.PhotoImage(bottom_img)
        
        f_lbl = Label(self.root, image=self.bottom_photoimg , bg="white", anchor=W)
        f_lbl.place(x=0, y=370, relwidth=1, height=300)
        
        
        
    def train_classifier(self):
        data_dir=("data")    
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L')  #Grey scale
            imgNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imgNp)
            ids.append(id)
            cv2.imshow("Training",imgNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)
        
        #============= Train the classifier and save==========
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")
        

            
            
        
        
        
        
        
if __name__ == "__main__":
        root = Tk()
        obj = Train(root)
        root.mainloop()        