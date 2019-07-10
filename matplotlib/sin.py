# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 10:04:58 2019

@author: kWX596514
"""

import numpy as np
import matplotlib.pyplot as plt


plt.style.use('ggplot')
fig, ax = plt.subplots(nrows=3, ncols=1)

f = 15*10**3
omega = 2*np.pi*f
tau = 1/f
x_T = np.arange(0, tau, 0.001*tau)
y_T_sum = 0
for i in range(4):
    y_T = np.sin((i+1)*omega*x_T)
    y_T_sum += y_T
    ax[0].plot(x_T, y_T, label=f'sin({i+1}ωx)')

ax[0].legend()
ax[0].set_xlabel('x')
ax[0].set_ylabel('y')
ax[0].set_xticks(np.linspace(0, tau, 17, endpoint=True))

ax[1].set_xlabel('x')
ax[1].set_ylabel('y_sum')
ax[1].set_xticks(np.linspace(0, tau, 17, endpoint=True))
ax[1].plot(x_T, y_T_sum, color='black')

x_F = np.arange(-8*f, 8*f, 0.01*f)
for i in range(4):
    y_F_1 = np.sin(np.pi*tau*(x_F-(i+1)*f))/(np.pi*tau*(x_F-(i+1)*f))
    y_F_2 = np.sin(np.pi*tau*(x_F+(i+1)*f))/(np.pi*tau*(x_F+(i+1)*f))
    ax[2].plot(x_F, y_F_1)
    ax[2].plot(x_F, y_F_2)

ax[2].legend()
ax[2].set_xticks(np.linspace(-8*f, 8*f, 17, endpoint=True))
