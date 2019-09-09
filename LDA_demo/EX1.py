# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

N = 5000;

lim_para = 5;
# [[3, 1],[1, 1]] would create a 2x2 matrix
A = [[1, 0.99],[0.99, 2]]
A_eig = np.linalg.eig(A)
# Now the Jordan decomposition Gamma*Lambda*Gamma^T
E_val = A_eig[0]
Gamma = A_eig[1]


Lambda12 = np.diag(np.sqrt(E_val))

sigma12 = np.dot( np.dot(Gamma, Lambda12), np.transpose(Gamma) )
A_estimated = np.dot(sigma12,sigma12.transpose())
delta = A - A_estimated;

norm_data_1 = np.random.normal(0, 1, N);
norm_data_2 = np.random.normal(0, 1, N);


tmp = np.vstack([norm_data_1,norm_data_2]).transpose()
tmp2 = np.dot(tmp,sigma12);

fig = plt.figure(figsize=(5,5)) # Create a window to draw
ax = plt.axes() # Create axes
#ax.plot(tmp[:,0], tmp[:,1], 'o')
plt.xlim(-lim_para, lim_para);
plt.ylim(-lim_para, lim_para);

ax.plot(tmp2[:,0], tmp2[:,1], 'o')

