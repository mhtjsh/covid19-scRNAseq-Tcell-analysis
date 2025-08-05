import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the ODE model
def pasc_model(y, t, alpha, beta, gamma, delta_T, delta_I):
    L, T, I = y
    dLdt = -gamma * L * T
    dTdt = alpha * T * I - delta_T * T
    dIdt = beta * T - delta_I * I
    return [dLdt, dTdt, dIdt]

# --- Simulation Setup ---

# 1. PARAMETERS for a pathological but stable model
alpha   = 0.03
beta    = 0.5
gamma   = 0.004
delta_T = 0.15
delta_I = 1.0

# 2. SET INITIAL CONDITIONS [L0, T0, I0]
L0 = 1000
T0 = 10
I0 = 1
y0 = [L0, T0, I0]

# 3. SET TIME VECTOR
t = np.linspace(0, 50, 500)

# 4. SOLVE THE ODE SYSTEM
solution = odeint(pasc_model, y0, t, args=(alpha, beta, gamma, delta_T, delta_I))

# 5. PLOT THE RESULTS ON SEPARATE SUBPLOTS FOR CLARITY
plt.style.use('seaborn-v0_8-whitegrid')

# Create a figure with 2 vertically stacked subplots that share an x-axis
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

fig.suptitle('ODE Model of "Stuck" Immune Response in PASC (Corrected)', fontsize=18)

# --- Top Plot: Lung Cells ---
ax1.plot(t, solution[:, 0], label='Healthy Lung Cells (L)', color='green', linewidth=2.5)
ax1.set_ylabel('Lung Cell Count', fontsize=12)
ax1.legend()
ax1.grid(True)

# --- Bottom Plot: T-Cells and IFN-gamma ---
ax2.plot(t, solution[:, 1], label='Activated T-Cells (T)', color='red', linewidth=2.5)
ax2.plot(t, solution[:, 2], label='IFN-gamma (I)', color='purple', linestyle='--', linewidth=2.5)
ax2.set_ylabel('Immune Concentration', fontsize=12)
ax2.set_xlabel('Time (Days)', fontsize=12)
ax2.legend()
ax2.grid(True)

# Improve layout and show the plot
plt.tight_layout(rect=[0, 0, 1, 0.96]) # Adjust for suptitle
plt.show()
