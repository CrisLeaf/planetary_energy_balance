import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("TkAgg") # <- for IntelliJ inline plotting
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")


# constants
time_step = 20							# years
water_depth = 5000						# meters
L = 1350								# Watts/m2
albedo = 0.3
epsilon = 1
sigma = 5.67e-8							# Watts/m2K4
heat_capacity = water_depth * 4.2e6		# J/Km2
heat_in = L * (1 - albedo) / 4			# Watts/m2
secs_per_year = 31536000
number_of_iterations = 100

# model 1 with no atmosphere reflection
heat_out = 0
time_years = [0]
temperatures1 = [0.]
heat_content = heat_capacity * temperatures1[0]

for t in range(0, number_of_iterations):
	time_years.append(time_step + time_years[-1])
	heat_out = epsilon * sigma * pow(temperatures1[-1], 4)
	heat_content = heat_content + (heat_in - heat_out) * time_step * secs_per_year
	temperatures1.append(heat_content / heat_capacity)

temperatures1 = [temp - 273.15 for temp in temperatures1]

# model 2 with 1 layer atmosphere reflection
heat_out = 0
time_years = [0]
temperatures2 = [0.]
heat_content = heat_capacity * temperatures2[0]

for t in range(0, number_of_iterations):
	time_years.append(time_step + time_years[-1])
	heat_out = epsilon * sigma * pow(temperatures2[-1], 4)
	heat_content = heat_content + (heat_in - heat_out) * time_step * secs_per_year
	temperatures2.append(heat_content / heat_capacity)

temperatures2 = [temp * 1.189 - 273.15 for temp in temperatures2]

plt.plot(time_years, temperatures1, label="Sin atmósfera")
plt.plot(time_years, temperatures2, label="Una capa de atmósfera")
plt.plot(time_years, [15 for time in time_years], label="Temperatura real")
plt.title("Balance de energía en La Tierra", fontsize=15)
plt.xlabel("Año", fontsize=12)
plt.ylabel("Temperatura (°C)", fontsize=12)
plt.legend(fontsize=12)
plt.show()