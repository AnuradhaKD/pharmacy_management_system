from logging import root
import random
import time
import datetime
from tkinter import *
from tkinter import ttk
from tkinter import font
import tkinter.messagebox

def main():
    root = Tk()
    app = windows1(root)
    root.mainloop()
    
class windows1:
    def __init__(self, master):
        self.master = master
        self.master.title("Pharmacy Management System")
        self.master.geometry('1270x710+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()
        
        self.Username = StringVar()
        self.Password = StringVar()
        
        self.LabelTitle = Label(self.frame, text = "      Pharmacy Management System      ", font=("arial", 40, "bold"), bd= 10, relief="sunken")
        self.LabelTitle.grid(row= 0, column= 0, columnspan=2, pady= 20)
        
        self.Loginframe1 = Frame(self.frame, width=1000, height=300, bd=10, relief="groove")
        self.Loginframe1.grid(row=1, column=0)
        
        self.Loginframe2 = Frame(self.frame, width=1000, height=100, bd=10, relief="groove")
        self.Loginframe2.grid(row=2, column=0, pady= 15)
        
        self.Loginframe3 = Frame(self.frame, width=1000, height=200, bd=10, relief="groove")
        self.Loginframe3.grid(row=6, column=0, pady= 5)
        
        self.button_reg = Button(self.Loginframe3,text = "Patient1 Registration Window", state= DISABLED, font=("arial", 15, "bold"), command= self.Registration_window)
        self.button_reg.grid(row=0, column=0, padx=10, pady=10)
        
        self.button_hosp = Button(self.Loginframe3,text = "Patient2 Registration Window", state= DISABLED, font=("arial", 15, "bold"), command= self.Hospital_window)
        self.button_hosp.grid(row=0, column=1, padx=10, pady=10)
        
        self.button_dr_app = Button(self.Loginframe3,text = "Patient3 Registration Window", state= DISABLED, font=("arial", 15, "bold"), command= self.Dr_appoint_window)
        self.button_dr_app.grid(row=1, column=0, padx=10, pady=10)
        
        self.button_med_stock = Button(self.Loginframe3,text = "Patient4 Registration Window", state= DISABLED, font=("arial", 15, "bold"), command= self.Medicine_stock)
        self.button_med_stock.grid(row=1, column=1, padx=10, pady=10)
        
        self.LabelUsername = Label(self.Loginframe1, text= "User Name", font = ("arial", 20, "bold"), bd= 3)
        self.LabelUsername.grid(row=0, column=0)
        
        self.textUsername = Entry(self.Loginframe1, font= ("arial", 20, "bold"), bd = 3, textvariable= self.Username)
        self.textUsername.grid(row= 0, column=1, padx= 40, pady= 15)
                
        self.LabelPassword = Label(self.Loginframe1, text= "Password", font = ("arial", 20, "bold"), bd= 3)
        self.LabelPassword.grid(row=1, column=0)
        
        self.textPassword = Entry(self.Loginframe1, font= ("arial", 20, "bold"), show="*", bd = 3, textvariable= self.Password)
        self.textPassword.grid(row= 1, column=1, padx= 40, pady= 15)
        
        self.button_login = Button(self.Loginframe2, text="Login", width=20, font=("arial", 18,"bold"), command= self.login_system)
        self.button_login.grid(row= 0, column= 0, padx= 10, pady= 10)
        
        self.button_reset = Button(self.Loginframe2, text="Reset", width=20, font=("arial", 18,"bold"), command= self.reset_btn)
        self.button_reset.grid(row= 0, column= 3, padx= 10, pady= 10)

        self.button_exit = Button(self.Loginframe2, text="Exit", width=20, font=("arial", 18,"bold"), command= self.exit_btn)
        self.button_exit.grid(row= 0, column= 6, padx= 10, pady= 10)
        
    def login_system(self):
        user = self.Username.get()
        pswd = self.Password.get()

        if (user == str("admin") and (pswd == str("admin"))):
            self.button_reg.config(state= NORMAL)
            self.button_hosp.config(state= NORMAL)
            self.button_dr_app.config(state= NORMAL)
            self.button_med_stock.config(state= NORMAL)
            
        else:
            tkinter.messagebox.askokcancel("Pharmacy Management System", "Invalid User name or Password")
            self.button_reg.config(state= DISABLED)
            self.button_hosp.config(state= DISABLED)
            self.button_dr_app.config(state= DISABLED)
            self.button_med_stock.config(state= DISABLED)
            
            self.Username.set("")
            self.Password.set("")
            self.textUsername.focus()
        
    def reset_btn(self):
        self.button_reg.config(state= DISABLED)
        self.button_hosp.config(state= DISABLED)
        self.button_dr_app.config(state= DISABLED)
        self.button_med_stock.config(state= DISABLED)
        
        self.Username.set("")
        self.Password.set("")
        self.textUsername.focus()
        
    def exit_btn(self):
        self.exit_btn = tkinter.messagebox.askyesno("Pharmacy Management System", "Are you sure ?")
        if self.exit_btn > 0:
            self.master.destroy()
            return
        
    def Registration_window(self):
        self.newWindow= Toplevel(self.master)
        self.app = windows2(self.newWindow)
        
    def Hospital_window(self):
        self.newWindow= Toplevel(self.master)
        self.app = windows3(self.newWindow)
        
    def Dr_appoint_window(self):
        self.newWindow= Toplevel(self.master)
        self.app = windows4(self.newWindow)
        
    def Medicine_stock(self):
        self.newWindow= Toplevel(self.master)
        self.app = windows5(self.newWindow)
        
class windows2:
    def __init__(self, master):
        self.master = master
        self.master.title("Patient Management System")
        self.master.geometry('1270x710+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

class windows3:
    def __init__(self, master):
        self.master = master
        self.master.title("Hospital Management System")
        self.master.geometry('1270x710+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

class windows4:
    def __init__(self, master):
        self.master = master
        self.master.title("Doctor Management System")
        self.master.geometry('1270x710+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()
        
class windows5:
    def __init__(self, master):
        self.master = master
        self.master.title("Medicine Management System")
        self.master.geometry('1270x710+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()
        
if __name__ == "__main__":
    main()