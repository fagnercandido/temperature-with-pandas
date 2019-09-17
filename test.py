import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from plot_erro import plot_erro


data =  pd.read_csv('GlobalLandTemperaturesByCountry.csv')

brasil = data.where(data.Country == 'Brazil')

brasil = brasil.dropna()

brasil.dt = [d.split('-')[0] for d in brasil.dt]
brasil_groupby_ano = brasil.groupby('dt')

x = [int(dt[0]) for dt in brasil_groupby_ano.dt]
y = brasil_groupby_ano.AverageTemperature.mean()

plt.scatter(x, y)
plt.title('Temperatura desde 1880')
plt.show()

#print(brasil.sample(10))


