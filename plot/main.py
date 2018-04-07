

import codecs
import math
import string
import sys
import time as t

import matplotlib.pyplot as plt
import numpy as np


def money_580(calltime=0):
    costpersecond=0.19
    call_long=150
    base_cost=18
    cost = (calltime*(calltime>call_long)+call_long*(calltime<=call_long) )*costpersecond+base_cost
    return cost

def money_38(calltime=0):
    costpersecond=0.19
    call_long=100
    base_cost=38
    cost = (calltime*(calltime>call_long)+call_long*(calltime<=call_long) )*costpersecond+base_cost
    return cost


t = np.arange(350)
x = money_38(t)
y = money_580(t)

p1 = plt.plot(t,x)
p2 = plt.plot(t,y)
p3 = plt.plot(t,x-y)

#plt.text(0.1,0.5, r"$\zeta(s) = \sum_{n=0}^{\infty}{\frac{1}{n^s}} $",fontsize=50)
plt.legend([p1,p2,p3],['38','580','diff'],loc='best')
plt.grid(True,linestyle='-',color=[0.9,0.9,0.9],linewidth=1)
plt.show()
