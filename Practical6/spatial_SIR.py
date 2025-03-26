# Pseudocode:
# 1.import necessary libraries
# 2.create the 2D population
# 3.choose a infected person randomly 
# 4.stimulate 100 time point
# 5.find every infected person and recovered person at each time point
# 6.save every time point as a frame and save the current frame to the list
# 7.make an animation to show the process

# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# define the variables
beta = 0.3   # infection probability
gamma = 0.05 # recovery probability

# make array of all susceptible popuation
population = np.zeros((100, 100))

# choose one infected person randomly
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1  # 1=infected

fig = plt.figure(figsize=(6,4), dpi=150)
ims = []
# stimulate 100 time points
for t in range(100):
    # find the infected
    infected = np.where(population == 1)
    infected_coords = list(zip(infected[0], infected[1]))
    
    # focus on each outbreak points
    for x, y in infected_coords:
        # check the neighbours
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:  # skip itself
                    continue
                nx, ny = x + dx, y + dy
                # check if the neighbour is susceptible
                if 0 <= nx < 100 and 0 <= ny < 100 and population[nx, ny] == 0:
                    # infection occurs with beta probability.
                    if np.random.random() < beta:  
                        population[nx, ny] = 1
    
        # recovery occurs with gamma probability
        if np.random.random() < gamma:
            population[x, y] = 2  # 2=recovered
    
    im = plt.imshow(population, cmap='viridis',interpolation='nearest', animated=True)
    plt.title(f'time point{t+1}')
    # save the current frame to the list
    ims.append([im])

# make an animation
ani = animation.ArtistAnimation(fig, ims, interval=200, blit=True, repeat=False)
plt.show()
# All the codes related to the animation is from Grok3.