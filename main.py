from tkinter import *
from tkinter import ttk
import random
import datetime
from tkinter import messagebox

import pymysql



class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        # Variables
        self.NameofTablets = StringVar()
        self.ref = StringVar()
        self.Dose = StringVar()
        self.NumberofTablets = StringVar()
        self.Lot = StringVar()
        self.Issuedate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.sideEffect = StringVar()
        self.furtherinfo = StringVar()
        self.bloodPressure = StringVar()
        self.storage = StringVar()
        self.Medication = StringVar()
        self.patientId = StringVar()
        self.nhsNumber = StringVar()
        self.patientName = StringVar()
        self.dateOfBirth = StringVar()
        self.patientAddress = StringVar()
        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)
        # ================== DataFrame Left ====================




        DataFrame = LabelFrame(self.root, bd=10, padx=10, relief=RIDGE, font=("Arial", 12, "bold"),
                                   text="Patient Data")
        DataFrame.place(x=0, y=130, width=1670, height=920)
        
        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,font=("times new roman",10,"bold"),text="PATIENT INFORMATION")
        DataFrameLeft.place(x=0,y=5,width=1000,height=350)


        DataFrameright=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,font=("times new roman",10,"bold"),text="PATIENT INFORMATION")
        DataFrameright.place(x=1010,y=5,width=620,height=350)

        buttonframe=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,font=("times new roman",10,"bold"))
        buttonframe.place(x=2,y=360,width=1630,height=70)

        detailFrame=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,font=("times new roman",10,"bold"),text="PATIENT INFORMATION")
        detailFrame.place(x=2,y=430,width=1630,height=450)




        # Name of Tablets
        lblNameTablet = Label(DataFrameLeft, text="Name Of Tablets:", font=("Arial", 20, "bold"))
        lblNameTablet.grid(row=0, column=0, padx=2, pady=6, sticky=W)

        comNameTablet = ttk.Combobox(DataFrameLeft, textvariable=self.NameofTablets, state="readonly",
                                     font=("Arial",12, "bold"), width=33)
        comNameTablet["value"] = ("Nice", "Corona Vaccine", "Acetaminophen", "Adderall", "Amlodipine", "Ativan")
        comNameTablet.current(0)
        comNameTablet.grid(row=0, column=1)

        # Reference No
        lblref = Label(DataFrameLeft, font=("Arial", 20, "bold"), text="Reference No:")
        lblref.grid(row=1, column=0, sticky=W)
        txtref = Entry(DataFrameLeft, font=("Arial", 13, "bold"), textvariable=self.ref, width=35)
        txtref.grid(row=1, column=1)

        # Dose
        lblDose = Label(DataFrameLeft, font=("Arial", 20, "bold"), text="Dose:")
        lblDose.grid(row=2, column=0, sticky=W)
        txtDose = Entry(DataFrameLeft, font=("Arial", 13, "bold"), textvariable=self.Dose, width=35)
        txtDose.grid(row=2, column=1)

        # Number of Tablets
        lblNoOfTablets = Label(DataFrameLeft, font=("Arial", 20, "bold"), text="No Of Tablets:")
        lblNoOfTablets.grid(row=3, column=0, sticky=W)
        txtNoOfTablets = Entry(DataFrameLeft, font=("Arial", 13, "bold"), textvariable=self.NumberofTablets, width=35)
        txtNoOfTablets.grid(row=3, column=1)

        # Lot
        lblLot = Label(DataFrameLeft, font=("Arial", 20, "bold"), text="Lot:")
        lblLot.grid(row=4, column=0, sticky=W)
        txtLot = Entry(DataFrameLeft, font=("Arial", 13, "bold"), textvariable=self.Lot, width=35,)
        txtLot.grid(row=4, column=1)

        issdate = Label(DataFrameLeft, font=("Arial",20, "bold"), text="Issue Date:")
        issdate.grid(row=5, column=0, sticky=W)
        issdate = Entry(DataFrameLeft, font=("Arial", 13, "bold"), textvariable=self.Issuedate, width=35)
        issdate.grid(row=5, column=1)

        expdate = Label(DataFrameLeft, font=("Arial", 20, "bold"), text="EXP Date:")
        expdate.grid(row=6, column=0, sticky=W)
        expdate = Entry(DataFrameLeft, font=("Arial", 13, "bold"), textvariable=self.ExpDate, width=35)
        expdate.grid(row=6, column=1)

        dailydose = Label(DataFrameLeft, font=("Arial", 20, "bold"), text="Daily Dose:")
        dailydose.grid(row=7, column=0, sticky=W)
        dailydose = Entry(DataFrameLeft, font=("Arial", 13, "bold"), textvariable=self.DailyDose, width=35)
        dailydose.grid(row=7, column=1)

        sideeffects = Label(DataFrameLeft, font=("Arial", 20, "bold"), text="Side Effects:")
        sideeffects.grid(row=8, column=0, sticky=W)
        sideeffects = Entry(DataFrameLeft, font=("Arial", 13, "bold"), textvariable=self.sideEffect, width=35)
        sideeffects.grid(row=8, column=1)


###########################right data field##############################
        futurinf = Label(DataFrameLeft, font=("Arial", 20, "bold"), text="Further Information:")
        futurinf.grid(row=0, column=2, sticky=W)
        futurinf = Entry(DataFrameLeft, font=("Arial", 13, "bold"), textvariable=self.furtherinfo, width=35)
        futurinf.grid(row=0, column=3)

        bloodpressure = Label(DataFrameLeft, font=("Arial", 20, "bold"), text="Blood Pressure:")
        bloodpressure.grid(row=1, column=2, sticky=W)
        bloodpressure = Entry(DataFrameLeft, font=("Arial", 13, "bold"), textvariable=self.bloodPressure, width=35)
        bloodpressure.grid(row=1, column=3)

        
        storageadvice = Label(DataFrameLeft, font=("Arial", 20, "bold"), text="Storage Advice:")
        storageadvice.grid(row=2, column=2, sticky=W)
        storageadvice = Entry(DataFrameLeft, font=("Arial", 13, "bold"), textvariable=self.storage, width=35)
        storageadvice.grid(row=2, column=3)

        medication = Label(DataFrameLeft, font=("Arial", 20, "bold"), text="Medication:")
        medication.grid(row=3, column=2, sticky=W)
        medication = Entry(DataFrameLeft, font=("Arial", 13, "bold"), textvariable=self.Medication, width=35)
        medication.grid(row=3, column=3)

        
        patient_id = Label(DataFrameLeft, font=("Arial", 20, "bold"), text="Patient ID:")
        patient_id.grid(row=4, column=2, sticky=W)
        patient_id = Entry(DataFrameLeft, font=("Arial", 13, "bold"), textvariable=self.patientId, width=35)
        patient_id.grid(row=4, column=3)

        
        NHS_number = Label(DataFrameLeft, font=("Arial", 20, "bold"), text="NHS Number:")
        NHS_number.grid(row=5, column=2, sticky=W)
        NHS_number = Entry(DataFrameLeft, font=("Arial", 13, "bold"), textvariable=self.nhsNumber, width=35)
        NHS_number.grid(row=5, column=3)

        patients_name = Label(DataFrameLeft, font=("Arial", 20, "bold"), text="Patients Name:")
        patients_name.grid(row=6, column=2, sticky=W)
        patients_name = Entry(DataFrameLeft, font=("Arial", 13, "bold"), textvariable=self.patientName, width=35)
        patients_name.grid(row=6, column=3)

        dob = Label(DataFrameLeft, font=("Arial", 20, "bold"), text="Date Of Birth:")
        dob.grid(row=7, column=2, sticky=W)
        dob = Entry(DataFrameLeft, font=("Arial", 13, "bold"), textvariable=self.dateOfBirth, width=35)
        dob.grid(row=7, column=3)
        
        patients_address = Label(DataFrameLeft, font=("Arial", 20, "bold"), text="Patients Address:")
        patients_address.grid(row=8, column=2, sticky=W)
        patients_address = Entry(DataFrameLeft, font=("Arial", 13, "bold"), textvariable=self.patientAddress, width=35)
        patients_address.grid(row=8,column=3)

#======================== right data frame=========================================

      
        self.textprecption = Text(DataFrameright, font=("Arial", 13, "bold"), width=72,height=21)
        self.textprecption.grid(row=1, column=1)

#===================================  buttonss ===========================================

        btnPrescription = Button(buttonframe, text="Prescription",command=self.iprecriptiondata, bg="blue", fg="white",
                         font=("Arial", 13, "bold"), width=16, height=2)
        btnPrescription.grid(row=0, column=0, padx=30)

        btnUpdate = Button(buttonframe, text="Update",command=self.update_prescriptiondata, bg="green", fg="white",
                        font=("Arial", 13, "bold"), width=16, height=2)
        btnUpdate.grid(row=0, column=1, padx=100)

        btnDelete = Button(buttonframe, text="Delete",command=self.delete_prescriptiondata, bg="red", fg="white",
                        font=("Arial", 13, "bold"), width=16, height=2)
        btnDelete.grid(row=0, column=2, padx=100)

        btnReset = Button(buttonframe, text="Reset",command=self.reset_prescriptiondata, bg="#FFA500", fg="white",
                        font=("Arial", 13, "bold"), width=16, height=2)
        btnReset.grid(row=0, column=3, padx=100)

        btnExit = Button(buttonframe, text="Exit", bg="black", fg="white", 
                        font=("Arial", 13, "bold"), width=16, height=2, command=self.root.quit)
        btnExit.grid(row=0, column=4, padx=100)



        scroll_x=ttk.Scrollbar(detailFrame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detailFrame,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(detailFrame,columns=("NameofTablets",
                                                                "ref",
                                                                "Dose",
                                                                "NumberofTablets",
                                                                "Lot",
                                                                "Issuedate",
                                                                "ExpDate",
                                                                "DailyDose",
                                                                "sideEffect",
                                                                "furtherinfo",
                                                                "bloodPressure",
                                                                "storage",
                                                                "Medication",
                                                                "patientId",
                                                                "nhsNumber",
                                                                "patientName",
                                                                "dateOfBirth",
                                                                "patientAddress"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)


        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("NameofTablets", text="Name of Tablets")
        self.hospital_table.heading("ref", text="Reference No")
        self.hospital_table.heading("Dose", text="Dose")
        self.hospital_table.heading("NumberofTablets", text="Number of Tablets")
        self.hospital_table.heading("Lot", text="Lot")
        self.hospital_table.heading("Issuedate", text="Issue Date")
        self.hospital_table.heading("ExpDate", text="Expiry Date")
        self.hospital_table.heading("DailyDose", text="Daily Dose")
        self.hospital_table.heading("sideEffect", text="Side Effect")
        self.hospital_table.heading("furtherinfo", text="Further Info")
        self.hospital_table.heading("bloodPressure", text="Blood Pressure")
        self.hospital_table.heading("storage", text="Storage Advice")
        self.hospital_table.heading("Medication", text="Medication")
        self.hospital_table.heading("patientId", text="Patient ID")
        self.hospital_table.heading("nhsNumber", text="NHS Number")
        self.hospital_table.heading("patientName", text="Patient Name")
        self.hospital_table.heading("dateOfBirth", text="Date of Birth")
        self.hospital_table.heading("patientAddress", text="Patient Address")


        self.hospital_table["show"]="headings"



        self.hospital_table.column("NameofTablets", width=150)
        self.hospital_table.column("ref", width=120)
        self.hospital_table.column("Dose", width=100)
        self.hospital_table.column("NumberofTablets", width=140)
        self.hospital_table.column("Lot", width=100)
        self.hospital_table.column("Issuedate", width=120)
        self.hospital_table.column("ExpDate", width=120)
        self.hospital_table.column("DailyDose", width=130)
        self.hospital_table.column("sideEffect", width=130)
        self.hospital_table.column("furtherinfo", width=130)
        self.hospital_table.column("bloodPressure", width=130)
        self.hospital_table.column("storage", width=140)
        self.hospital_table.column("Medication", width=140)
        self.hospital_table.column("patientId", width=120)
        self.hospital_table.column("nhsNumber", width=140)
        self.hospital_table.column("patientName", width=150)
        self.hospital_table.column("dateOfBirth", width=130)
        self.hospital_table.column("patientAddress", width=180)
        


        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetchdata()



#======================== functionlity ==============================

    def iprecriptiondata(self):
    # Check if required fields are empty
        if self.NameofTablets.get() == "" or self.ref.get() == "":
                messagebox.showerror("Error", "All fields are required!")
                return

        try:
                conn = pymysql.connect(
                host="localhost",
                user="root",
                password="abisheek",
                database="hospital"
                )
                cursor = conn.cursor()
                print("Connected")

                cursor.execute("""
                INSERT INTO hospital VALUES 
                (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """, (
                self.NameofTablets.get(),
                self.ref.get(),
                self.Dose.get(),
                self.NumberofTablets.get(),
                self.Lot.get(),
                self.Issuedate.get(),
                self.ExpDate.get(),
                self.DailyDose.get(),
                self.sideEffect.get(),
                self.furtherinfo.get(),
                self.bloodPressure.get(),
                self.storage.get(),
                self.Medication.get(),
                self.patientId.get(),
                self.nhsNumber.get(),
                self.patientName.get(),
                self.dateOfBirth.get(),
                self.patientAddress.get(),
                ))

                conn.commit()
                self.fetchdata()
                conn.close()
                messagebox.showinfo("Success", "Record Inserted Successfully!")

        except Exception as e:
                messagebox.showerror("Error", f"Database Error: {str(e)}")
    def fetchdata(self):
           conn = pymysql.connect(
                host="localhost",
                user="root",
                password="abisheek",
                database="hospital"
                )
           cursor = conn.cursor()
           cursor.execute("select * from hospital")
           rows=cursor.fetchall()
           if len (rows)!=0:
                  self.hospital_table.delete(*self.hospital_table.get_children())
                  for i in rows:
                         self.hospital_table.insert("",END,values=i)
                  conn.commit()
           conn.close()
           
    def get_cursor(self, event=""):
        cursor_row = self.hospital_table.focus()  # Get selected row's ID
        content = self.hospital_table.item(cursor_row)  # Get data of that row
        row = content['values']  # Extract values list

        if row:  # Check if row is not empty
                self.NameofTablets.set(row[0])
                self.ref.set(row[1])
                self.Dose.set(row[2])
                self.NumberofTablets.set(row[3])
                self.Lot.set(row[4])
                self.Issuedate.set(row[5])
                self.ExpDate.set(row[6])
                self.DailyDose.set(row[7])
                self.sideEffect.set(row[8])
                self.furtherinfo.set(row[9])
                self.bloodPressure.set(row[10])
                self.storage.set(row[11])
                self.Medication.set(row[12])
                self.patientId.set(row[13])
                self.nhsNumber.set(row[14])
                self.patientName.set(row[15])
                self.dateOfBirth.set(row[16])
                self.patientAddress.set(row[17])



                
    def update_prescriptiondata(self):
    # Check if required fields are empty
        if self.NameofTablets.get() == "" or self.ref.get() == "":
                messagebox.showerror("Error", "All fields are required!")
                return

        try:
                conn = pymysql.connect(
                host="localhost",
                user="root",
                password="abisheek",
                database="hospital"
                )
                cursor = conn.cursor()
                print("Connected")

                cursor.execute("""
    UPDATE hospital SET
        nameofTablets=%s,
        dose=%s,
        numberofTablets=%s,
        lot=%s,
        issueDate=%s,
        expDate=%s,
        dailyDose=%s,
        sideEffect=%s,
        furtherInfo=%s,
        bloodPressure=%s,
        storage=%s,
        medication=%s,
        patientId=%s,
        nhsNumber=%s,
        patientName=%s,
        dateOfBirth=%s,
        patientAddress=%s
    WHERE ref=%s
""", (
    self.NameofTablets.get(),
    self.Dose.get(),
    self.NumberofTablets.get(),
    self.Lot.get(),
    self.Issuedate.get(),
    self.ExpDate.get(),
    self.DailyDose.get(),
    self.sideEffect.get(),
    self.furtherinfo.get(),
    self.bloodPressure.get(),
    self.storage.get(),
    self.Medication.get(),
    self.patientId.get(),
    self.nhsNumber.get(),
    self.patientName.get(),
    self.dateOfBirth.get(),
    self.patientAddress.get(),
    self.ref.get()  # Reference_No used in WHERE clause
))


                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Record Updated Successfully!")

        except Exception as e:
                messagebox.showerror("Error", f"Database Error: {str(e)}")




    def delete_prescriptiondata(self):
    # Check if Reference_No is provided
        if self.ref.get() == "":
                messagebox.showerror("Error", "Reference Number is required to delete a record!")
                return

        try:
                conn = pymysql.connect(
                host="localhost",
                user="root",
                password="abisheek",
                database="hospital"
                )
                cursor = conn.cursor()
                

                # Execute DELETE query
                cursor.execute("DELETE FROM hospital WHERE ref=%s", (self.ref.get(),))

                if cursor.rowcount == 0:
                        messagebox.showwarning("Warning", "No record found with this Reference Number!")
                else:
                        conn.commit()
                        messagebox.showinfo("Success", "Record Deleted Successfully!")

                conn.close()

        except Exception as e:
                messagebox.showerror("Error", f"Database Error: {str(e)}")
    def reset_prescriptiondata(self):
        try:
                # Clear all the entry fields
                self.NameofTablets.set("")
                self.ref.set("")
                self.Dose.set("")
                self.NumberofTablets.set("")
                self.Lot.set("")
                self.Issuedate.set("")
                self.ExpDate.set("")
                self.DailyDose.set("")
                self.sideEffect.set("")
                self.furtherinfo.set("")
                self.bloodPressure.set("")
                self.storage.set("")
                self.Medication.set("")
                self.patientId.set("")
                self.nhsNumber.set("")
                self.patientName.set("")
                self.dateOfBirth.set("")
                self.patientAddress.set("")

                messagebox.showinfo("Reset", "All fields have been cleared!")

        except Exception as e:
                messagebox.showerror("Error", f"Reset Error: {str(e)}")
    

        









# Run the app
if __name__ == "__main__":
    root = Tk()
    obj = Hospital(root)
    root.mainloop()
