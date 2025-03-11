import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def H(theta):
    return theta**4 - 8*theta**2 - 2*np.cos(4*np.pi*theta)

def gradient_H(theta):
    return 4*theta**3 - 16*theta + 8*np.pi*np.sin(4*np.pi*theta)

def gradient_descent_scheduled_lr(theta_init, max_iter=500, tol=1e-6):
    """
    Gradient descent with scheduled learning rate using 1/np.linspace(50,200,N)
    where N is the total number of steps.
    """
    # Estimate N (number of steps) - we'll use max_iter and adjust later
    N = max_iter
    
    # Create scheduled learning rates
    alphas = 1/np.linspace(50, 200, N)
    
    theta = theta_init
    theta_vals = [theta]
    H_vals = [H(theta)]
    iter_count = 0
    
    while iter_count < max_iter:
        grad = gradient_H(theta)
        
        if np.isnan(grad) or np.abs(grad) < tol:
            break
        
        # Use the current step's learning rate (or the last one if we exceed N)
        alpha = alphas[min(iter_count, N-1)]
        
        theta_new = theta - alpha * grad
        
        # Update theta and store values
        theta = theta_new
        theta_vals.append(theta)
        H_vals.append(H(theta))
        
        iter_count += 1
    
    return theta_vals, H_vals

def create_animation(theta_path, h_path, theta_init, output_file=None):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plot the function
    x = np.linspace(-3, 3, 1000)
    y = H(x)
    ax.plot(x, y, 'b-', linewidth=1.5, label='H(θ)')
    
    # Plot the gradient descent path
    ax.plot(theta_path, h_path, 'r.-', alpha=0.5, linewidth=0.5, markersize=3, label='Path')
    
    # Create the moving point
    point, = ax.plot([], [], 'ro', markersize=8)
    
    # Annotation for current position
    annotation = ax.annotate("", xy=(0, 0), xytext=(10, 10), textcoords="offset points",
                            bbox=dict(boxstyle="round", fc="w"), ha='center')
    annotation.set_visible(False)
    
    # Set axis labels and title
    ax.set_xlabel('θ', fontsize=12)
    ax.set_ylabel('H(θ)', fontsize=12)
    ax.set_title(f'Gradient Descent with Scheduled LR (Starting at θ = {theta_init})', fontsize=14)
    ax.legend(loc='upper right')
    
    # Set appropriate axis limits
    y_margin = (max(y) - min(y)) * 0.1
    ax.set_ylim(min(y) - y_margin, max(y) + y_margin)
    
    def init():
        point.set_data([], [])
        annotation.set_visible(False)
        return point, annotation
    
    def update(frame):
        point.set_data(theta_path[frame], h_path[frame])
        annotation.xy = (theta_path[frame], h_path[frame])
        
        # Calculate current learning rate if we were to display it
        if frame < len(theta_path) - 1:
            step_num = frame
            N = len(theta_path) - 1  # Total steps taken
            alpha = 1/np.interp(step_num, [0, N-1], [50, 200])
            annotation.set_text(f"θ: {theta_path[frame]:.4f}\nH(θ): {h_path[frame]:.4f}\nLR: {alpha:.6f}")
        else:
            annotation.set_text(f"θ: {theta_path[frame]:.4f}\nH(θ): {h_path[frame]:.4f}")
            
        annotation.set_visible(True)
        return point, annotation
    
    ani = FuncAnimation(fig, update, frames=len(theta_path), init_func=init, 
                        interval=100, blit=True, repeat=False)
    
    if output_file:
        # Check for ffmpeg
        try:
            ani.save(output_file, writer='ffmpeg', dpi=100)
            print(f"Animation saved to {output_file}")
        except Exception as e:
            print(f"Error saving animation: {e}")
            print("Trying to save with pillow writer instead...")
            try:
                ani.save(output_file.replace('.mp4', '.gif'), writer='pillow', dpi=100)
                print(f"Animation saved as GIF")
            except:
                print("Failed to save animation. Display only.")
    
    plt.tight_layout()
    plt.show()
    return ani

# Analyze the function to find approximate global minimum locations for reference
x_test = np.linspace(-3, 3, 10000)
y_test = H(x_test)
min_indices = np.where((y_test < np.roll(y_test, 1)) & (y_test < np.roll(y_test, -1)))[0]
min_thetas = x_test[min_indices]
min_values = y_test[min_indices]
global_min_idx = np.argmin(min_values)
global_min_theta = min_thetas[global_min_idx]
global_min_value = min_values[global_min_idx]

print(f"Approximate global minimum at θ ≈ {global_min_theta:.6f} with H(θ) ≈ {global_min_value:.6f}")

# Run gradient descent with scheduled learning rate for multiple initial values
theta_inits = [-1, 0.5, 3]
results = []

for theta_0 in theta_inits:
    theta_path, h_path = gradient_descent_scheduled_lr(theta_0)
    
    if theta_path:
        final_theta = theta_path[-1]
        final_h = h_path[-1]
        distance_to_global = abs(final_theta - global_min_theta)
        
        print(f"Initial θ: {theta_0}, Final θ: {final_theta:.6f}, Final H(θ): {final_h:.6f}")
        print(f"Distance to global minimum: {distance_to_global:.6f}")
        print(f"Number of steps taken: {len(theta_path)-1}")
        
        results.append((theta_0, final_theta, final_h, distance_to_global))
        
        # Create and display the animation
        ani = create_animation(theta_path, h_path, theta_0, f'gradient_descent_scheduled_{theta_0}.mp4')
        
        print("-" * 50)

# Print a summary of results
print("\nResults Summary:")
print("=" * 60)
print(f"{'Initial θ':<10} | {'Final θ':<12} | {'Final H(θ)':<12} | {'To Global Min':<12}")
print("-" * 60)
for init, final, h_val, dist in results:
    print(f"{init:<10.2f} | {final:<12.6f} | {h_val:<12.6f} | {dist:<12.6f}")