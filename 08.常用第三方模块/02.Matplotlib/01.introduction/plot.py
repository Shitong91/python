#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
#导入模块matplotlib.pyplot,并简写成plt.
import numpy as np
x=np.linspace(-1,1,50)#定义x范围是(-1,1),个数是50
y=2*x+1
plt.figure()
plt.plot(x,y)
plt.show()

