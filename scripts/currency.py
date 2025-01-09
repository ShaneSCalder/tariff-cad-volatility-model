import numpy as np
import matplotlib.pyplot as plt

# Parameters for simulation
current_rate = 0.7  # Current CAD/USD rate
initial_drop_mean = 0.0375  # Mean of initial drop (3.75%)
recovery_mean = 0.0159  # Mean of recovery after resolution (1.59%)
severity_factor = 2.25  # increase greater severity past 1
iterations = 5000  # Number of iterations for Latin Hypercube sampling

# Random seed for reproducibility
np.random.seed(42)

#Sampling for uncertainty (initial drop and recovery)
initial_drop_samples = np.random.uniform(initial_drop_mean * (1 - 0.2), initial_drop_mean * (1 + 0.2), iterations)
recovery_samples = np.random.uniform(recovery_mean * (1 - 0.2), recovery_mean * (1 + 0.2), iterations)

# Apply severity adjustment
initial_drop_samples *= severity_factor
recovery_samples *= severity_factor

# Simulate CAD rates based on sampled values
post_uncertainty_rates = current_rate * (1 - initial_drop_samples)  # After initial drop
post_recovery_rates = post_uncertainty_rates * (1 + recovery_samples)  # After recovery

# Prepare histogram for visualization
plt.figure(figsize=(12, 6))
plt.hist(post_recovery_rates, bins=50, color="blue", alpha=0.7, label="Post-Recovery CAD Rates")
plt.axvline(current_rate, color="red", linestyle="--", label="Current Rate (0.7)")
plt.title("Simulated Distribution of Post-Recovery CAD Rates (5000 Iterations)")
plt.xlabel("CAD/USD Exchange Rate")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True)

# Save the graph as a PNG file
output_file = "simulated_cad_rates.png"
plt.savefig(output_file, dpi=300)
plt.show()

print(f"Graph saved as: {output_file}")
