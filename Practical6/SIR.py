# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# define the variables
N = 10000  # total number
S = 9999   # the number of initial susceptible people
I = 1      # the number of initial infected
R = 0      # the number of initial recovered
beta = 0.3   # infection probability
gamma = 0.05 # recovery probability

# create arrays for each of variables to track how they evolve over time
S_list = [S]
I_list = [I]
R_list = [R]

# stimulate 1000 time points
for t in range(1000):
    # get the infection probability
    infection_prob = beta * (I / N)
    
    # get the number of people who are newly infected
    new_infections = np.random.choice(range(2), size=S, p=[1 - infection_prob, infection_prob]).sum()
    
    # get the number of people who are newly recovered
    new_recoveries = np.random.choice(range(2), size=I, p=[1 - gamma, gamma]).sum()
    
    # update the value of S, I, R
    S = S - new_infections
    I = I + new_infections - new_recoveries
    R = R + new_recoveries
    
    # update the arrays
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)

# plot the chart
plt.figure(figsize=(6, 4), dpi=150)
plt.plot(S_list, label='susceptible')
plt.plot(I_list, label='infected')
plt.plot(R_list, label='recovered')
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.legend()
plt.show()