import tkinter as tk
from tkinter import ttk
import constants
import db
import doctor
from tkcalendar import Calendar




class CreateDoctorPage(tk.Frame):
    def __init__(self, container, controller):
        ttk.Frame.__init__(self, container)
        self.current_doctor=None
        self.controller=controller

    def display_content(self):
        _list = self.winfo_children()
        for child in _list:
            child.destroy()
        headerLabel=ttk.Label(self, text = "Creating a doctor's profile", font = constants.Large_font)
        nameLabel = ttk.Label(self, text = "Set doctor\'s name")
        name_entry=ttk.Entry(self)
        
        varA = tk.BooleanVar()
        doA_button = ttk.Checkbutton(self, text="List A", variable=varA, state="active", onvalue=True, offvalue=False)
        
        varB = tk.BooleanVar()
        doB_button = ttk.Checkbutton(self, text="List B", variable=varB, offvalue=False, onvalue=True)
        
        varC = tk.BooleanVar()
        doC_button = ttk.Checkbutton(self, text="List C", variable=varC, offvalue=False, onvalue=True)
        
        var3 = tk.BooleanVar()
        do3_button = ttk.Checkbutton(self, text="List 3", variable=var3, offvalue=False, onvalue=True)
        
        varICU = tk.BooleanVar()
        doICU_button = ttk.Checkbutton(self, text="List ICU", variable=varICU, offvalue=False, onvalue=True)
        
        varSPIRE = tk.BooleanVar()
        doSPIRE_button = ttk.Checkbutton(self, text="List SPIRE", variable=varSPIRE, offvalue=False, onvalue=True)
       
        PAentry=ttk.Entry(self)
        PPentry=ttk.Entry(self)
        
        confirmButton=ttk.Button(self, text="confirm", command=lambda: self.current_doctor.set_attributes(name=name_entry.get(), doA=varA.get(), doB=varB.get(), doC=varC.get(), do3=var3.get(), doICU=varICU.get(), doSPIRE=varSPIRE.get(), targetPA=PAentry.get(), targetPP=PPentry.get()))
        daysOffWorkButton=ttk.Button(self, text='Select days off', command=self.calendarWindow)
        back_button=ttk.Button(self, text="Back", command=lambda: self.controller.show_frame(0))

        headerLabel.grid(row=0, pady=20)
        nameLabel.grid(row=1, column=0,pady=20)
        name_entry.grid(row=1, column=1,pady=20)
        doA_button.grid(row=2, column=1,pady=20)
        doB_button.grid(row=3, column=1,pady=20)
        doC_button.grid(row=4, column=1,pady=20)
        do3_button.grid(row=5, column=1,pady=20)
        doICU_button.grid(row=6, column=1,pady=20)
        doSPIRE_button.grid(row=7, column=1,pady=20)
        PAentry.grid(row=8, column=1, pady=20)
        PPentry.grid(row=9, column=1, pady=20)
        confirmButton.grid(row=2, column=0, rowspan=9, pady=20)
        daysOffWorkButton.grid(row=10, column =0,pady=20)
        back_button.grid(row=11,pady=20)

    
        
    def set_current_doctor(self,doctor):
        self.current_doctor=doctor 
    
    def calendarWindow(self):
        def select_day_off_work():
            self.current_doctor.set_day_off_work(cal.selection_get())
            

        top = tk.Toplevel(self)
        style = ttk.Style(top)
        style.theme_use('clam')
        cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand2", year=2020, month=2, day=5, background="black", disabledbackground="black", bordercolor="black", 
               headersbackground="black", normalbackground="black", foreground='white', 
               normalforeground='white', headersforeground='white')
        cal.pack(fill="both", expand=True)
        ttk.Button(top, text="confirm", command=select_day_off_work).pack()


