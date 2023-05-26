import numpy as np
import matplotlib.pyplot as plt

# Define the parameters of the model
N = 1000  # Total population
beta = 0.2  # Transmission rate
gamma = 0.1  # Recovery rate
mu = 0.01  # Natural death rate
nu = 0.005  # Disease-related death rate
rho = 0.005  # Birth rate
epsilon = 0.05  # Immunity loss rate
I0 = 10  # Initial number of infected individuals

# Define the initial conditions
S = N - I0  # Number of susceptible individuals
I = I0  # Number of infected individuals
D = 0  # Number of deceased individuals
H = 0  # Number of immune individuals

# Define the time interval and the time step
tmax = 100  # Maximum time
dt = 0.1  # Time step

# Define the arrays to store the results
time = np.arange(0, tmax, dt)  # Time array
S_array = np.zeros(len(time))  # Array to store the number of susceptible individuals
I_array = np.zeros(len(time))  # Array to store the number of infected individuals
D_array = np.zeros(len(time))  # Array to store the number of deceased individuals
H_array = np.zeros(len(time))  # Array to store the number of immune individuals

# Define the Gillespie algorithm
for i in range(len(time)):
    # Calculate the rates of the different events
    betaS = beta * S * I / N
    gammaI = gamma * I
    muN = mu * N
    nuI = nu * I
    rhoN = rho * N
    epsilonH = epsilon * H
    
    # Calculate the total rate of all events
    total_rate = betaS + gammaI + muN + nuI + rhoN + epsilonH
    
    # Generate two random numbers
    r1, r2 = np.random.rand(2)
    
    # Calculate the time until the next event occurs
    tau = -np.log(r1) / total_rate
    
    # Determine which event occurs next
    if r2 < betaS / total_rate:
        S -= 1
        I += 1
    elif r2 < (betaS + gammaI) / total_rate:
        I -= 1
        D += 1
    elif r2 < (betaS + gammaI + muN) / total_rate:
        N -= 1
    elif r2 < (betaS + gammaI + muN + nuI) / total_rate:
        I -= 1
        D += 1
    elif r2 < (betaS + gammaI + muN + nuI + rhoN) / total_rate:
        N += 1
    else:
        H -= 1
    
    # Update the arrays with the new values
    S_array[i] = S
    I_array[i] = I
    D_array[i] = D
    H_array[i] = H
    
# Plot the results
plt.plot(time, S_array, label='Susceptible')
plt.plot(time, I_array, label='Infected')
plt.plot(time, D_array, label='Deceased')
plt.plot(time, H_array, label='Immune')
plt.xlabel('Time')
plt.ylabel('Number of individuals')
plt.legend()
plt.show()
