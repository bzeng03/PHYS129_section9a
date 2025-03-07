import numpy as np
import matplotlib.pyplot as plt

e = 0.6

q1 = [1 - e]
q2 = [0]
p1 = [0]
p2 = [np.sqrt((1 + e) / (1 - e))]

def explicit_Euler_method(q1, q2, p1, p2, Tf, N):
    dt = Tf / N
    for _ in range(N):
        r = (q1[-1]**2 + q2[-1]**2)**(3/2)
        
        # Compute accelerations
        a1, a2 = -q1[-1] / r, -q2[-1] / r
        
        # Update position using Euler's method
        q1.append(q1[-1] + dt * p1[-1])
        q2.append(q2[-1] + dt * p2[-1])
        
        # Update velocity using Euler's method
        p1.append(p1[-1] + dt * a1)
        p2.append(p2[-1] + dt * a2)
        
        

# Run the simulation
Tf = 200
N = 100000
explicit_Euler_method(q1, q2, p1, p2, Tf, N)

# Plot the orbit
plt.figure(figsize=(8, 8))
plt.plot(q1, q2, label='Explicit Euler Orbit')
plt.scatter([0], [0], color='red', label='Star')  # Indicate the central star
plt.xlabel("q1")
plt.ylabel("q2")
plt.legend()
plt.title("Planetary Orbit using Explicit Euler Method")
plt.grid()
plt.show()
plt.savefig("plot_a.png")