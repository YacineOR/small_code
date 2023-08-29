"""
Visualizing data
"""

import xarray as xr
import matplotlib.pyplot as plt
from smallcode import yearly_means, monthly_means


# plot monthly means
def plot_monthly_means(darr):
    monthly_means(darr).plot(col='month', col_wrap=4, label=None, cmap='RdBu_r')

# plot yearly means
def plot_yearly_means(darr):
    yearly_means(darr).plot(col='year', col_wrap=5, label=None, cmap='RdBu_r')
