import numpy as np
import matplotlib.pyplot as plt

number_of_walks = np.linspace(0, 10**5 + 1, 10**5 + 1)
choices = [-1, 1]
plt.xlabel("Number of walks")
plt.ylabel("Distance")

for j in range(15):
    distances = [0]
    for i in range(10**5):
        distances.append(distances[i] + np.random.choice(choices))
    plt.plot(number_of_walks, distances)

plt.savefig("Figure1.png")
plt.show()