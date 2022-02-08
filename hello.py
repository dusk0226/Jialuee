# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 23:51:45 2022

@author: Lenovo
"""
import math
import matplotlib.pyplot as plt
# this is the change of lingxiao
# print('hello world')

GRAVITY= 0.98
theta = math.pi/4

v0=1
uy = v0*math.sin(theta)
ux = v0*math.cos(theta)

ay = -GRAVITY

t = [0.01*n for n in range(100)]
y = [uy*ti + 1/2*ay*ti**2 for ti in t]
x = [ux*ti for ti in t]

plt.plot(x, y, linewidth=3, color='black')
plt.xlabel(r'$x\,(\mathrm{m})$')
plt.ylabel(r'$y\,(\mathrm{m})$', rotation=0)
plt.title('Trajectory of projectile')
plt.xlim([0, 0.7])
plt.ylim([0, 0.3])

plt.savefig('plot1.svg')

plt.show()


