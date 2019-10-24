from celery import Celery
import celery
from oct2py import Oct2Py
import json
import time
import operator

def schedule(solver_name, problem_id, parameters):

    result = None
    octave = Oct2Py()
    octave.addpath('/multi/BENCHOP/RBF-FD')
    octave.addpath('/multi/BENCHOP/COS')
    octave.addpath('/multi/BENCHOP/FD')

    U = None
    exec_time = time.time()

    if problem_id=="1":

        U = [ 2.758443856146076, 7.485087593912603,14.702019669720769 ]

        try:
            S = [90, 100, 110] if parameters.get('S') is None else list(map(float,parameters['S'].split(',')))
            K = 100 if parameters.get('K') is None else float(parameters['K'])
            T = 1 if parameters.get('T') is None else float(parameters['T'])
            r = 0.03 if parameters.get('r') is None else float(parameters['r'])
            sig = 0.15 if parameters.get('sig') is None else float(parameters['sig'])
        except:
            return json.dumps({'failure':False,'error':"Wrong input arguments for choice of solver {}".format(solver_name)})

        try:
            if solver_name=="COS":
                result = octave.BSeuCallUI_COS(S, K, T, r, sig)
            elif solver_name=="RBFFD":
                result = octave.BSeuCallUI_RBFFD(S, K, T, r, sig)
            elif solver_name=="FD":
                result = octave.BSeuCallUI_UniformGrid(S, K, T, r, sig)
        except:
            return json.dumps({'failure':False,'error':"Solver crashed {}".format(solver_name)})


    elif problem_id=="2":

        U = [ 10.726486710094511, 4.820608184813253, 1.828207584020458 ]

        try:
            S = [90, 100, 110] if parameters.get('S') is None else list(map(float,parameters['S'].split(',')))
            K = 100 if parameters.get('K') is None else float(parameters['K'])
            T = 1 if parameters.get('T') is None else float(parameters['T'])
            r = 0.03 if parameters.get('r') is None else float(parameters['r'])
            sig = 0.15 if parameters.get('sig') is None else float(parameters['sig'])
        except:
            return json.dumps({'failure':False,'error':"Wrong input arguments for choice of solver {}".format(solver_name)})

        try:
            if solver_name=="COS":
                result = octave.BSamPutUI_COS(S, K, T, r, sig)
            elif solver_name=="RBFFD":
                result = octave.BSamPutUI_RBFFD(S, K, T, r, sig)
            elif solver_name=="FD":
                result = octave.BSamPutUI_UniformGrid(S, K, T, r, sig)
        except:
            return json.dumps({'failure':False,'error':"Solver crashed {}".format(solver_name)})


    elif problem_id=="3":

        U = [ 1.822512255945242, 3.294086516281595, 3.221591131246868 ]

        try:
            S = [90, 100, 110] if parameters.get('S') is None else list(map(float,parameters['S'].split(',')))
            K = 100 if parameters.get('K') is None else float(parameters['K'])
            B = 1.25*K if parameters.get('B') is None else float(parameters['B'])
            T = 1 if parameters.get('T') is None else float(parameters['T'])
            r = 0.03 if parameters.get('r') is None else float(parameters['r'])
            sig = 0.15 if parameters.get('sig') is None else float(parameters['sig'])
        except:
            return json.dumps({'failure':False,'error':"Wrong input arguments for choice of solver {}".format(solver_name)})

        try:
            if solver_name=="COS":
                result = octave.BSupoutCallI_COS(S, K, T, r, sig, B)
            elif solver_name=="RBFFD":
                result = octave.BSupoutCallI_RBFFD(S, K, T, r, sig, B)
            elif solver_name=="FD":
                result = octave.BSupoutCallI_UniformGrid(S, K, T, r, sig, B)
        except:
            return json.dumps({'failure':False,'error':"Solver crashed {}".format(solver_name)})

    elif problem_id=="4":

        U = [ 0.033913177006141, 0.512978189232598, 1.469203342553328 ]

        try:
            S = [97, 98, 99] if parameters.get('S') is None else list(map(float,parameters['S'].split(',')))
            K = 100 if parameters.get('K') is None else float(parameters['K'])
            T = 0.25 if parameters.get('T') is None else float(parameters['T'])
            r = 0.1 if parameters.get('r') is None else float(parameters['r'])
            sig = 0.01 if parameters.get('sig') is None else float(parameters['sig'])
        except:
            return json.dumps({'failure':False,'error':"Wrong input arguments for choice of solver {}".format(solver_name)})

        try:
            if solver_name=="COS":
                result = octave.BSeuCallUII_COS(S, K, T, r, sig)
            elif solver_name=="RBFFD":
                result = octave.BSeuCallUII_RBFFD(S, K, T, r, sig)
            elif solver_name=="FD":
                result = octave.BSeuCallUII_UniformGrid(S, K, T, r, sig)
        except:
            return json.dumps({'failure':False,'error':"Solver crashed {}".format(solver_name)})

    elif problem_id=="5":

        U = [ 3.000000000000682, 2.000000000010786, 1.000000000010715 ]

        try:
            S = [97, 98, 99] if parameters.get('S') is None else list(map(float,parameters['S'].split(',')))
            K = 100 if parameters.get('K') is None else float(parameters['K'])
            T = 0.25 if parameters.get('T') is None else float(parameters['T'])
            r = 0.1 if parameters.get('r') is None else float(parameters['r'])
            sig = 0.01 if parameters.get('sig') is None else float(parameters['sig'])
        except:
            return json.dumps({'failure':False,'error':"Wrong input arguments for choice of solver {}".format(solver_name)})

        try:
            if solver_name=="COS":
                result = octave.BSamPutUII_COS(S, K, T, r, sig)
            elif solver_name=="RBFFD":
                result = octave.BSamPutUII_RBFFD(S, K, T, r, sig)
            elif solver_name=="FD":
                result = octave.BSamPutUII_UniformGrid(S, K, T, r, sig)
        except:
            return json.dumps({'failure':False,'error':"Solver crashed {}".format(solver_name)})

    elif problem_id=="6":

        U = [ 0.033913177006134, 0.512978189232598, 1.469203342553328]

        try:
            S = [97, 98, 99] if parameters.get('S') is None else list(map(float,parameters['S'].split(',')))
            K = 100 if parameters.get('K') is None else float(parameters['K'])
            B = 1.25*K if parameters.get('B') is None else float(parameters['B'])
            T = 0.25 if parameters.get('T') is None else float(parameters['T'])
            r = 0.1 if parameters.get('r') is None else float(parameters['r'])
            sig = 0.01 if parameters.get('sig') is None else float(parameters['sig'])
        except:
            return json.dumps({'failure':False,'error':"Wrong input arguments for choice of solver {}".format(solver_name)})

        try:
            if solver_name=="COS":
                result = octave.BSupoutCallII_COS(S, K, T, r, sig, B)
            elif solver_name=="RBFFD":
                result = octave.BSupoutCallII_RBFFD(S, K, T, r, sig, B)
            elif solver_name=="FD":
                result = octave.BSupoutCallII_UniformGrid(S, K, T, r, sig, B)
        except:
            return json.dumps({'failure':False,'error':"Solver crashed {}".format(solver_name)})

    exec_time = time.time() - exec_time

    if result is None:
        return json.dumps({'failure':True,'error':'your task failed'})

    res_list = result.tolist()
    map(operator.sub, U, res_list)
    map(operator.abs, res_list)
    return json.dumps({'failure':False, 'result':res_list, 'time': exec_time})
