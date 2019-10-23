from oct2py import Oct2Py
import json

octave = Oct2Py()
octave.addpath('/Users/andreasivarsson/multi-cloud/BENCHOP/RBF-FD')


def problem1(S, K, T, r, sig):
    print('problem1')
    res = json.dumps(octave.BSeuCallUI_RBFFD(S, K, T, r, sig).tolist())
    print('res:', res)
    return res
