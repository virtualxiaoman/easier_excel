###############
# Authored by Weisheng Jiang
# Book 4  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############

# Bk4_Ch17_01.py

import sympy
import numpy as np
from sympy.functions import exp

# define symbolic vars, function
x1, x2 = sympy.symbols('x1 x2')

f_x = x1 * exp(-(x1 ** 2 + x2 ** 2))

print(f_x)

# take the gradient symbolically
grad_f = [sympy.diff(f_x, var) for var in (x1, x2)]
print(grad_f)

f_x_fcn = sympy.lambdify([x1, x2], f_x)

# turn into a bivariate lambda for numpy
grad_fcn = sympy.lambdify([x1, x2], grad_f)

import matplotlib.pyplot as plt

xx1, xx2 = np.meshgrid(np.linspace(-2, 2, 40), np.linspace(-2, 2, 40))

# coarse mesh
xx1_, xx2_ = np.meshgrid(np.linspace(-2, 2, 20), np.linspace(-2, 2, 20))
V = grad_fcn(xx1_, xx2_)

ff_x = f_x_fcn(xx1, xx2)

color_array = np.sqrt(V[0] ** 2 + V[1] ** 2)

# 3D visualization
ax = plt.figure().add_subplot(projection='3d')
ax.plot_wireframe(xx1, xx2, ff_x, rstride=1,
                  cstride=1, color=[0.5, 0.5, 0.5],
                  linewidth=0.2)
ax.contour3D(xx1, xx2, ff_x, 20, cmap='RdBu_r')

ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])
ax.zaxis.set_ticks([])
plt.xlim(-2, 2)
plt.ylim(-2, 2)
ax.view_init(30, -125)
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_zlabel('$f(x_1,x_2)$')
plt.tight_layout()

# 2D visualization
fig, ax = plt.subplots()

plt.contourf(xx1, xx2, ff_x, 20, cmap='RdBu_r')

plt.quiver(xx1_, xx2_, V[0], V[1],
           angles='xy', scale_units='xy',
           edgecolor='none', facecolor='k')

plt.show()
ax.set_aspect('equal')
ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
plt.tight_layout()
