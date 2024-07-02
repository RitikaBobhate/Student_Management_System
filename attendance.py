from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os
import csv
import numpy as np
from tkinter import filedialog
from tkinter import messagebox


mydata = []

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x630+0+0")
        self.root.title("Student Management System")
        
        #-----------Variables-------------------
        self.var_id=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attend=StringVar()
        
        # First Image
        img = Image.open(r"img\1516603302phpz0SEMq.jpeg")
        img = img.resize((500, 130))
        self.photoimg = ImageTk.PhotoImage(img)
        
        f_lbl = Label(self.root, image=self.photoimg, bg="white")
        f_lbl.place(x=0, y=0, width=450, height=100)
        
        # Second Image
        img1 = Image.open(r"img\facialrecognition.png")
        img1 = img1.resize((500, 130))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f_lbl = Label(self.root, image=self.photoimg1, bg="white")
        f_lbl.place(x=450, y=0, width=450, height=100)
        
        # Third Image
        img2 = Image.open(r"img\1516603302phpz0SEMq.jpeg")
        img2 = img2.resize((500, 130))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        f_lbl = Label(self.root, image=self.photoimg2, bg="white")
        f_lbl.place(x=900, y=0, width=450, height=100)
        
        # Background Image
        img3 = Image.open(r"img\website-background-templates.png")
        img3 = img3.resize((1500, 1330))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=100, width=1300, height=610)
        
        title_lbl = Label(bg_img, text="ATTENDANCE SYSTEM", font=("times new roman", 28, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1270, height=30)
        
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=45, width=1235, height=490)
        
        # Left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="STUDENT ATTENDANCE DETAILS", font=("times new roman", 12, "bold"), fg="maroon")
        Left_frame.place(x=10, y=10, width=580, height=470)
        
        left_img = Image.open(r"img\Student.webp")
        left_img = left_img.resize((560, 200))  
        self.left_photoimg = ImageTk.PhotoImage(left_img)

        f_lbl = Label(Left_frame, image=self.left_photoimg, bg="white", anchor=W)
        f_lbl.place(x=10, y=0, width=560, height=150)
        
        left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=10, y=150, width=560, height=290)
        
        # Attendance ID
        Attendance_label = Label(left_inside_frame, text="Attendance ID:", font=("times new roman", 12, "bold"), bg="white")
        Attendance_label.grid(row=0, column=0, padx=3, pady=15, sticky=W)
        self.Attendance_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_id, font=("times new roman", 12, "bold"))
        self.Attendance_entry.grid(row=0, column=1, padx=3, pady=15, sticky=W)
        
        # Name
        Name_label = Label(left_inside_frame, text="Name:", font=("times new roman", 12, "bold"), bg="white")
        Name_label.grid(row=0, column=2, padx=3, pady=15, sticky=W)
        self.Name_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_name, font=("times new roman", 12, "bold"))
        self.Name_entry.grid(row=0, column=3, padx=3, pady=15, sticky=W)
        
        # Department
        Department_label = Label(left_inside_frame, text="Department:", font=("times new roman", 12, "bold"), bg="white")
        Department_label.grid(row=1, column=0, padx=3, pady=15, sticky=W)
        self.Department_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_dep, font=("times new roman", 12, "bold"))
        self.Department_entry.grid(row=1, column=1, padx=3, pady=15, sticky=W)
        
        # Date
        Date_label = Label(left_inside_frame, text="Date:", font=("times new roman", 12, "bold"), bg="white")
        Date_label.grid(row=1, column=2, padx=3, pady=15, sticky=W)
        self.Date_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_date,font=("times new roman", 12, "bold"))
        self.Date_entry.grid(row=1, column=3, padx=3, pady=15, sticky=W)
        
        # Time
        Time_label = Label(left_inside_frame, text="Time:", font=("times new roman", 12, "bold"), bg="white")
        Time_label.grid(row=2, column=2, padx=3, pady=15, sticky=W)
        self.Time_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_time, font=("times new roman", 12, "bold"))
        self.Time_entry.grid(row=2, column=3, padx=3, pady=15, sticky=W)
        
        # Attendance
        Attendance_label = Label(left_inside_frame, text="Attendance Status:", font=("times new roman", 12, "bold"), bg="white")
        Attendance_label.grid(row=2, column=0, padx=3, pady=15, sticky=W)
        
        self.atten_status = ttk.Combobox(left_inside_frame,font=("times new roman", 12, "bold"), state="readonly", width=10,textvariable=self.var_attend)
        self.atten_status["values"] = ("Status","Male","Present","Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=2, column=1, padx=3, pady=15, sticky=W)
        
        # Button
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=3,y=230,width=550,height=45)
        
        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=12,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0,padx=1)
        
        update_btn=Button(btn_frame,text="Export csv",width=13,command=self.exportCsv,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1,padx=1)
        
        delete_btn=Button(btn_frame,text="Update",width=13,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2,padx=1)
        
        reset_btn=Button(btn_frame,text="Reset",width=12,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3,padx=1)
        
        # Right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="STUDENT ATTENDANCE DETAILS", font=("times new roman", 12, "bold"), fg="maroon")
        Right_frame.place(x=600, y=10, width=620, height=470)
        
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=3,y=1,width=610,height=440)
        
        # Scroll Bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=('id',"name","department","roll","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance Status")
        
        self.AttendanceReportTable["show"] = "headings"
        
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor) 
        
    # Fetch data
    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)
    
    # Import CSV
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        
        if fln:
            print(f"Selected file: {fln}")  
            try:
                with open(fln, newline='') as myfile:
                    csvread = csv.reader(myfile, delimiter=",")
                    for i in csvread:
                        mydata.append(i)
                self.fetchData(mydata)
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("No file selected")
            
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data Found!",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Successfuly","Export Data Successfully!")
        except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)    
                
                
    def get_cursor(self,event=""):
        cursor_focus = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_focus)
        data = content["values"]

        self.var_id.set(data[0]),
        self.var_name.set(data[1]),
        self.var_dep.set(data[2]),
        self.var_date.set(data[5]),
        self.var_time.set(data[4]),
        self.var_attend.set(data[6])           
        
        
                
                    
        
if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
