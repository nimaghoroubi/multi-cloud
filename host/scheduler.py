from celery import Celery
import celery
from oct2py import Oct2Py
import json

def schedule(solver_name, problem_id, parameters):
    result = None
    octave = Oct2Py()
    octave.addpath('/multi/BENCHOP/RBF-FD')
    octave.addpath('/multi/BENCHOP/COS')
    octave.addpath('/multi/BENCHOP/FD')

    if problem_id=="1":

        S = [90, 100, 110] if parameters.get('S') is None else parameters['S']
        K = 100 if parameters.get('K') is None else parameters['K']
        T = 1 if parameters.get('T') is None else parameters['T']
        r = 0.03 if parameters.get('r') is None else parameters['r']
        sig = 0.15 if parameters.get('sig') is None else parameters['sig']

        if solver_name=="COS":
            result = octave.BSeuCallUI_COS(S, K, T, r, sig)
        elif solver_name=="RBFFD":
            result = octave.BSeuCallUI_RBFFD(S, K, T, r, sig)
        elif solver_name=="FD":
            result = octave.BSeuCallUI_UniformGrid(S, K, T, r, sig)

    elif problem_id==2:

        return("this is solver 2")

    elif problem_id==3:
        return("this is solver 3")

    elif problem_id==4:
        return("this is solver 4")

    elif problem_id==5:
        return("this is solver 5")

    elif problem_id==6:
        return("this is solver 6")


    if result is None:
        return json.dumps({'failure':True})
    return json.dumps({'failure':False, 'result':result.tolist()})
