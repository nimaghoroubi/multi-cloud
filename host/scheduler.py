from celery import Celery
import celery
from oct2py import Oct2Py
import json

def schedule(solver_name, problem_id, parameters):
    return json.dumps({'failure':False,'result':"it works"})
    
    octave = Oct2Py()
    octave.addpath('/multi/BENCHOP/RBF-FD')
    octave.addpath('/multi/BENCHOP/COS')
    octave.addpath('/multi/BENCHOP/FD')

    if problem_id==1:

        parameters['S'] = [90, 100, 110] if S is None else S
        K = 100 if K is None else K
        T = 1 if T is None else T
        r = 0.03 if r is None else r
        sig = 0.15 if sig is None else sig

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
