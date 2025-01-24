import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
lambda_values = [5, 10, 15]  # Different arrival rates
mu = 12  # Service rate
queue_populations = np.arange(1, 51)  # Range of queue populations

# Function to calculate average queue length and system utilization
def calculate_queue_metrics(lambda_rate, mu_rate, queue_population):
    utilization = lambda_rate / mu_rate
    # Calculate average queue length for a given queue population using M/M/1 queue formula
    avg_queue_length = (lambda_rate**2) / (mu_rate * (mu_rate - lambda_rate))
    # Factor in population size to estimate how the system will behave as queue length increases
    if queue_population < avg_queue_length:
        avg_queue_length = queue_population
    return avg_queue_length, utilization

# Initialize lists to store metrics for different lambda values
avg_queue_lengths = []
utilizations = []

# Simulate and calculate for each lambda value
for lambda_rate in lambda_values:
    queue_lengths = []
    utilizations_for_lambda = []
    
    for population in queue_populations:
        avg_queue_length, utilization = calculate_queue_metrics(lambda_rate, mu, population)
        queue_lengths.append(avg_queue_length)
        utilizations_for_lambda.append(utilization)
    
    avg_queue_lengths.append(queue_lengths)
    utilizations.append(utilizations_for_lambda)

# Plotting the results
plt.figure(figsize=(12, 6))

# Plot average queue length
plt.subplot(1, 2, 1)
for i, lambda_rate in enumerate(lambda_values):
    plt.plot(queue_populations, avg_queue_lengths[i], label=f"λ = {lambda_rate}")
plt.title('Average Queue Length vs Queue Population')
plt.xlabel('Queue Population')
plt.ylabel('Average Queue Length')
plt.legend()

# Plot system utilization
plt.subplot(1, 2, 2)
for i, lambda_rate in enumerate(lambda_values):
    plt.plot(queue_populations, utilizations[i], label=f"λ = {lambda_rate}")
plt.title('System Utilization vs Queue Population')
plt.xlabel('Queue Population')
plt.ylabel('System Utilization')
plt.legend()

plt.tight_layout()
plt.show()
