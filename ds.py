import numpy as np
import matplotlib.pyplot as plt

# Parameters
mu = 6  # service rate
lambda_values = np.arange(1, 10, 0.1)  # arrival rates from 1 to 10

# Calculate L and W for each lambda
L_values = lambda_values / (mu - lambda_values)
W_values = 1 / (mu - lambda_values)

# Plotting
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(lambda_values, L_values, label='Average number of customers in system (L)')
plt.xlabel('Arrival Rate (λ)')
plt.ylabel('L')
plt.title('Average Number of Customers in System')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(lambda_values, W_values, label='Average time in system (W)', color='orange')
plt.xlabel('Arrival Rate (λ)')
plt.ylabel('W (hours)')
plt.title('Average Time Spent in System')
plt.legend()

plt.tight_layout()
plt.show()