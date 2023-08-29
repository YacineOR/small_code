"""
IO operations
reading/writing of Netcdf CDS climate data files 
"""

import xarray as xr

#Read NetCDF
def read_data(file, timespan=None, darrays=None, expver=None):
    ds=xr.open_dataset(file)
    if expver != None :
        ds = ds.sel(expver=expver)
    if timespan != None :
        ds = ds.sel(time=slice(timespan[0],timespan[1]))
    if darrays != None :
        ds = ds[darrays]
    return ds

# Write NetCDF file
def write_data(ds, file):
    ds.to_netcdf(file)

