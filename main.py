import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
arrival_rates = np.linspace(0.1, 0.9, 50)  # Lambda (arrival rate)
service_rate = 1.0  # Mu (service rate), fixed at 1 customer/unit time

# Calculate performance metrics for M/M/1 queue
utilization = arrival_rates / service_rate  # Utilization factor (rho)
L = utilization / (1 - utilization)  # Average number in the system
L_q = utilization**2 / (1 - utilization)  # Average number in the queue
W = 1 / (service_rate - arrival_rates)  # Average time in the system
W_q = utilization / (service_rate - arrival_rates)  # Average time in the queue

# Plot Utilization vs. Arrival Rate
plt.figure(figsize=(10, 6))
plt.plot(arrival_rates, utilization, label="Utilization Factor (ρ)", lw=2)
plt.axhline(y=1, color='r', linestyle='--', label="Maximum Utilization (ρ=1)")
plt.title("Utilization Factor vs. Arrival Rate (M/M/1 Queue)", fontsize=14)
plt.xlabel("Arrival Rate (λ)", fontsize=12)
plt.ylabel("Utilization Factor (ρ)", fontsize=12)
plt.legend()
plt.grid(True)
plt.show()

# Plot Queue Metrics
plt.figure(figsize=(12, 6))

# Average number in system and queue
plt.plot(arrival_rates, L, label="Average Number in System (L)", lw=2)
plt.plot(arrival_rates, L_q, label="Average Number in Queue (Lq)", lw=2)

# Labels and title
plt.title("Queue Metrics vs. Arrival Rate (M/M/1 Queue)", fontsize=14)
plt.xlabel("Arrival Rate (λ)", fontsize=12)
plt.ylabel("Number of Customers", fontsize=12)
plt.legend()
plt.grid(True)
plt.show()

# Plot Time Metrics
plt.figure(figsize=(12, 6))

# Average time in system and queue
plt.plot(arrival_rates, W, label="Average Time in System (W)", lw=2)
plt.plot(arrival_rates, W_q, label="Average Time in Queue (Wq)", lw=2)

# Labels and title
plt.title("Time Metrics vs. Arrival Rate (M/M/1 Queue)", fontsize=14)
plt.xlabel("Arrival Rate (λ)", fontsize=12)
plt.ylabel("Time (Units)", fontsize=12)
plt.legend()
plt.grid(True)
plt.show()
