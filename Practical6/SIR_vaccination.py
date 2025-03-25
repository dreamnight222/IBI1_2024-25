# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# define the variables
N = 10000  # total number
beta = 0.3   # infection probability
gamma = 0.05 # recovery probability

# set for the chart
plt.figure(figsize=(6, 4), dpi=150)

# Get the vaccination rate from 0% to 100% in steps of 10%
for vacc_rate in range(0, 101, 10):
    # set the initial values
    V = int(N * vacc_rate / 100)  # number of people who have been vaccinated
    S = max(N - V - 1, 0)         # number of susceptible individuals(s>=0)
    I = 1 if S > 0 else 0         # number of infected people
    R = N - S - I                 # recovered or resistant
    
    # create an array for infected  
    I_list = [I]
    
    # stimulate 1000 time points
    for t in range(1000):
        #get the infection probability
        infection_prob = beta * (I / N)
        
        # get the number of people who are newly infected
        if S > 0:
            new_infections = np.random.choice(range(2), size=S, p=[1 - infection_prob, infection_prob]).sum()
            new_infections = min(new_infections, S)
        else:
            new_infections = 0
        # get the number of people who are newly recovered
        new_recoveries = np.random.choice(range(2), size=I, p=[1 - gamma, gamma]).sum()
        
        # update the value of S, I, R
        S = S - new_infections
        I = I + new_infections - new_recoveries
        R = R + new_recoveries
        
        #update infected
        I_list.append(I)
    
    # plot the curve of infected people for current vaccination rate
    plt.plot(I_list, label=f'{vacc_rate}% vaccination')

# plot the chart
plt.xlabel('time')
plt.ylabel('number of infections')
plt.title('SIR model of different vaccination rates')
plt.legend()
plt.show()