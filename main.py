from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk #python3 -m pip install --upgrade Pillow  ---------Run this command if pillow error-----------
import random,os
from tkinter import messagebox
import tempfile
from time import strftime


class Training_Fee_Calculator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("North Sussex Judo App")

        # Variables
        self.aname=StringVar()
        self.a_phone=StringVar()
        self.bill_no=StringVar()
        y=random.randint(1000,9999)
        self.bill_no.set(y)
        self.a_email=StringVar()
        self.search_bill=StringVar()
        self.package=StringVar()
        self.prices=DoubleVar()
        self.comp=IntVar()
        self.train_hours=IntVar()
        self.total=StringVar()
        self.weight=StringVar()
        self.current_weight=StringVar()

        #Package Catagory List
        self.Category=["Select Option", "Beginner (2 Sessions per week) - Weekly Fee", "Intermediate (3 Sessions per week) - Weekly Fee", "Elite (5 Sessions per week) - Weekly Fee", "Private Tuition - Per Hour", "Competition Entry Fee - Per Competition"]
        self.price_A=25.00
        self.price_B=30.00
        self.price_C=35.00
        self.price_D=9.50
        self.price_E=22.00

        #Weight Catagory List
        self.Weight_C=["Select Option", "Heavyweight", "Light-Heavyweight", "Middleweight", "Light-Middleweight", "Lightweight", "Flyweight"]

        lbl_title=Label(self.root,text="North Sussex Judo",font=("times new roman",35,"bold"))
        lbl_title.place(x=0,y=0,width=1530,height=45)

        #Clock
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl = Label(lbl_title, font = ("times new roman",16, "bold"),fg = "blue")
        lbl.place(x=0,y=(-15), width=120,height=50)
        time()

        #Main Frame
        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=60,width=1530,height=740)

        # Athlete Details Label Frame
        Cust_Frame=LabelFrame(Main_Frame,text="Athlete Details",font=("times new roman",12,"bold"),bg="white",fg="red")
        Cust_Frame.place(x=10,y=5,width=350,height=140)

        self.lbl_Mobile=Label(Cust_Frame,text="Mobile No:",font=("times new roman",12,"bold"),bg="white")
        self.lbl_Mobile.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.entry_Mobile=ttk.Entry(Cust_Frame,textvariable=self.a_phone,font=("times new roman",12,"bold"),width=24)
        self.entry_Mobile.grid(row=0,column=1)

        self.lbl_Athlete_Name=Label(Cust_Frame,text="Athlete Name:",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lbl_Athlete_Name.grid(row=1,column=0,stick=W,padx=5,pady=2)

        self.entry_Athlete_Name=ttk.Entry(Cust_Frame,textvariable=self.aname,font=("times new roman",12,"bold"),width=24)
        self.entry_Athlete_Name.grid(row=1,column=1,stick=W,padx=5,pady=2)

        self.lbl_Email=Label(Cust_Frame,text="Email:",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lbl_Email.grid(row=2,column=0,stick=W,padx=5,pady=2)

        self.entry_Email=ttk.Entry(Cust_Frame,textvariable=self.a_email,font=("times new roman",12,"bold"),width=24)
        self.entry_Email.grid(row=2,column=1,stick=W,padx=5,pady=2)

        # Training Details Label Frame
        Training_Frame=LabelFrame(Main_Frame,text="Training Details",font=("times new roman",12,"bold"),bg="white",fg="red")
        Training_Frame.place(x=370,y=5,width=1010,height=140)

        self.lbl_Training_Plan=Label(Training_Frame,text="Training Plan:",font=("times new roman",12,"bold"),bg="white")
        self.lbl_Training_Plan.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.Combo_Training_Plan=ttk.Combobox(Training_Frame,textvariable=self.package,value=self.Category,font=("times new roman",12,"bold"),width=24,state="readonly")
        self.Combo_Training_Plan.current(0)
        self.Combo_Training_Plan.grid(row=0,column=1,stick=W,padx=5,pady=2)
        self.Combo_Training_Plan.bind("<<ComboboxSelected>>",self.price)

        #Current Weight Lable
        self.lbl_Current_Weight=Label(Training_Frame,text="Current Weight (KG):",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lbl_Current_Weight.grid(row=1,column=0,stick=W,padx=5,pady=2)

        self.entry_Current_Weight=ttk.Entry(Training_Frame,textvariable=self.current_weight,font=("times new roman",12,"bold"),width=24)
        self.entry_Current_Weight.grid(row=1,column=1,stick=W,padx=5,pady=2)

        #Weight Category Lable
        self.lbl_Weight_Category=Label(Training_Frame,text="Weight Category:",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lbl_Weight_Category.grid(row=2,column=0,stick=W,padx=5,pady=2)

        self.Combo_Weight_Category=ttk.Combobox(Training_Frame,textvariable=self.weight,value=self.Weight_C,font=("times new roman",12,"bold"),width=24,state="readonly")
        self.Combo_Weight_Category.current(0)
        self.Combo_Weight_Category.grid(row=2,column=1,stick=W,padx=5,pady=2)

        #No of Competitions Lable
        self.lbl_No_Of_Comp_Entered=Label(Training_Frame,text="Number of Competitions Entered This Month:",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lbl_No_Of_Comp_Entered.grid(row=0,column=4,stick=W,padx=5,pady=2)

        self.entry_No_Of_Comp_Entered=ttk.Entry(Training_Frame,textvariable=self.comp,font=("times new roman",12,"bold"),width=24)
        self.entry_No_Of_Comp_Entered.grid(row=0,column=5,stick=W,padx=5,pady=2)

        #No of Private Training Hours Lable
        self.lbl_No_Of_Priv_Training=Label(Training_Frame,text="Number of Private Training Hours or No of Weeks:",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lbl_No_Of_Priv_Training.grid(row=1,column=4,stick=W,padx=5,pady=2)

        self.entry_No_Of_Priv_Training=ttk.Entry(Training_Frame,textvariable=self.train_hours,font=("times new roman",12,"bold"),width=24)
        self.entry_No_Of_Priv_Training.grid(row=1,column=5,stick=W,padx=5,pady=2)

        #Package Price Lable
        self.lbl_Price=Label(Training_Frame,text="Package Price:",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lbl_Price.grid(row=2,column=4,stick=W,padx=5,pady=2)

        self.entry_Price=ttk.Combobox(Training_Frame,state="readonly",textvariable=self.prices,font=("times new roman",12,"bold"),width=24)
        self.entry_Price.grid(row=2,column=5,stick=W,padx=5,pady=2)

        #Invoice Frame
        Invoice_Frame=LabelFrame(Main_Frame,text="Invoice Details",font=("times new roman",12,"bold"),bg="white",fg="red")
        Invoice_Frame.place(x=10,y=160,width=710,height=400)

        #Invoice Frame Scrollbar
        scroll_y=Scrollbar(Invoice_Frame,orient=VERTICAL)
        self.textarea=Text(Invoice_Frame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        # Total Amount Frame
        Total_Frame=LabelFrame(Main_Frame,text="Total",font=("times new roman",12,"bold"),bg="white",fg="red")
        Total_Frame.place(x=10,y=575,width=300,height=80)

        self.lbl_Total=Label(Total_Frame,text="Total:",textvariable=self.total,font=("times new roman",12,"bold"),bg="white")
        self.lbl_Total.grid(row=0,column=0,stick=W,padx=5,pady=2)

        #Button Frame
        Btn_Frame=LabelFrame(Main_Frame,bd=2,bg="white")
        Btn_Frame.place(x=975,y=260,width=405,height=225)

        #Add Invoice Button
        self.BtnAddToInv=Button(Btn_Frame,command=self.AddItem,height=2,width=15,text="Add to Invoice",font=("times new roman",15,"bold"),bg="orangered",fg="white",cursor="hand2")
        self.BtnAddToInv.grid(row=0,column=0,stick=W,padx=5,pady=5)

        #Generate Invoice Button
        self.BtnGenerateInv=Button(Btn_Frame,height=2,width=15,text="Generate Invoice",command=self.genbill,font=("times new roman",15,"bold"),bg="orangered",fg="white",cursor="hand2")
        self.BtnGenerateInv.grid(row=0,column=1,stick=W,padx=5,pady=5)

        #Save Invoice Button
        self.BtnSaveInv=Button(Btn_Frame,command=self.save_bill,height=2,width=15,text="Save Invoice",font=("times new roman",15,"bold"),bg="orangered",fg="white",cursor="hand2")
        self.BtnSaveInv.grid(row=1,column=0,stick=W,padx=5,pady=5)

        #Print Invoice Button
        self.BtnPrint=Button(Btn_Frame,height=2,width=15,text="Print",command=self.iprint,font=("times new roman",15,"bold"),bg="orangered",fg="white",cursor="hand2")
        self.BtnPrint.grid(row=1,column=1,stick=W,padx=5,pady=5)

        #Clear All Fields Button
        self.BtnClear=Button(Btn_Frame,height=2,width=15,text="Clear",command=self.clear,font=("times new roman",15,"bold"),bg="orangered",fg="white",cursor="hand2")
        self.BtnClear.grid(row=2,column=0,stick=W,padx=5,pady=5)
        
        #Exit Button
        self.BtnExit=Button(Btn_Frame,height=2,width=15,text="Exit",command=self.root.destroy,font=("times new roman",15,"bold"),bg="orangered",fg="white",cursor="hand2")
        self.BtnExit.grid(row=2,column=1,stick=W,padx=5,pady=5)

        # #Search
        # Search_Frame=LabelFrame(Main_Frame,bd=2,bg="white")
        # Search_Frame.place(x=975,y=170,width=405,height=80)

        # self.lbl_Inv=Label(Search_Frame,text="Invoice Number",font=("times new roman",12,"bold"),bg="White",width=15)
        # self.lbl_Inv.grid(row=0,column=0,stick=W,padx=5,pady=5)

        # self.lbl_Search_Entry=ttk.Entry(Search_Frame,font=("times new roman",12,"bold"),width=24)
        # self.lbl_Search_Entry.grid(row=0,column=1,stick=W,padx=1)

        # self.Btn_Search=Button(Search_Frame,text="Search",command=self.find_bill,font=("times new roman",12,"bold"),fg="white",bg="orangered",width=15)
        # self.Btn_Search.grid(row=1,column=0,stick=W,padx=5,pady=5)

        self.welcome()

        self.l=[]

    #=============================Functions=================================

    #Invoice Header Function
    def welcome(self):
        self.textarea.delete(1.0,END)
        
        self.textarea.insert(END,"\t\t\t\t\t Welcome to North Sussex Judo")
        self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
        self.textarea.insert(END,f"\n Athlete Name:{self.aname.get()}")
        self.textarea.insert(END,f"\n Mobile Number:{self.a_phone.get()}")
        self.textarea.insert(END,f"\n Email:{self.a_email.get()}")

        self.textarea.insert(END,"\n============================================================================")
        self.textarea.insert(END,f"\n Package\t\t\t\t\tNo of Weeks/Hours\t\t\t\t\tPrice")
        self.textarea.insert(END,"\n============================================================================\n")

    #Onclick Add to Invoice Function
    def AddItem(self):
        self.n=self.prices.get()
        self.m=self.train_hours.get()*self.n
        self.l.append(self.m)
        if self.package.get()=="Select Option":
            messagebox.showerror("ERROR","Please Select a Training Plan")
        elif self.train_hours.get() > 5:
            messagebox.showerror("Error", "Number of Training hours is greater than 5")
        elif self.package.get()=="Beginner (2 Sessions per week) - Weekly Fee" and self.comp.get() > 0:
            messagebox.showerror("Error", "Only Intermediate and Elite athletes can enter competitions")
        else:
            self.textarea.insert(END,f"\n {self.package.get()}\t\t\t\t\t\t{self.train_hours.get()}\t\t\t\t{self.m}")
            self.total.set(str('GBP %.2f'%(sum(self.l))))
        
    #Onclick Generate Invoice Function
    def genbill(self):
        if self.package.get()=="Select Option":
            messagebox.showerror("Error","Please add a product to cart")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n============================================================================")
            self.textarea.insert(END,f"\n Total:\t\t\t\t{self.total.get()}")

    #Onclick Save Invoice Function
    def save_bill(self):
        op=messagebox.askyesno("Save Bill", "Would you like to save the bill?")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open('bills/'+str(self.bill_no.get())+".txt",'w')
            f1.write(self.bill_data)
            op=messagebox.showinfo("Saved",f"Bill No:{self.bill_no.get()} saved successfully")
            f1.close()

    #Onclick Print Function
    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")

    # def find_bill(self):
    #     found="no"
    #     for i in os.listdir("bills/"):
    #         if i.split('.')[0]==self.search_bill.get():
    #             f1=open(f"bills/{i}",'r')
    #             self.textarea.delete(1.0,END)
    #             for d in f1:
    #                 self.textarea.insert(END,d)
    #             f1.close()
    #             found="yes"
    #     if found=='no':
    #         messagebox.showerror("Error","Invalid Bill No.")

    #Onclick Delete Function
    def clear(self):
        self.textarea.delete(1.0,END)
        self.aname.set("")
        self.a_phone.set("")
        y=random.randint(1000,9999)
        self.bill_no.set(str(y))
        self.a_email.set("")
        self.search_bill.set("")
        self.package.set("")
        self.prices.set("")
        self.train_hours.set("")
        self.total.set("")
        self.welcome()
        self.comp.set("")
        self.weight.set("")
        self.current_weight.set("")

    #Package Price Function
    def price(self,event=""):
        if self.Combo_Training_Plan.get()=="Beginner (2 Sessions per week) - Weekly Fee":
            self.entry_Price.config(value=self.price_A)
            self.entry_Price.current(0)
            self.train_hours.set(1)

        if self.Combo_Training_Plan.get()=="Intermediate (3 Sessions per week) - Weekly Fee":
            self.entry_Price.config(value=self.price_B)
            self.entry_Price.current(0)
            self.train_hours.set(1)

        if self.Combo_Training_Plan.get()=="Elite (5 Sessions per week) - Weekly Fee":
            self.entry_Price.config(value=self.price_C)
            self.entry_Price.current(0)
            self.train_hours.set(1)

        if self.Combo_Training_Plan.get()=="Private Tuition - Per Hour":
            self.entry_Price.config(value=self.price_D)
            self.entry_Price.current(0)
            self.train_hours.set(1)

        if self.Combo_Training_Plan.get()=="Competition Entry Fee - Per Competition":
            self.entry_Price.config(value=self.price_E)
            self.entry_Price.current(0)
            self.train_hours.set(1)

if __name__ == '__main__':
    root=Tk()
    obj=Training_Fee_Calculator(root)
    root.mainloop()