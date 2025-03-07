import numpy as np
import matplotlib.pyplot as plt
from a import explicit_Euler_method  # Assuming a.py contains the explicit Euler method

def symplectic_Euler_method(q1, q2, p1, p2, Tf, N):
    dt = Tf / N
    for _ in range(N):
        r = (q1[-1]**2 + q2[-1]**2)**(3/2)
        
        # Update velocity using Symplectic Euler method
        p1.append(p1[-1] - dt * q1[-1] / r)
        p2.append(p2[-1] - dt * q2[-1] / r)
        
        # Update position using new velocity
        q1.append(q1[-1] + dt * p1[-1])
        q2.append(q2[-1] + dt * p2[-1])

# Initialize parameters
e = 0.6
Tf, N_explicit, N_symplectic = 200, 100000, 400000

# Run explicit Euler method
q1_exp, q2_exp, p1_exp, p2_exp = [1 - e], [0], [0], [np.sqrt((1 + e) / (1 - e))]
explicit_Euler_method(q1_exp, q2_exp, p1_exp, p2_exp, Tf, N_explicit)

# Run symplectic Euler method
q1_symp, q2_symp, p1_symp, p2_symp = [1 - e], [0], [0], [np.sqrt((1 + e) / (1 - e))]
symplectic_Euler_method(q1_symp, q2_symp, p1_symp, p2_symp, Tf, N_symplectic)

# Plot both orbits
plt.figure(figsize=(8, 8))
plt.plot(q1_exp, q2_exp, label='Explicit Euler Orbit', color='orange', alpha=0.7)
plt.plot(q1_symp, q2_symp, label='Symplectic Euler Orbit', color='blue')
plt.scatter([0], [0], color='red', label='Star')  # Indicate the central star
plt.xlabel("q1")
plt.ylabel("q2")
plt.legend()
plt.title("Comparison of Explicit and Symplectic Euler Methods")
plt.grid()
plt.show()
plt.savefig("plot_b.png")