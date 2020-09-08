import tkinter as tk
from tkinter import ttk
import constants
import db
import doctor
from tkcalendar import Calendar
import datetime
import solver
from functools import partial



#importing pages needed
from results_page import Results
from create_doctor_page import CreateDoctorPage

class StartPage(tk.Frame):
    def __init__(self, container, controller):
        ttk.Frame.__init__(self, container)
        self.controller=controller
        
        
    def display_content(self):
        _list = self.winfo_children()
        for child in _list:
            child.destroy()
        headerLabel=ttk.Label(self, text="Welcome to the Rota Scheduling Tool\n Create doctors, and input their schedules below then have a cup of Tea and let us do the work!", font=constants.Large_font)
        rotaButton = ttk.Button(self, text="Click to see the Rota", command=lambda : self.run_solver())
        create_new_doctorButton=ttk.Button(self, text="Create a new Doctor Profile", command=lambda : self.create_new_doctor())
        

        headerLabel.grid(row=0, padx =self.winfo_screenwidth()/6)
        rotaButton.grid(row=21, sticky = "ns")
        create_new_doctorButton.grid(row=20, sticky = "ns")
        lst_of_doctor_buttons=[]
        if db.get_startdate()==datetime.date(2000,1,3):
            no_start_dateLabel=ttk.Label(self, text = "No start date selected, please select one below before continuing")
            choose_start_dateButton=ttk.Button(self, text="Choose start date", command=self.calendarWindow)
            no_start_dateLabel.grid(row=1, pady=20)
            choose_start_dateButton.grid(row=2, pady=20)
        else:
            start_dateLabel=ttk.Label(self, text="Start date already selected, to change it delete the database")
            start_dateLabel.grid(row=1, pady=20)
        if len(db.get_doctors_list())==0:
            no_doctorsLabel=ttk.Label(self, text="No current doctors", font = constants.Large_font)
            no_doctorsLabel.grid(row=3)
        else:
            for i in range(len(db.get_doctors_list())):
                lst_of_doctor_buttons.append(ttk.Button(self, text=db.get_doctors_list()[i].name, command=partial(self.edit_doctor, i)))
                lst_of_doctor_buttons[-1].grid(row=i+6)
    #this function was not originally there
    def edit_doctor(self, n):
        self.controller.frames[3].set_current_doctor(doctor=db.get_doctors_list()[n], old_name=db.get_doctors_list()[n].name)
        self.controller.show_frame(3)

    def create_new_doctor(self):
        new_doctor=doctor.Doctor()
        self.controller.show_frame(2)
        self.controller.frames[2].set_current_doctor(new_doctor)
    
    def run_solver(self):
        results_dictionary=solver.brain()
        self.controller.frames[1].set_results_dictionary(results_dictionary)
        self.controller.show_frame(1)
        
        
        



    def calendarWindow(self):
        def selecting_start_date():
            if cal.selection_get().weekday()==0:
                db.startdate=cal.selection_get()
                self.controller.show_frame(0)
            else: 
                top2=tk.Toplevel(self)
                label5=ttk.Label(top2, text="Please select a Monday")
                label5.pack()
            

        top = tk.Toplevel(self)
        style = ttk.Style(top)
        style.theme_use('clam')
        cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand2", year=2020, month=2, day=5, background="black", disabledbackground="black", bordercolor="black", 
               headersbackground="black", normalbackground="black", foreground='white', 
               normalforeground='white', headersforeground='white')
        cal.pack(fill="both", expand=True)
        ttk.Button(top, text="confirm", command=selecting_start_date).pack()