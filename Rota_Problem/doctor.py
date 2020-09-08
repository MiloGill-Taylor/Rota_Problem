import db
import constants


class Doctor:

    def __init__(self): 

        self.name=None
        self.doA = None
        self.doB = None
        self.doC = None
        self.do3 = None
        self.doICU = None
        self.doSPIRE = None 
        self.days_can_work = {}
        days_left=constants.days
        day_index=0
        while days_left>0:
            print(day_index)
            if day_index<5:
                self.days_can_work[db.get_startdate()+day_index*constants.delta]=1
            elif day_index<10:
                self.days_can_work[db.get_startdate()+(day_index+2)*constants.delta]=1
            elif day_index<15:
                self.days_can_work[db.get_startdate()+(day_index+4)*constants.delta]=1
            elif day_index<20:
                self.days_can_work[db.get_startdate()+(day_index+6)*constants.delta]=1
            elif day_index<25:
                self.days_can_work[db.get_startdate()+(day_index+8)*constants.delta]=1
            elif day_index<30:
                self.days_can_work[db.get_startdate()+(day_index+10)*constants.delta]=1
            elif day_index<35:
                self.days_can_work[db.get_startdate()+(day_index+12)*constants.delta]=1
            elif day_index<40:
                self.days_can_work[db.get_startdate()+(day_index+14)*constants.delta]=1
            elif day_index<45:
                self.days_can_work[db.get_startdate()+(day_index+16)*constants.delta]=1
            elif day_index<50:
                self.days_can_work[db.get_startdate()+(day_index+18)*constants.delta]=1 
            elif day_index<55:
                self.days_can_work[db.get_startdate()+(day_index+20)*constants.delta]=1
            elif day_index<60:
                self.days_can_work[db.get_startdate()+(day_index+22)*constants.delta]=1
            
            days_left-=1
            day_index+=1
        self.targetPA = 0
        self.targetPP = 0
        self.id=len(db.lst_of_doctors)
        db.lst_of_doctors.append(self)
    
        
    def set_attributes(self, name, doA, doB, doC, do3, doICU, doSPIRE, targetPA, targetPP):
        self.name=name.title()
        self.doA=doA
        self.doB=doB
        self.do3=do3
        self.doC=doC
        self.doICU=doICU
        self.doSPIRE=doSPIRE
        if targetPA =='':
            self.targetPA=0.0
        else:
            self.targetPA=float(targetPA)
        if targetPP =='':
            self.targetPP=0.0
        else:
            self.targetPP=float(targetPP)

    def clear_attributes(self):
        self.name=None
        self.doA=None
        self.doB=None
        self.doC=None
        self.do3=None
        self.doICU=None
        self.doSPIRE=None
        self.targetPA=0
        self.targetPP=0
        self.days_can_work = {}
        days_left=constants.days
        day_index=0
        while days_left>0:
            print(day_index)
            if day_index<5:
                self.days_can_work[db.get_startdate()+day_index*constants.delta]=1
            elif day_index<10:
                self.days_can_work[db.get_startdate()+(day_index+2)*constants.delta]=1
            elif day_index<15:
                self.days_can_work[db.get_startdate()+(day_index+4)*constants.delta]=1
            elif day_index<20:
                self.days_can_work[db.get_startdate()+(day_index+6)*constants.delta]=1
            elif day_index<25:
                self.days_can_work[db.get_startdate()+(day_index+8)*constants.delta]=1
            elif day_index<30:
                self.days_can_work[db.get_startdate()+(day_index+10)*constants.delta]=1
            elif day_index<35:
                self.days_can_work[db.get_startdate()+(day_index+12)*constants.delta]=1
            elif day_index<40:
                self.days_can_work[db.get_startdate()+(day_index+14)*constants.delta]=1
            elif day_index<45:
                self.days_can_work[db.get_startdate()+(day_index+16)*constants.delta]=1
            elif day_index<50:
                self.days_can_work[db.get_startdate()+(day_index+18)*constants.delta]=1 
            elif day_index<55:
                self.days_can_work[db.get_startdate()+(day_index+20)*constants.delta]=1
            elif day_index<60:
                self.days_can_work[db.get_startdate()+(day_index+22)*constants.delta]=1
            
            days_left-=1
            day_index+=1

    def set_day_off_work(self, day):
        if day in self.days_can_work.keys():
            self.days_can_work[day]=0
        else: 
            print("Date selected out of range")
    
    
    def get_targetPA(self):
        return self.targetPA

    def get_targetPP(self):
        return self.targetPP
    
    def get_schedule(self):
    # Creating daily list
        daily_list=[]
        if self.doA == True:
            daily_list.append(1)
        else:
            daily_list.append(0)
        if self.doB==True:
            daily_list.append(1)
        else:
            daily_list.append(0)
        if self.doC==True:
            daily_list.append(1)
        else:
            daily_list.append(0)
        if self.do3==True:
            daily_list.append(1)
        else:
            daily_list.append(0)
        if self.doICU==True:
            daily_list.append(1)
        else:
            daily_list.append(0)
        if self.doSPIRE ==True:
            daily_list.append(1)
        else:
            daily_list.append(0)
        schedule=[]
        modified_days_can_work=[]
        for key in self.days_can_work:
            modified_days_can_work.append(self.days_can_work[key])
        for i in range(constants.days):
            if modified_days_can_work[i]==1:
                schedule.append(daily_list)
            else:
                schedule.append([0 for i in range(constants.shifts)])
        return schedule 
    
    def destroy_doctor(self):
        db.get_doctors_list().remove(self)

