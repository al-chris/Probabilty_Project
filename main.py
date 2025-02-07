import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math

def queue_metrics(arrival_rate, service_rate, num_servers):
    rho = arrival_rate / (num_servers * service_rate)
    if rho >= 1:
        return np.inf, np.inf, np.inf, np.inf, np.inf
    
    p0 = 1 / (sum([(arrival_rate / service_rate) ** n / math.factorial(n) for n in range(num_servers)]) +
              ((arrival_rate / service_rate) ** num_servers / (math.factorial(num_servers) * (1 - rho))))
    
    Lq = ((arrival_rate / service_rate) ** num_servers * rho) / (math.factorial(num_servers) * (1 - rho) ** 2) * p0
    L = Lq + (arrival_rate / service_rate)
    Wq = Lq / arrival_rate
    W = L / arrival_rate
    
    return rho, L, Lq, W, Wq

def plot_queue_metrics(arrival_rate, service_rate, num_servers):
    arrival_rates = np.linspace(0.1, service_rate * num_servers - 0.1, 50)
    
    utilization = [queue_metrics(lam, service_rate, num_servers)[0] for lam in arrival_rates]
    L_values = [queue_metrics(lam, service_rate, num_servers)[1] for lam in arrival_rates]
    Lq_values = [queue_metrics(lam, service_rate, num_servers)[2] for lam in arrival_rates]
    W_values = [queue_metrics(lam, service_rate, num_servers)[3] for lam in arrival_rates]
    Wq_values = [queue_metrics(lam, service_rate, num_servers)[4] for lam in arrival_rates]
    
    fig, axes = plt.subplots(3, 1, figsize=(10, 15))
    
    axes[0].plot(arrival_rates, utilization, label="Utilization Factor (ρ)", lw=2)
    axes[0].axhline(y=1, color='r', linestyle='--', label="Maximum Utilization (ρ=1)")
    axes[0].set_title("Utilization Factor vs. Arrival Rate (M/M/c Queue)")
    axes[0].set_xlabel("Arrival Rate (λ)")
    axes[0].set_ylabel("Utilization Factor (ρ)")
    axes[0].legend()
    axes[0].grid(True)
    
    axes[1].plot(arrival_rates, L_values, label="Average Number in System (L)", lw=2)
    axes[1].plot(arrival_rates, Lq_values, label="Average Number in Queue (Lq)", lw=2)
    axes[1].set_title("Queue Metrics vs. Arrival Rate (M/M/c Queue)")
    axes[1].set_xlabel("Arrival Rate (λ)")
    axes[1].set_ylabel("Number of Customers")
    axes[1].legend()
    axes[1].grid(True)
    
    axes[2].plot(arrival_rates, W_values, label="Average Time in System (W)", lw=2)
    axes[2].plot(arrival_rates, Wq_values, label="Average Time in Queue (Wq)", lw=2)
    axes[2].set_title("Time Metrics vs. Arrival Rate (M/M/c Queue)")
    axes[2].set_xlabel("Arrival Rate (λ)")
    axes[2].set_ylabel("Time (Units)")
    axes[2].legend()
    axes[2].grid(True)
    
    st.pyplot(fig)

st.title("Bank Queue Management System")

arrival_rate = st.slider("Arrival Rate (λ)", 0.1, 5.0, 1.0, 0.1)
service_rate = st.slider("Service Rate (μ)", 0.5, 5.0, 1.0, 0.1)
num_servers = st.slider("Number of Servers (c)", 1, 10, 1)

rho, L, Lq, W, Wq = queue_metrics(arrival_rate, service_rate, num_servers)

if np.isinf(L):
    st.error("System is unstable. Increase the number of servers or reduce arrival rate.")
else:
    st.write(f"**Utilization Factor (ρ):** {rho:.2f}")
    st.write(f"**Average Number in System (L):** {L:.2f}")
    st.write(f"**Average Number in Queue (Lq):** {Lq:.2f}")
    st.write(f"**Average Time in System (W):** {W:.2f} units")
    st.write(f"**Average Time in Queue (Wq):** {Wq:.2f} units")
    
    plot_queue_metrics(arrival_rate, service_rate, num_servers)
