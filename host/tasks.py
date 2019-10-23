from oct2py import Oct2Py
import json

octave = Oct2Py()
octave.addpath('/multi/BENCHOP/RBF-FD')
# octave.addpath('/multi/BENCHOP/RBF-FD')
# octave.addpath('/multi/BENCHOP/RBF-FD')

def problem1(S, K, T, r, sig):
    re = octave.BSeuCallUI_RBFFD(S, K, T, r, sig)
    print('res: ', dir(octave))
    res = json.dumps(re.tolist())
    print('res:', res)
    return res
