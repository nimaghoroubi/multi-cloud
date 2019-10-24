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

        try:
            S = [90, 100, 110] if parameters.get('S') is None else list(map(float,parameters['S'].split(',')))
            K = 100 if parameters.get('K') is None else float(parameters['K'])
            T = 1 if parameters.get('T') is None else float(parameters['T'])
            r = 0.03 if parameters.get('r') is None else float(parameters['r'])
            sig = 0.15 if parameters.get('sig') is None else float(parameters['sig'])
        except:
            return json.dumps({'failure':False,'error':"Wrong input arguments for choice of solver {}".format(solver_name)})

        if solver_name=="COS":
            result = octave.BSeuCallUI_COS(S, K, T, r, sig)
        elif solver_name=="RBFFD":
            result = octave.BSeuCallUI_RBFFD(S, K, T, r, sig)
        elif solver_name=="FD":
            result = octave.BSeuCallUI_UniformGrid(S, K, T, r, sig)

    elif problem_id=="2":

        try:
            S = [90, 100, 110] if parameters.get('S') is None else list(map(float,parameters['S'].split(',')))
            K = 100 if parameters.get('K') is None else float(parameters['K'])
            T = 1 if parameters.get('T') is None else float(parameters['T'])
            r = 0.03 if parameters.get('r') is None else float(parameters['r'])
            sig = 0.15 if parameters.get('sig') is None else float(parameters['sig'])
        except:
            return json.dumps({'failure':False,'error':"Wrong input arguments for choice of solver {}".format(solver_name)})

        if solver_name=="COS":
            result = octave.BSamPutUI_COS(S, K, T, r, sig)
        elif solver_name=="RBFFD":
            result = octave.BSamPutUI_RBFFD(S, K, T, r, sig)
        elif solver_name=="FD":
            result = octave.BSamPutUI_UniformGrid(S, K, T, r, sig)


    elif problem_id=="3":

        try:
            S = [90, 100, 110] if parameters.get('S') is None else list(map(float,parameters['S'].split(',')))
            K = 100 if parameters.get('K') is None else float(parameters['K'])
            B = 1.25*K if parameters.get('B') is None else float(parameters['B'])
            T = 1 if parameters.get('T') is None else float(parameters['T'])
            r = 0.03 if parameters.get('r') is None else float(parameters['r'])
            sig = 0.15 if parameters.get('sig') is None else float(parameters['sig'])
        except:
            return json.dumps({'failure':False,'error':"Wrong input arguments for choice of solver {}".format(solver_name)})


        if solver_name=="COS":
            result = octave.BSupoutCallI_COS(S, K, T, r, sig, B)
        elif solver_name=="RBFFD":
            result = octave.BSupoutCallI_RBFFD(S, K, T, r, sig, B)
        elif solver_name=="FD":
            result = octave.BSupoutCallI_UniformGrid(S, K, T, r, sig, B)

    elif problem_id=="4":

        try:
            S = [97, 98, 99] if parameters.get('S') is None else list(map(float,parameters['S'].split(',')))
            K = 100 if parameters.get('K') is None else float(parameters['K'])
            T = 0.25 if parameters.get('T') is None else float(parameters['T'])
            r = 0.1 if parameters.get('r') is None else float(parameters['r'])
            sig = 0.01 if parameters.get('sig') is None else float(parameters['sig'])
        except:
            return json.dumps({'failure':False,'error':"Wrong input arguments for choice of solver {}".format(solver_name)})

        if solver_name=="COS":
            result = octave.BSeuCallUII_COS(S, K, T, r, sig)
        elif solver_name=="RBFFD":
            result = octave.BSeuCallUII_RBFFD(S, K, T, r, sig)
        elif solver_name=="FD":
            result = octave.BSeuCallUII_UniformGrid(S, K, T, r, sig)

    elif problem_id=="5":

        try:
            S = [97, 98, 99] if parameters.get('S') is None else list(map(float,parameters['S'].split(',')))
            K = 100 if parameters.get('K') is None else float(parameters['K'])
            T = 0.25 if parameters.get('T') is None else float(parameters['T'])
            r = 0.1 if parameters.get('r') is None else float(parameters['r'])
            sig = 0.01 if parameters.get('sig') is None else float(parameters['sig'])
        except:
            return json.dumps({'failure':False,'error':"Wrong input arguments for choice of solver {}".format(solver_name)})

        if solver_name=="COS":
            result = octave.BSamPutUII_COS(S, K, T, r, sig)
        elif solver_name=="RBFFD":
            result = octave.BSamPutUII_RBFFD(S, K, T, r, sig)
        elif solver_name=="FD":
            result = octave.BSamPutUII_UniformGrid(S, K, T, r, sig)

    elif problem_id=="6":

        try:
            S = [97, 98, 99] if parameters.get('S') is None else list(map(float,parameters['S'].split(',')))
            K = 100 if parameters.get('K') is None else float(parameters['K'])
            B = 1.25*K if parameters.get('B') is None else float(parameters['B'])
            T = 0.25 if parameters.get('T') is None else float(parameters['T'])
            r = 0.1 if parameters.get('r') is None else float(parameters['r'])
            sig = 0.01 if parameters.get('sig') is None else float(parameters['sig'])
        except:
            return json.dumps({'failure':False,'error':"Wrong input arguments for choice of solver {}".format(solver_name)})

        if solver_name=="COS":
            result = octave.BSupoutCallII_COS(S, K, T, r, sig, B)
        elif solver_name=="RBFFD":
            result = octave.BSupoutCallII_RBFFD(S, K, T, r, sig, B)
        elif solver_name=="FD":
            result = octave.BSupoutCallII_UniformGrid(S, K, T, r, sig, B)




    if result is None:
        return json.dumps({'failure':True,'error':'your task failed'})
    return json.dumps({'failure':False, 'result':result.tolist()})
