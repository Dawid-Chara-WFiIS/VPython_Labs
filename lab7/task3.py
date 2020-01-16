import numpy as np
import matplotlib.pyplot as plt


def calculate_average(number_of_flips):
    choices = [-1, 1]
    avg = 0

    for _ in range(200):
        distances = [0]
        for i in range(number_of_flips):
            distances.append(distances[i] + np.random.choice(choices))
        avg += distances[number_of_flips]**2
    return np.sqrt(avg/200)


coin_flips = [10, 50, 100, 200, 400, 1000, 1600, 2500, 4000, 5000, 6000, 8000, 10000]
averages = [calculate_average(i) for i in coin_flips]

for i, j in zip(coin_flips, averages):
    print(f"Coin flips {i} - Average distance walked {j}")

plt.grid()
plt.xlabel("Number of coin flips")
plt.ylabel("Average distance walked")
plt.plot(coin_flips, averages, 'k')
plt.savefig("Figure3.png")
plt.show()