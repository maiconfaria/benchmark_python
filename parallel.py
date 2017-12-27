'''
Documentation, License etc.

@package parallel
'''

import numpy as np
import matplotlib.pyplot as plt
import time
from math import sqrt
from joblib import Parallel, delayed
from joblib.pool import has_shareable_memory


def square(x):
    return sqrt(x)
  
def rndarray(n):
    t = np.arange(n)
    a = np.random.rand(n)
    return t, a

def sinarray(n,f):
    t = np.arange(n)
    a = np.sin(f*t)
    return t, a

def FFT(t,a):
    b = np.fft.fft(a)
    f = np.fft.fftfreq(t.shape[-1])
    return f, b

def aaf(n,f):
    t = np.arange(n)
    a = np.sin(f*t)
    b = np.fft.fft(a)
    f = np.fft.fftfreq(t.shape[-1])
    return f, b

if __name__ == "__main__":
    n = 30000
    l = []
    
    type = "parallel"
    #type = "serial"
    
    if type=="serial":
	starttime = time.time()
	print type
	for v in np.arange(0.1,20.0,0.1):
	    t, a = sinarray(n, v)
	    f, b = FFT(t,a)
	    l.append((f, b))
	f, b = l[0]
	endtime = time.time()
	print(endtime-starttime)
    
    elif type=="parallel":
	print type
	starttime = time.time()
	l = Parallel(n_jobs=4)(delayed(aaf)(n,v) for v in np.arange(0.1,20.0,0.1))
	f, b = l[0]
	endtime = time.time()
	print(endtime-starttime)

    
    
    plt.plot(f, b.real, f, b.imag)
    plt.show()