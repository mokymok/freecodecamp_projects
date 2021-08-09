import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
  df=pd.read_csv('https://raw.githubusercontent.com/mokymok/freecodecamp_projects/main/sea_level_data.csv',delimiter=',')
  x=df['Year']
  y=df['CSIRO Adjusted Sea Level']
    # Create scatter plot
  plt.scatter(x,y)
    # Create first line of best fit
  r=linregress(x,y)
  y_e=np.arange(1880, 2050, 1)
  l=[r.slope*xi+r.intercept for xi in y_e]
  plt.plot(y_e,l,'r')
    # Create second line of best fit
  s=linregress(x[121:],y[121:])
  y_f=np.arange(2000, 2050, 1)
  l=[s.slope*xi+s.intercept for xi in y_f]
  plt.plot(y_f,l,'b')
    # Add labels and title
  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')
  plt.title('Rise in Sea Level')
    # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return df,plt.gca()
