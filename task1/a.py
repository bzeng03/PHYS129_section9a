import numpy as np
from scipy.integrate import quad, fixed_quad

def integrand(z):
    x = z / (1 - z)
    return (z**3) / ((1 - z)**5 * (np.exp(x) - 1))

# Perform the integration over [0,1]
integral, error = fixed_quad(integrand, 0, 1)

print(f"Integral result: {integral}")