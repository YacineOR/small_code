"""
Filtering and converting operations
"""

import xarray as xr

# filter using start time and end time 
def filter_timespan(ds, time_start, time_end):
    return ds.sel(time=slice(timespan[0],timespan[1]))


# filter space
def filter_space(ds, lat_min, lat_max, lon_min, lon_max):
     return ds.sel(**{'longitude' : slice(lon_min, lon_max),
                        'latitude' : slice(lat_max, lat_min)})

# convert kelvin to celsius
def kelvin_to_celsius(ds,da_name):
    if ds[da_name].attrs['units']=="K":
        long_name = ds[da_name].attrs['long_name']
        ds[da_name] = ds[da_name]-273.15
        ds[da_name].attrs['units']="C"
        ds[da_name].attrs['long_name']=long_name
        

# convert longitudes to [-180,180]
def center_longitude0(ds) :
    ds2 = ds.copy(deep=True)
    ds2.coords['longitude'] = (ds.coords['longitude'] + 180) % 360 - 180
    ds2.coords['longitude'].attrs['units']="degrees_east"
    ds2.coords['longitude'].attrs['long_name']="longitude"
    return ds2.sortby(ds2.longitude)
    
    
# check if longitudes within [-180,180] 
def check_centered_europe(ds) :
    return ds.coords['longitude'].max() <= 180 
 
