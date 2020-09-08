import datetime 

#miscalaneous stuff
scale_factor=100


#number of days that we are scheduling for
days=60 #do not exceed 60 without updating doctor class
shifts=6
delta = datetime.timedelta(days=1)

#peformance parameters
pabound = int(120*scale_factor)
ppbound = int(30*scale_factor)
max_time=60

#fonts
Large_font=("Verdana", 20)
Small_font=("Verdana",15)



pamatrix = [[1 for x in range(shifts)] for y in range(days)]
for i in range (days):
    day = i%5
    for j in range(shifts):
                    #pa = 3.5 for shifts 1-4, 2.5 shift 5, shift 6 = 0, except tuesday-friday shift 1 = 2.9
        if (day != 0 and j == 0):
            pa = int(2.9*scale_factor)
        elif (j <= 3):
            pa = int(3.5*scale_factor)
        elif(j == 4):
            pa = int(2.5*scale_factor)
        elif(j == 5):
            pa = int(0*scale_factor)                          
                            
        pamatrix[i][j] = pa      

ppmatrix = [[1 for x in range(shifts)] for y in range(days)]
for i in range(days):
    day=i%5
    for j in range(shifts):
        if j==5 and day in {0,2,4}:
            pp=int(3*scale_factor)
        else:
            pp=int(0*scale_factor)
        ppmatrix[i][j]=pp

#dictionary of shift names
shift_names={1: "Theatre A", 2:"Theatre B", 3:"Theatre C", 4:"Theatre 3", 5:"Theatre ICU", 6:"Theatre Spire"}