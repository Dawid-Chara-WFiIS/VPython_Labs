import numpy as np
import matplotlib.pyplot as plt

colors = ['red', 'blue', 'green', 'cyan', 'purple']
plt.xlabel("X coordinate")
plt.ylabel("Y coordinate")

for j in range(5):
    x_position = [0]
    y_position = [0]

    for i in range(10**5):
        angle = np.random.uniform(0, 2*np.pi)
        x_position.append(x_position[i] + np.cos(angle))
        y_position.append(y_position[i] + np.sin(angle))
    plt.plot(x_position, y_position, '-', color=colors[j], linewidth=0.1)
    plt.plot(x_position[10**5], y_position[10**5], 'o', color=colors[j], ms='30')

plt.savefig("Figure2.png")
plt.show()