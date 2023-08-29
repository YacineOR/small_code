"""
some summary operations
"""

import xarray as xr

# yearly means
def yearly_means(ds):
    years = ds.time.dt.year
    return ds.groupby(years).mean()
    
# means over the years for each month
def monthly_means(ds):
    months = ds.time.dt.month
    return ds.groupby(months).mean()

