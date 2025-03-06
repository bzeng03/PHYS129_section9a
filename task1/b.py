from a import integral
import numpy as np

# Constants for Stefan-Boltzmann Law Calculation
k = 1.38064852e-23  
h = 6.626e-34      
c = 3e8        

sigma = 2 * np.pi * k**4 / c**2 / h**3 * integral

print(f"Stefan-Boltzmann constant: {sigma}")