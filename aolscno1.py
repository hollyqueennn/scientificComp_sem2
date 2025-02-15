# -*- coding: utf-8 -*-
"""aolsc1a.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qG9J_EPzdZMXu_dysR6pUzHz7vpZqIij

**A**
"""

from scipy.interpolate import interp1d, interpolate
from scipy.interpolate import CubicSpline
import numpy as np
import matplotlib.pyplot as plt

x = [1981, 1983, 1985, 1987, 1989, 1991, 1993, 1995, 1997, 1999]
y = [14.1999, 14.2411, 14.0342, 14.2696, 14.197, 14.3055, 14.1835,
     14.3577, 14.4187, 14.3438]

"""**Linear Interpolation**"""

f_linear = interp1d(x, y)
print("Temperature Estimate (Linear Interpolation) : ")
for year in range(1982, 2000, 2) :
  y_hat = f_linear(year)
  print("Year", year, ":", format(y_hat, ".4f"), "°C")

"""**Quadratic Interpolation**"""

f_quadra = interp1d(x, y, kind = 'quadratic')
x_quadra = np.arange(1982, 2000, 2)
y_quadra = f_quadra(x_quadra)
print("Temperature Estimate (Quadratic Interpolation) : ")
for i in range(len(x_quadra)):
    print("Year", x_quadra[i], ":", "{:.4f}".format(y_quadra[i]), "°C")

"""**Cubic Spline Interpolation**"""

f_cubicSpline = CubicSpline(x, y, bc_type = "natural")
x_cs = np.array([1982, 1984, 1986, 1988, 1990, 1992, 1994, 1996, 1998])
y_cs = f_cubicSpline(x_cs)
print("Temperature Estimate (Cubic Spline Interpolation) : ")
for j in range(len(x_cs)) :
  print("Year", x_cs[j], ":", "{:.4f}" .format(y_cs[j]), "°C")

plt.figure(figsize=(7, 5))
plt.plot(x, y, 'ro', label='Data')
x_linear = np.arange(1982, 2000, 2)
y_linear = f_linear(x_linear)
plt.plot(x_linear, y_linear, 'b', label='Linear Interpolation')
plt.plot(x_quadra, y_quadra, linestyle='dotted', color='orange', label='Quadratic Interpolation')
plt.plot(x_cs, y_cs, 'g--', label='Cubic Spline Interpolation')
plt.xlabel('Year(x)')
plt.ylabel('Temperature(y)')
plt.title('Temperature Interpolation')
plt.grid(color='black', linestyle='-', linewidth=0.2)
plt.legend()
plt.show()

"""**D**"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, CubicSpline
from sklearn.linear_model import LinearRegression

x= np.array([1981, 1983, 1985, 1987, 1989, 1991, 1993, 1995, 1997, 1999])
y = np.array([14.1999, 14.2411, 14.0342, 14.2696, 14.197, 14.3055, 14.1853, 14.3577, 14.4187, 14.3438])

x_even = np.arange(1982, 1999, 2)

y_linear = np.interp(x_even, x, y)

interpolation_quadratic = interp1d(x, y, kind='quadratic')
y_quadratic = interpolation_quadratic(x_even)

cs = CubicSpline(x, y)
y_cubic = cs(x_even)

regression = LinearRegression()
regression.fit(x.reshape(-1, 1), y)
y_regression = regression.predict(x_even.reshape(-1, 1))

plt.figure(figsize=(8, 6))
plt.plot(x, y, 'bo', label='Data')
plt.plot(x_even, y_linear, 'g-', label='Linear Interpolation')
plt.plot(x_even, y_quadratic, 'r-', label='Quadratic Interpolation')
plt.plot(x_even, y_cubic, 'm-', label='Cubic Spline Interpolation')
plt.plot(x_even, y_regression, 'y-', label='Least-Square Regression')
plt.xlabel('Year (x)')
plt.ylabel('Temperature (y)')
plt.title('The relationship between Temperature and Year')
plt.legend()
plt.grid(True)
plt.show()