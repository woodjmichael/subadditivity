# subadd.py
# subadditivity numerical example with plot
# python 3.7

__author__ = "Michael Wood"
__email__ = "woodjmichael@gmail.com"
__license__ = "GPL"
__version__ = "1.0"


import matplotlib.pyplot as plt
import numpy as np
import sys

#
L = 1500

# cost curve coefficients
a = 1
b = 1
c = 10000

# way to create different "tech" (cost curves) s.t. min(AC) is the same
k = 2

#
# Cost, Average Cost, Marginal Cost
#

# quantity
q = np.arange(5,L)

Ca = a*q**2 + b*q + c                       # tech A
Cb = (a/k)*q**2 + b*q + c*k                 # tech B
Cb2 = 2*((a/k)*(q/2)**2 + b*(q/2) + c*k)    # two firms with tech B

ACa = Ca/q
ACb = Cb/q
ACb2 = Cb2/q

MCa = 2*a*q + b


#
# Plots
#

fig, ax1 = plt.subplots(figsize=(20,8.3))

ax1.plot(q[40:250], ACa[40:250], label='AC one firm tech A')
ax1.plot(q[100:600], ACb[100:600], label='AC one firm tech B')
ax1.plot(q[200:1200], ACb2[200:1200], label='AC two firms tech B')

ax1.plot(q,-10*q+1000,label='demand 1')
ax1.plot(q,-10*q+2500,label='demand 2')
ax1.plot(q,-10*q+5000,label='demand 3')

ax1.plot(q,MCa,'--',label='MC one firm tech A')

ax1.set_xlim(0,L)
ax1.set_ylim(100,400)
ax1.set_xlabel('quantity')
ax1.set_ylabel('eur')

leg = ax1.legend();

plt.show()
