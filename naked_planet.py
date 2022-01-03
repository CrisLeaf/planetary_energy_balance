import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("TkAgg") # <- for IntelliJ inline plotting
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")


time_step = 10							# years
water_depth = 4000						# meters
L = 1350								# Watts/m2
albedo = 0.3
epsilon = 1
sigma = 5.67e-8							# Watts/m2K4
heat_capacity = water_depth * 4.2e6		# J/Km2
heat_in = L * (1 - albedo) / 4			# Watts/m2
heat_out = 0
time_years = [0]
temperatures = [0.]
heat_content = heat_capacity * temperatures[0]

for t in range(0, 1000):
	time_years.append(time_step + time_years[-1])
	heat_out = epsilon * sigma * pow(temperatures[-1], 4)
	heat_content = heat_content + (heat_in - heat_out) * time_step * 3.14e7
	temperatures.append(heat_content / heat_capacity)

plt.plot(time_years, temperatures)
plt.show()
