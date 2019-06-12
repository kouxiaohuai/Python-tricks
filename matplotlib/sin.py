# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 10:04:58 2019

@author: kWX596514
"""

import numpy as np
import matplotlib.pyplot as plt

plt.xkcd()

print(plt.style.available)

plt.style.use('ggplot')

x = np.arange(0, 10, 0.1)
y = np.sin(x)

plt.plot(x, y, label='sin')
plt.xticks(np.linspace(0, 10, 11, endpoint=True))
plt.yticks(np.linspace(-1, 1, 11, endpoint=True))
plt.xlim([-2, 12])
plt.ylim([-1.2, 1.2])
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()
