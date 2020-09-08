import tkinter as tk
from tkinter import ttk
import constants
import db
import doctor

padx=75
padx1=25

class Results(tk.Frame):
    def __init__(self, container, controller):
        ttk.Frame.__init__(self, container)
        self.controller=controller
        self.results_dictionary=None
    def display_content(self):
        _list = self.winfo_children()
        for child in _list:
            child.destroy()
        tabControl=ttk.Notebook(self)
        doctor_tab=ttk.Frame(tabControl)
        calender_tab=ttk.Frame(tabControl)
        tabControl.add(doctor_tab, text = "Doctors", )
        tabControl.add(calender_tab, text = "Calendar View")
        tabControl.pack(expand = 1, fill = "both")

        canvas = tk.Canvas(calender_tab)
        scrollbar = ttk.Scrollbar(calender_tab, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        backButton=ttk.Button(self, text="Back To Home", command=lambda: self.controller.show_frame(0))
        
        backButton.pack()
        

        #following block is designing the calender view
        day_labels=[]
        shift_and_doctor_labels=[]
        days_left=constants.days
        day_index=0
        while days_left>0:
            if day_index<5:
                day_labels.append(ttk.Label(scrollable_frame, text=db.get_startdate()+day_index*constants.delta, font=constants.Large_font))
                day_labels[-1].grid(row=0, column=day_index,padx=padx)
                for s in range(constants.shifts):
                    for n in range(len(db.get_doctors_list())):
                        if self.results_dictionary[(n,day_index,s)] == 1:
                            shift_and_doctor_labels.append(ttk.Label(scrollable_frame, text='{} {}'.format(db.get_doctors_list()[n].name, s+1), font=constants.Small_font ))
                            shift_and_doctor_labels[-1].grid(column=day_index, row=s+1, pady=10)
            elif day_index<10:
                day_labels.append(ttk.Label(scrollable_frame, text=db.get_startdate()+(day_index+2)*constants.delta, font=constants.Large_font))
                day_labels[-1].grid(row=7, column=day_index-5,padx=padx)
                for s in range(constants.shifts):
                    for n in range(len(db.get_doctors_list())):
                        if self.results_dictionary[(n,day_index,s)] == 1:
                            shift_and_doctor_labels.append(ttk.Label(scrollable_frame, text='{} {}'.format(db.get_doctors_list()[n].name, s+1), font=constants.Small_font ))
                            shift_and_doctor_labels[-1].grid(column=day_index-5, row=s+1+7, pady=10)
            elif day_index<15:
                day_labels.append(ttk.Label(scrollable_frame, text=db.get_startdate()+(day_index+4)*constants.delta, font=constants.Large_font))
                day_labels[-1].grid(row=14, column=day_index-10,padx=padx)
                for s in range(constants.shifts):
                    for n in range(len(db.get_doctors_list())):
                        if self.results_dictionary[(n,day_index,s)] == 1:
                            shift_and_doctor_labels.append(ttk.Label(scrollable_frame, text='{} {}'.format(db.get_doctors_list()[n].name, s+1), font=constants.Small_font ))
                            shift_and_doctor_labels[-1].grid(column=day_index-10, row=s+1+14, pady=10)
            elif day_index<20:
                day_labels.append(ttk.Label(scrollable_frame, text=db.get_startdate()+(day_index+6)*constants.delta, font=constants.Large_font))
                day_labels[-1].grid(row=21, column=day_index-15,padx=padx)
                for s in range(constants.shifts):
                    for n in range(len(db.get_doctors_list())):
                        if self.results_dictionary[(n,day_index,s)] == 1:
                            shift_and_doctor_labels.append(ttk.Label(scrollable_frame, text='{} {}'.format(db.get_doctors_list()[n].name, s+1), font=constants.Small_font ))
                            shift_and_doctor_labels[-1].grid(column=day_index-15, row=s+1+21, pady=10)
            elif day_index<25:
                day_labels.append(ttk.Label(scrollable_frame, text=db.get_startdate()+(day_index+8)*constants.delta, font=constants.Large_font))
                day_labels[-1].grid(row=28, column=day_index-20,padx=padx)
                for s in range(constants.shifts):
                    for n in range(len(db.get_doctors_list())):
                        if self.results_dictionary[(n,day_index,s)] == 1:
                            shift_and_doctor_labels.append(ttk.Label(scrollable_frame, text='{} {}'.format(db.get_doctors_list()[n].name, s+1), font=constants.Small_font ))
                            shift_and_doctor_labels[-1].grid(column=day_index-20, row=s+1+28, pady=10)
            elif day_index<30:
                day_labels.append(ttk.Label(scrollable_frame, text=db.get_startdate()+(day_index+10)*constants.delta, font=constants.Large_font))
                day_labels[-1].grid(row=35, column=day_index-25,padx=padx)
                for s in range(constants.shifts):
                    for n in range(len(db.get_doctors_list())):
                        if self.results_dictionary[(n,day_index,s)] == 1:
                            shift_and_doctor_labels.append(ttk.Label(scrollable_frame, text='{} {}'.format(db.get_doctors_list()[n].name, s+1), font=constants.Small_font ))
                            shift_and_doctor_labels[-1].grid(column=day_index-25, row=s+1+35, pady=10)
            elif day_index<35:
                day_labels.append(ttk.Label(scrollable_frame, text=db.get_startdate()+(day_index+12)*constants.delta, font=constants.Large_font))
                day_labels[-1].grid(row=42, column=day_index-30,padx=padx)
                for s in range(constants.shifts):
                    for n in range(len(db.get_doctors_list())):
                        if self.results_dictionary[(n,day_index,s)] == 1:
                            shift_and_doctor_labels.append(ttk.Label(scrollable_frame, text='{} {}'.format(db.get_doctors_list()[n].name, s+1), font=constants.Small_font ))
                            shift_and_doctor_labels[-1].grid(column=day_index-30, row=s+1+42, pady=10)
            elif day_index<40:
                day_labels.append(ttk.Label(scrollable_frame, text=db.get_startdate()+(day_index+14)*constants.delta, font=constants.Large_font))
                day_labels[-1].grid(row=49, column=day_index-35,padx=padx)
                for s in range(constants.shifts):
                    for n in range(len(db.get_doctors_list())):
                        if self.results_dictionary[(n,day_index,s)] == 1:
                            shift_and_doctor_labels.append(ttk.Label(scrollable_frame, text='{} {}'.format(db.get_doctors_list()[n].name, s+1), font=constants.Small_font ))
                            shift_and_doctor_labels[-1].grid(column=day_index-35, row=s+1+49, pady=10)
            elif day_index<45:
                day_labels.append(ttk.Label(scrollable_frame, text=db.get_startdate()+(day_index+16)*constants.delta, font=constants.Large_font))
                day_labels[-1].grid(row=56, column=day_index-40,padx=padx)
                for s in range(constants.shifts):
                    for n in range(len(db.get_doctors_list())):
                        if self.results_dictionary[(n,day_index,s)] == 1:
                            shift_and_doctor_labels.append(ttk.Label(scrollable_frame, text='{} {}'.format(db.get_doctors_list()[n].name, s+1), font=constants.Small_font ))
                            shift_and_doctor_labels[-1].grid(column=day_index-40, row=s+1+56, pady=10)
            elif day_index<50:
                day_labels.append(ttk.Label(scrollable_frame, text=db.get_startdate()+(day_index+18)*constants.delta, font=constants.Large_font))
                day_labels[-1].grid(row=63, column=day_index-45,padx=padx)
                for s in range(constants.shifts):
                    for n in range(len(db.get_doctors_list())):
                        if self.results_dictionary[(n,day_index,s)] == 1:
                            shift_and_doctor_labels.append(ttk.Label(scrollable_frame, text='{} {}'.format(db.get_doctors_list()[n].name, s+1), font=constants.Small_font ))
                            shift_and_doctor_labels[-1].grid(column=day_index-45, row=s+1+63, pady=10)
            elif day_index<55:
                day_labels.append(ttk.Label(scrollable_frame, text=db.get_startdate()+(day_index+20)*constants.delta, font=constants.Large_font))
                day_labels[-1].grid(row=70, column=day_index-50,padx=padx)
                for s in range(constants.shifts):
                    for n in range(len(db.get_doctors_list())):
                        if self.results_dictionary[(n,day_index,s)] == 1:
                            shift_and_doctor_labels.append(ttk.Label(scrollable_frame, text='{} {}'.format(db.get_doctors_list()[n].name, s+1), font=constants.Small_font ))
                            shift_and_doctor_labels[-1].grid(column=day_index-50, row=s+1+70, pady=10)
            elif day_index<60:
                day_labels.append(ttk.Label(scrollable_frame, text=db.get_startdate()+(day_index+22)*constants.delta, font=constants.Large_font))
                day_labels[-1].grid(row=77, column=day_index-55,padx=padx)
                for s in range(constants.shifts):
                    for n in range(len(db.get_doctors_list())):
                        if self.results_dictionary[(n,day_index,s)] == 1:
                            shift_and_doctor_labels.append(ttk.Label(scrollable_frame, text='{} {}'.format(db.get_doctors_list()[n].name, s+1), font=constants.Small_font ))
                            shift_and_doctor_labels[-1].grid(column=day_index-55, row=s+1+77, pady=10)

            days_left-=1
            day_index+=1

        #following block is designing the doctor view
        doctor_name_labels=[]
        pa_and_pp_labels=[]
        targetpa_and_targetpp_labels=[]
        differene_labels=[]
        for n in range(len(db.get_doctors_list())):
            doctor_name_labels.append(ttk.Label(doctor_tab, text=db.get_doctors_list()[n].name, font=constants.Large_font))

            totalPA = 0
            totalPP=0
            for d in range(constants.days):
                for  s in range(constants.shifts):
                    totalPA = totalPA + self.results_dictionary[(n,d,s)]*constants.pamatrix[d][s]
                    totalPP+=self.results_dictionary[(n,d,s)]*constants.ppmatrix[d][s]
            totalPA=totalPA/constants.scale_factor
            totalPP=totalPP/constants.scale_factor
            targetPA=db.get_doctors_list()[n].get_targetPA()
            targetPP=db.get_doctors_list()[n].get_targetPP()

            pa_and_pp_labels.append(ttk.Label(doctor_tab, text="Total PA: {}   Total PP: {}".format(totalPA, totalPP), font=constants.Small_font))
            targetpa_and_targetpp_labels.append(ttk.Label(doctor_tab, text="Target PA: {}   Target PP: {}".format(targetPA,targetPP), font=constants.Small_font))
            differene_labels.append(ttk.Label(doctor_tab, text="Difference PA: {}   Difference PP: {}".format(round(totalPA-targetPA,2), totalPP-targetPP), font=constants.Small_font, style='red.TLabel'))
            if n<5:
                doctor_name_labels[-1].grid(row=0, column=n, padx=padx1, pady=10)
                pa_and_pp_labels[-1].grid(row=1, column=n, padx=padx1, pady=10)
                targetpa_and_targetpp_labels[-1].grid(row=2, column=n, padx=padx1, pady=10)
                differene_labels[-1].grid(row=3, column=n, padx=padx1, pady=10)
            elif n<10:
                doctor_name_labels[-1].grid(row=4, column=n-5, padx=padx1, pady=10)
                pa_and_pp_labels[-1].grid(row=5, column=n-5, padx=padx1, pady=10)
                targetpa_and_targetpp_labels[-1].grid(row=6, column=n-5, padx=padx1, pady=10)
                differene_labels[-1].grid(row=7, column=n-5, padx=padx1, pady=10)
            else:
                doctor_name_labels[-1].grid(row=8, column=n-10, padx=padx1, pady=10)
                pa_and_pp_labels[-1].grid(row=9, column=n-10, padx=padx1, pady=10)
                targetpa_and_targetpp_labels[-1].grid(row=10, column=n-10, padx=padx1, pady=10)
                differene_labels[-1].grid(row=11, column=n-10, padx=padx1, pady=10)
            
        #print(total/constants.scale_factor, targetpa[n]/constants.scale_factor, (total-targetpa[n])/constants.scale_factor)
            
           


    def set_results_dictionary(self, results_dictionary):
        self.results_dictionary=results_dictionary

