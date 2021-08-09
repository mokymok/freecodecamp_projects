import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x= "Year", y = "CSIRO Adjusted Sea Level", data = df)
    # Create first line of best fit
    r=linregress(df["Year"],df["CSIRO Adjusted Sea Level"])
    y_e=np.arange(1880, 2051, 1)
    l=[r.slope*xi+r.intercept for xi in y_e]
    plt.plot(y_e,l,'r')
    # Create second line of best fit
    df2 = df.loc[df["Year"] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df2["Year"], df2["CSIRO Adjusted Sea Level"])
    years2 = pd.Series(range(2000,2051))
    ax.plot(years2, intercept2 + slope2*years2, 'b', label='second line of best fit')
    # Add labels and title
    ax.set(xlabel="Year", ylabel="Sea Level (inches)", title="Rise in Sea Level")
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
