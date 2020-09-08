from ortools.sat.python import cp_model
import time
import db
import constants

def brain():
    #start runtime
    start_time = time.time()

    #params to be changed
    max_time = constants.max_time
    shifts = constants.shifts
    days = constants.days
    num_docs = len(db.get_doctors_list())
    targetpa = [int(doctor.get_targetPA()*constants.scale_factor) for doctor in db.get_doctors_list()]
    targetpp = [int(doctor.get_targetPP()*constants.scale_factor) for doctor in db.get_doctors_list()]
    pabound = constants.pabound
    ppbound = constants.ppbound

   
    
    #fake schedule, can be deleted
    #schedule1 = [[1 for x in range(shifts)] for y in range(days)]

    schedulelist =[doctor.get_schedule() for doctor in db.get_doctors_list()]

    #define matrices of pa and pp (x100 multiplied for integer values)
    pamatrix = constants.pamatrix
    ppmatrix = constants.ppmatrix
   
    model = cp_model.CpModel()
    varmatrix = {}
    for n in range(num_docs):
        for d in range(days):
            for s in range(shifts):
                varmatrix[(n, d, s)] = model.NewBoolVar('shift_n%id%is%i' % (n, d, s))
                    
    #every shift must have exactly one doctor
    for d in range(days):
        for s in range(shifts):
            model.Add(sum(varmatrix[(n, d, s)] for n in range(num_docs)) == 1)
    
    #add hard constraints for all doctors         
    for n in range(num_docs):
        for d in range(len(schedulelist[n])):
            for i in range(shifts):
                if schedulelist[n][d][i] == 0:
                    model.Add(varmatrix[(n, d, i)] == 0)
                    
    #maximum number of shifts per doctor per day is 1
    for n in range(num_docs):
            for d in range(days):
                model.Add(sum(varmatrix[(n, d, s)] for s in range(shifts)) <= 1)

    #define cost function as difference
    pacost = sum(sum(varmatrix[(n,d,s)]*pamatrix[d][s] for d in range(days) for  s in range(shifts))-targetpa[n] for n in range (num_docs))
    ppcost =  sum(sum(varmatrix[(n,d,s)]*ppmatrix[d][s] for d in range(days) for  s in range(shifts))-targetpp[n] for n in range (num_docs))
    padifference=0
    for i in reversed(range(num_docs)):
        for j in reversed(range(i)):
            padifference += sum(varmatrix[(i,d,s)]*pamatrix[d][s] for d in range(days) for  s in range(shifts)) - sum(varmatrix[(j,d,s)]*pamatrix[d][s] for d in range(days) for  s in range(shifts))

    model.Minimize(pacost+ppcost)

    #have two bounds and set the difference to not be too negative
    for n in range (num_docs):
        model.Add((sum(varmatrix[(n,d,s)]*pamatrix[d][s] for d in range(days) for  s in range(shifts))-targetpa[n]) > -pabound)
        model.Add((sum(varmatrix[(n,d,s)]*ppmatrix[d][s] for d in range(days) for  s in range(shifts))-targetpp[n]) > -ppbound)
        
        
    #solve
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = max_time
    solver.Solve(model)
    

    #print sched
    """
    for d in range(days):
        print('day:' ,d+1)
        for s in range(shifts):
            for n in range(num_docs):
                if solver.Value(varmatrix[(n,d,s)]) == 1:
                    print('doctor ', n+1, ' works ', s+1)

    #print pa, targetpa, difference
    
    for n in range (num_docs):
        total = 0
        for d in range(days):
            for  s in range(shifts):
                total = total + solver.Value(varmatrix[(n,d,s)])*pamatrix[d][s]
        print(total/constants.scale_factor, targetpa[n]/constants.scale_factor, (total-targetpa[n])/constants.scale_factor)

    for n in range (num_docs):
        total = 0
        for d in range(days):
            for  s in range(shifts):
                total = total + solver.Value(varmatrix[(n,d,s)])*ppmatrix[d][s]
        print(total/constants.scale_factor, targetpp[n]/constants.scale_factor, (total-targetpp[n])/constants.scale_factor)
    #output runtime
    print("--- %s seconds ---" % (time.time() - start_time))

    """
    #creating the results dictionary we want
    results_dictionary={}
    for key in varmatrix:
        results_dictionary[key]=solver.Value(varmatrix[key])

    return results_dictionary