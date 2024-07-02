from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x630+0+0")
        self.root.title("Student_Management_System")
        
        #======================variables================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_stu_id=StringVar()
        self.var_stu_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

        
        
       # First Image
        img = Image.open(r"img\1516603302phpz0SEMq.jpeg")
        img = img.resize((500, 130))
        self.photoimg = ImageTk.PhotoImage(img)
        
        f_lbl = Label(self.root, image=self.photoimg, bg="white")  # Set bg="white"
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
        
        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 28, "bold"), bg="white", fg="RED")
        title_lbl.place(x=0, y=0, width=1270, height=30)
        
        
        main_frame= Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=45,width=1235,height=490)
        
        # Left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="STUDENT DETAILS", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=580, height=470)

        # Left Image
        left_img = Image.open(r"img\Students-in-Cap-and-Gown-for-College-Success.jpeg")
        left_img = left_img.resize((560, 100))  
        self.left_photoimg = ImageTk.PhotoImage(left_img)

        f_lbl = Label(Left_frame, image=self.left_photoimg, bg="white", anchor=W)
        f_lbl.place(x=0, y=0, relwidth=1, height=100)  

        
        
        #Current Course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Details",font=("times new roman",12,"bold"))
        current_course_frame.place(x=10,y=110,width=560,height=110)
        

        
                # Department
        dep_label = Label(current_course_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        dept_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep, font=("times new roman", 12, "bold"), state="readonly", width=17)
        dept_combo["values"] = ("Select Department", "Computer Science", "IT", "EXCS", "EXTC", "BIOMED")
        dept_combo.current(0)
        dept_combo.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        # Course
        course_label = Label(current_course_frame, text="Course", font=("times new roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, pady=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course, font=("times new roman", 12, "bold"), state="readonly", width=17)
        course_combo["values"] = ("Select course", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=10, pady=10, sticky=W)

        # Year
        Year_label = Label(current_course_frame, text="Year", font=("times new roman", 12, "bold"), bg="white")
        Year_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        Year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year,font=("times new roman", 12, "bold"), state="readonly", width=17)
        Year_combo["values"] = ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24","2024-2025")
        Year_combo.current(0)
        Year_combo.grid(row=1, column=1, padx=10, pady=10, sticky=W)
        
        # Semester
        Semester_label = Label(current_course_frame, text="Semester", font=("times new roman", 12, "bold"), bg="white")
        Semester_label.grid(row=1, column=2, padx=10, pady=10, sticky=W)

        Semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_sem,font=("times new roman", 12, "bold"), state="readonly", width=17)
        Semester_combo["values"] = ("Select Semester", "Sem-1", "Sem-2", "Sem-3","Sem-4","Sem-5","Sem-6","Sem-7","Sem-8")
        Semester_combo.current(0)
        Semester_combo.grid(row=1, column=3, padx=10, pady=10, sticky=W)
        
        
        # Class Student Information
        Class_Student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Student Information", font=("times new roman", 10, "bold"))
        Class_Student_frame.place(x=10, y=220, width=560, height=220)

        # Student ID
        StudentId_label = Label(Class_Student_frame, text="Student ID:", font=("times new roman", 10, "bold"), bg="white")
        StudentId_label.grid(row=0, column=0, padx=1, pady=3, sticky=W)

        StudentId_entry = ttk.Entry(Class_Student_frame,textvariable=self.var_stu_id, width=20, font=("times new roman", 10, "bold"))
        StudentId_entry.grid(row=0, column=1, padx=1, pady=3, sticky=W)

        # Student Name
        Studentname_label = Label(Class_Student_frame, text="Student Name:", font=("times new roman", 10, "bold"), bg="white")
        Studentname_label.grid(row=0, column=2, padx=1, pady=3, sticky=W)

        Studentname_entry = ttk.Entry(Class_Student_frame,textvariable=self.var_stu_name, width=20, font=("times new roman", 10, "bold"))
        Studentname_entry.grid(row=0, column=3, padx=1, pady=3, sticky=W)

        # Class Division
        Class_Division_label = Label(Class_Student_frame, text="Class Division:", font=("times new roman", 10, "bold"), bg="white")
        Class_Division_label.grid(row=1, column=0, padx=1, pady=3, sticky=W)

        Class_Division_entry = ttk.Entry(Class_Student_frame,textvariable=self.var_div, width=20, font=("times new roman", 10, "bold"))
        Class_Division_entry.grid(row=1, column=1, padx=1, pady=3, sticky=W)

        # Roll No
        Roll_label = Label(Class_Student_frame, text="Roll No:", font=("times new roman", 10, "bold"), bg="white")
        Roll_label.grid(row=1, column=2, padx=1, pady=3, sticky=W)

        Roll_entry = ttk.Entry(Class_Student_frame, textvariable=self.var_roll,width=20, font=("times new roman", 10, "bold"))
        Roll_entry.grid(row=1, column=3, padx=1, pady=3, sticky=W)

        # Email
        Email_label = Label(Class_Student_frame, text="Email:", font=("times new roman", 10, "bold"), bg="white")
        Email_label.grid(row=2, column=0, padx=1, pady=3, sticky=W)

        Email_entry = ttk.Entry(Class_Student_frame, textvariable=self.var_email,width=20, font=("times new roman", 10, "bold"))
        Email_entry.grid(row=2, column=1, padx=1, pady=3, sticky=W)

        # Phone No
        Phone_no_label = Label(Class_Student_frame, text="Phone No:", font=("times new roman", 10, "bold"), bg="white")
        Phone_no_label.grid(row=2, column=2, padx=1, pady=3, sticky=W)

        Phone_no_entry = ttk.Entry(Class_Student_frame, textvariable=self.var_phone,width=20, font=("times new roman", 10, "bold"))
        Phone_no_entry.grid(row=2, column=3, padx=1, pady=3, sticky=W)

        # Address
        Adress_label = Label(Class_Student_frame, text="Address:", font=("times new roman", 10, "bold"), bg="white")
        Adress_label.grid(row=3, column=0, padx=1, pady=3, sticky=W)

        Adress_entry = ttk.Entry(Class_Student_frame, textvariable=self.var_address,width=20, font=("times new roman", 10, "bold"))
        Adress_entry.grid(row=3, column=1, padx=1, pady=3, sticky=W)
        
        #Teacher
        Teacher_label = Label(Class_Student_frame, text="Teacher name:", font=("times new roman", 10, "bold"), bg="white")
        Teacher_label.grid(row=3 , column=2, padx=1, pady=3, sticky=W)
        
        Teacher_entry = ttk.Entry(Class_Student_frame,textvariable=self.var_teacher, width=20, font=("times new roman", 10, "bold"))
        Teacher_entry.grid(row=3, column=3, padx=1, pady=3, sticky=W)
        
        
        #Gender
        Gender_label = Label(Class_Student_frame, text="Gender", font=("times new roman", 10, "bold"), bg="white")
        Gender_label.grid(row=4 , column=0, padx=1, pady=3, sticky=W)
        
        Gender_combo = ttk.Combobox(Class_Student_frame, textvariable=self.var_gender,font=("times new roman", 12, "bold"), state="readonly", width=17)
        Gender_combo["values"] = ("Select Gender","Male","Female","Other")
        Gender_combo.current(0)
        Gender_combo.grid(row=4, column=1, padx=1, pady=3, sticky=W)
        
        #DOB
        DOB_label = Label(Class_Student_frame, text="DOB", font=("times new roman", 10, "bold"), bg="white")
        DOB_label.grid(row=4 , column=2, padx=1, pady=3, sticky=W)
        
        DOB_entry = ttk.Entry(Class_Student_frame,textvariable=self.var_dob, width=20, font=("times new roman", 10, "bold"))
        DOB_entry.grid(row=4, column=3, padx=1, pady=3, sticky=W)    
    
        #Radio Button
        self.var_Radiobutton1=StringVar()
        Radiobutton1=ttk.Radiobutton(Class_Student_frame,variable=self.var_Radiobutton1,text="Take Photo Sample",value="Yes")
        Radiobutton1.grid(row=5,column=0, padx=5, sticky=W)
        
        Radiobutton2=ttk.Radiobutton(Class_Student_frame,variable=self.var_Radiobutton1, text="No Photo Sample",value="No")
        Radiobutton2.grid(row=5,column=1, padx=5, sticky=W)
        
        #Button Frame
        btn_frame=Frame(Class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=3,y=170,width=550,height=30)
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=7,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0,padx=2)
        
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=7,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1,padx=1)
        
        delete_btn=Button(btn_frame,text="Delete",width=7,command=self.delete_data,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2,padx=1)
        
        reset_btn=Button(btn_frame,text="Reset",width=7,command=self.reset_data,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3,padx=1)
        
        take_photo_btn=Button(btn_frame,command=self.generate_data_set,text="Take photo",width=9,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=4,padx=1)
        
        update_photo_btn=Button(btn_frame,text="Update photo",command=self.generate_data_set,width=10,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=5,padx=1)
        
              
        
        
       # Right label frame
        RIGHT_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="STUDENT DETAILS", font=("times new roman", 12, "bold"))
        RIGHT_frame.place(x=600, y=10, width=620, height=470)

     
   

        # Right Image
        right_img = Image.open(r"img\Student.webp")
        right_img = right_img.resize((600, 100)) 
        self.right_photoimg = ImageTk.PhotoImage(right_img)

        f_lbl = Label(RIGHT_frame, image=self.right_photoimg, bg="white", anchor=W) 
        f_lbl.place(x=0, y=0, relwidth=1, height=100)  

        #====Search System ======

        Search_System_frame = LabelFrame(RIGHT_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("times new roman", 12, "bold"))
        Search_System_frame.place(x=5, y=105, width=600, height=68)
        
        Search_label = Label(Search_System_frame, text="Search By:", font=("times new roman", 11, "bold"), bg="yellow")
        Search_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        
        Search_combo = ttk.Combobox(Search_System_frame, font=("times new roman", 12, "bold"), state="readonly", width=14)
        Search_combo["values"] = ("Select :", "Roll_No", "Phone-No")
        Search_combo.current(0)
        Search_combo.grid(row=0, column=1, padx=10, pady=10, sticky=W)
        
        
        Search_entry = ttk.Entry(Search_System_frame, width=20, font=("times new roman", 10, "bold"))
        Search_entry.grid(row=0, column=2, padx=1, pady=5, sticky=W)
        
        
        Search_btn=Button(Search_System_frame,text="Search",command=self.fetch_data,width=7,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Search_btn.grid(row=0,column=3,padx=5)
        
        ShowALL_btn=Button(Search_System_frame,text="Show All",command=self.fetch_data,width=7,font=("times new roman",13,"bold"),bg="blue",fg="white")
        ShowALL_btn.grid(row=0,column=4,padx=5)
        
        
         #====Table Frame ======

        table_frame = Frame(RIGHT_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=180, width=600, height=260)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,columns=("dept","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        
        self.student_table.heading("dept",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll_No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        
        self.student_table.column("dept",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
        
        #=================Function declaration============
    def add_data(self):
        if (self.var_dep.get() == "Select Department" or 
            self.var_stu_name.get() == "" or 
            self.var_stu_id.get() == "" or 
            self.var_address.get() == ""):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:    
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="15102004",
                    database="face_recognition"
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "INSERT INTO student (Department, Course, Year, Semester, Student_id, Name, Division, Roll_No, Gender, DOB, Email, Phone, Address, Teacher, radiobutton) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_stu_id.get(),
                        self.var_stu_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_Radiobutton1.get()
                    )
                )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details have been added successfully", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Error due to: {str(e)}", parent=self.root)

             #=======================Fetch Data=====================
    def fetch_data(self):
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="15102004",
                        database="face_recognition"
                    )
                    my_cursor = conn.cursor()
                    my_cursor.execute("select * from student ")
                    data=my_cursor.fetchall()
                    
                    if len(data)!=0:
                        self.student_table.delete(*self.student_table.get_children())
                        for i in data:
                            self.student_table.insert("",END,values=i)
                        conn.commit()
                    conn.close()
    #===================get cursor============
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]         
        
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_stu_id.set(data[4]),
        self.var_stu_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_Radiobutton1.set(data[14])
             
             
    #========Update Function=======
       
    def update_data(self):
        if (self.var_dep.get() == "Select Department" or 
                self.var_stu_name.get() == "" or 
                self.var_stu_id.get() == "" or 
                self.var_address.get() == ""):
                messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
                try:
                    Update = messagebox.askyesno("Update", "Do you want to update this student details?", parent=self.root)
                    if Update>0:
                        conn = mysql.connector.connect(
                            host="localhost",
                            username="root",
                            password="15102004",
                            database="face_recognition"
                        )
                        my_cursor = conn.cursor()
                        my_cursor.execute("""
                            UPDATE student 
                            SET Department=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, 
                                Roll_No=%s, Gender=%s, DOB=%s, Email=%s, Phone=%s, Address=%s, 
                                Teacher=%s, radiobutton=%s 
                            WHERE Student_id=%s
                        """, (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_sem.get(),
                            self.var_stu_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_Radiobutton1.get(),
                            self.var_stu_id.get()
                        ))
                        conn.commit()
                        self.fetch_data()
                        conn.close()    
                        messagebox.showinfo("Success", "Student information successfully updated", parent=self.root)
                    else:
                        messagebox.showinfo("Info", "Update operation cancelled", parent=self.root)
                except Exception as es:
                    messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)
                    
     #delete function               
    def delete_data(self):
        if self.var_stu_id.get=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root) 
                          
        else:
            try: 
                delete=messagebox.askyesno("Student Delete page","Do you want to delete this student?",parent=self.root)   
                
                if delete>0:
                    conn = mysql.connector.connect(
                                host="localhost",
                                username="root",
                                password="15102004",
                                database="face_recognition"
                            )
                    my_cursor = conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_stu_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return    
                            
                conn.commit()
                self.fetch_data()
                conn.close()    
                messagebox.showinfo("Delated Success", "Successfully deleted student details ", parent=self.root)
            except Exception as ed:
                    messagebox.showerror("Error", f"Error due to: {str(ed)}", parent=self.root) 
                    
                    
                       
    #delete function 
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")            
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_stu_id.set("")
        self.var_stu_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Female")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_Radiobutton1.set("")
        
        
        
        #=========Generate data set or take photo sample============
    def generate_data_set(self):
        if (self.var_dep.get() == "Select Department" or 
                self.var_stu_name.get() == "" or 
                self.var_stu_id.get() == "" or 
                self.var_address.get() == ""):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="15102004",
                    database="face_recognition"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute("""
                    UPDATE student 
                    SET Department=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, 
                        Roll_No=%s, Gender=%s, DOB=%s, Email=%s, Phone=%s, Address=%s, 
                        Teacher=%s, radiobutton=%s 
                    WHERE Student_id=%s
                """, (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_stu_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_Radiobutton1.get(),
                    self.var_stu_id.get()==id+1
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # Load predefined data on face frontals from OpenCV
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 10)
                    # Scaling factor=1.3, Minimum neighbor=5
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped
                    return None

                capture = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = capture.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (600, 600))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id),(50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 120:
                        break

                capture.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generation of data sets completed!!!")

            except Exception as ep:
                messagebox.showerror("Error", f"Error due to: {str(ep)}", parent=self.root)

        
                
                
if __name__ == "__main__":
        root = Tk()
        obj = Student(root)
        root.mainloop()            
                
                
