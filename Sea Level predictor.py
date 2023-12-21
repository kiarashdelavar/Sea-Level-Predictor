import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


data = pd.read_csv("epa-sea-level.csv")
plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'])
slope, intercept, r_value, p_value, std_err = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
years = range(1880, 2051)
line = slope * years + intercept
plt.plot(years, line, color='r')
recent_data = data[data['Year'] >= 2000]
recent_slope, recent_intercept, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
recent_line = recent_slope * years + recent_intercept
plt.plot(years, recent_line, color='g')
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')

plt.savefig('sea_level_plot.png')
return plt.gca()