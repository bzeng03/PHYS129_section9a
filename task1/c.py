import numpy as np
from scipy.integrate import quad
from b import integral

def integrand(x):
    return (x**3) / (np.exp(x) - 1)

# Perform the integration over [0, ∞]
integral2, error = quad(integrand, 0, np.inf)

# Constants for Stefan-Boltzmann Law Calculation
k = 1.38064852e-23  
h = 6.626e-34       
c = 3e8            

# Stefan-Boltzmann constant
sigma2 = 2 * np.pi * k**4 / c**2 / h**3 * integral2

print(f"Integral result: {integral2}")
print(f"Estimated Stefan-Boltzmann constant: {sigma2}")
print(f"Relative error: {integral / integral2}")