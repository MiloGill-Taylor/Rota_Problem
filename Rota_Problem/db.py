import pickle
import datetime


lst_of_doctors=[]

def get_doctors_list():
    return lst_of_doctors



startdate=datetime.date(2000,1,3)

def get_startdate():
    return startdate



def pickleData():
    pickle_out1=open("doctors_list.pickle","wb")
    pickle.dump(lst_of_doctors, pickle_out1)
    pickle_out1.close()

    pickle_out2=open("startdate.pickle","wb")
    pickle.dump(startdate, pickle_out2)
    pickle_out2.close()

def unpickleDoctorData():
    pickle_in1=open("doctors_list.pickle", "rb")
    lst_of_doctors=pickle.load(pickle_in1)
    pickle_in1.close()
    return lst_of_doctors

def unpickleStartdateData():
    pickle_in1=open("startdate.pickle", "rb")
    startdate=pickle.load(pickle_in1)
    pickle_in1.close()
    return startdate

