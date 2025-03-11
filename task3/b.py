import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the Hamiltonian function
def H(theta):
    return theta**4 - 8 * theta**2 - 2 * np.cos(4 * np.pi * theta)

# Metropolis–Hastings algorithm
def metropolis_hastings(theta0, beta, sigma, num_steps):
    theta = theta0
    history = [theta]

    for _ in range(num_steps):
        theta_proposed = theta + np.random.normal(0, sigma)  # Propose new theta
        delta_H = H(theta_proposed) - H(theta)
        acceptance_ratio = np.exp(-beta * delta_H)

        if delta_H < 0 or np.random.rand() < acceptance_ratio:
            theta = theta_proposed  # Accept move

        history.append(theta)

    return np.array(history)

# Parameters
beta = 1.5  # Set an intermediate β value
sigma = 0.5  # Step size for Gaussian proposal
num_steps = 200  # Number of iterations for animation
initial_guesses = [-1, 0.5, 3]  # Different initial starting points

# Loop through each initial guess and create a separate animation
for theta0 in initial_guesses:
    history = metropolis_hastings(theta0, beta, sigma, num_steps)

    # Create figure
    fig, ax = plt.subplots(figsize=(8, 5))
    theta_vals = np.linspace(-3, 3, 400)
    H_vals = H(theta_vals)
    ax.plot(theta_vals, H_vals, label="H(θ)", color='blue')  # Plot energy landscape
    point, = ax.plot([], [], 'ro', markersize=6, label=f"θ₀={theta0}")  # Red dot for steps
    ax.set_xlabel("θ")
    ax.set_ylabel("H(θ)")
    ax.set_title(f"Metropolis–Hastings Optimization (θ₀={theta0})")
    ax.legend()

    # Update function for animation
    def update(frame):
        point.set_data(history[frame], H(history[frame]))
        return point,

    # Create animation
    ani = animation.FuncAnimation(fig, update, frames=num_steps, interval=100, blit=True)

    # Save animation as mp4 file
    filename = f"metropolis_hastings_theta_{theta0}.mp4"
    ani.save(filename, writer="ffmpeg", fps=20)

    print(f"Animation saved as {filename}")