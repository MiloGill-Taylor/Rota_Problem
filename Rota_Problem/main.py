import os.path as fileCheck
import tkinter as tk
from tkinter import ttk
import constants
import db
import datetime






#List of current doctors
if fileCheck.exists("doctors_list.pickle"):
    db.lst_of_doctors= db.unpickleDoctorData()
    
else:
    db.lst_of_doctors=[]
    

if fileCheck.exists("startdate.pickle"):
    db.startdate= db.unpickleStartdateData()
else:
    db.startdate=datetime.date(2000,1,3)


#importing pages
from create_doctor_page import CreateDoctorPage
from results_page import Results
from start_page import StartPage
from edit_doctor import EditDoctorPage
   


#function that is called when the x button is clicked
def on_closing():
    db.pickleData()
    app.destroy()


class RotaScheduleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        container=tk.Frame(self)
        s=ttk.Style()
        s.configure('TLabel', background='white')
        s.configure('TFrame', background='white')
        s.configure('red.TLabel', foreground='red')
        container.pack(side="top", fill = "both", expand = True)
        
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames={}
        mytuple=(StartPage, Results, CreateDoctorPage, EditDoctorPage)
        for i in range(len(mytuple)):

            frame=mytuple[i](container, self)
            
            self.frames[i]=frame

            frame.grid(row=0, column = 0, sticky = "nsew")
        
        #start page is key 0, results is key 1, create doctor page is key 2 and edit doctor page is key3

        self.show_frame(0)

        self._geom='600x600+0+0'
        self.geometry("{0}x{1}+0+0".format(
            self.winfo_screenwidth()-3, self.winfo_screenheight()-3))
        self.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.winfo_geometry()
        print(geom,self._geom)
        self.geometry(self._geom)
        self._geom=geom

    def show_frame(self, key):
        frame=self.frames[key]
        frame.display_content()
        frame.tkraise()
        

    
app = RotaScheduleApp()
app.title('Rota Scheduling Application')

app.protocol("WM_DELETE_WINDOW", on_closing)


app.mainloop()
