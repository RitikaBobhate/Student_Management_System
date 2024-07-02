from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime

class Face_recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x630+0+0")
        self.root.title("Face Detector")
        
        title_lbl = Label(self.root, text="FACE DETECTION :)", font=("times new roman", 28, "bold"), bg="pink", fg="dark red")
        title_lbl.place(x=0, y=0, width=1270, height=60)
        
        # TOP Image
        top_img = Image.open(r"img/360_F_527974548_QHcZxnZYAOqew0XOP9uTL4ClfqsbVvMs.jpg")
        top_img = top_img.resize((650, 700))
        self.top_photoimg = ImageTk.PhotoImage(top_img)
        
        top_lbl = Label(self.root, image=self.top_photoimg)
        top_lbl.place(x=0, y=60, width=630, height=585)
        
        # Bottom Image
        bottom_img = Image.open(r"img/face_recognition_hr_attendance.png")
        bottom_img = bottom_img.resize((650, 700))
        self.bottom_photoimg = ImageTk.PhotoImage(bottom_img)
        
        bottom_lbl = Label(self.root, image=self.bottom_photoimg)
        bottom_lbl.place(x=630, y=60, width=640, height=585)
        
        # Button
        b1_1 = Button(top_lbl, text="FACE DETECTOR BUTTON", cursor="hand2", command=self.face_recog, font=("times new roman", 15, "bold"), bg="red", fg="white")
        b1_1.place(x=330, y=250, width=280, height=50)  
        
    # Attendance Function
    def mark_attendance(self, m, i, r, p):
        file_path = "college.csv"
        try:
            file_exists = os.path.exists(file_path)
            
            if not file_exists:
                print(f"File {file_path} does not exist. It will be created.")
            
            today = datetime.now().strftime("%d/%m/%Y")
            
            with open(file_path, "a+", newline="\n") as f:
                if not file_exists:
                    f.write("Student_ID,Name,Department,Roll_No,Time,Date,Status\n")  
                    
                f.seek(0)
                myDataList = f.readlines()
                name_list = [line.split(",")[0] for line in myDataList if line.split(",")[5] == today]
                print(f"Name list for today ({today}): {name_list}")  

                if m not in name_list:
                    now = datetime.now()
                    d1 = now.strftime("%d/%m/%Y")
                    dtString = now.strftime("%H:%M:%S")
                    f.writelines(f"{m},{i},{r},{p},{dtString},{d1},Present\n")
                    print(f"Attendance marked for {m}, {i}, {r}, {p} at {dtString} on {d1}")
                else:
                    print(f"{m} is already marked present for today.")
            
            
            with open(file_path, "r") as f:
                file_contents = f.readlines()
                print(f"Contents of the file after writing: {file_contents}")

        except Exception as e:
            messagebox.showerror("File Error", f"Could not open or write to file: {e}")
            print(f"File Error: Could not open or write to file: {e}")
    # Face Recognition Function
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []
            
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100 * (1 - predict / 300)))
                
                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="15102004",
                        database="face_recognition"
                    )
                    my_cursor = conn.cursor()
                    my_cursor.execute("SELECT Name FROM student WHERE Student_id=%s", (id,))
                    i = my_cursor.fetchone()
                    i = " ".join(i) if i else "Unknown"
                    
                    my_cursor.execute("SELECT Department FROM student WHERE Student_id=%s", (id,))
                    r = my_cursor.fetchone()
                    r = " ".join(r) if r else "Unknown"
                    
                    my_cursor.execute("SELECT Roll_No FROM student WHERE Student_id=%s", (id,))
                    p = my_cursor.fetchone()
                    p = " ".join(p) if p else "Unknown"
                    
                    my_cursor.execute("SELECT Student_id FROM student WHERE Student_id=%s", (id,))
                    m = my_cursor.fetchone()
                    m = " ".join(m) if m else "Unknown"
                    
                    conn.close()

                    print(f"Fetched data - ID: {id}, Name: {i}, Department: {r}, Roll No: {p}, Student ID: {m}")
                    
                    if confidence > 77:
                        cv2.putText(img, f"Student_Id: {m}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (57, 255, 20), 3)
                        cv2.putText(img, f"Name: {i}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (57, 255, 20), 3)
                        cv2.putText(img, f"Department: {r}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (57, 255, 20), 3)
                        cv2.putText(img, f"Roll_No: {p}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (57, 255, 20), 3)
                        self.mark_attendance(m, i, r, p)
                    else:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                        cv2.putText(img, "Unknown face", (x, y - 20), cv2.FONT_HERSHEY_COMPLEX, 0.8, (57, 255, 20), 3)
                    
                except mysql.connector.Error as db_err:
                    print(f"Database Error: {db_err}")
                except Exception as e:
                    print(f"Error: {e}")
                
                coord = [x, y, w, h]
                
            return coord
        
        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap = cv2.VideoCapture(0)
        
        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to face Detector", img)
            
            if cv2.waitKey(1) == 13:
                break
            
        video_cap.release()
        cv2.destroyAllWindows()
        
if __name__ == "__main__":
        root = Tk()
        obj = Face_recognition(root)
        root.mainloop()         