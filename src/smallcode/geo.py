"""
operations linked to geopandas
"""

import xarray as xr
import geopandas as gpd
import pandas as pd

# convert xarray.DataArray to geopandas.GeoDataFrame 
def convert_to_geopandas(darr):
    df = darr.to_dataframe().reset_index()
    return gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitude, df.latitude), crs = 'EPSG:4326')

# load worldgdf and select a region (continent or country)
def load_worldgdf(continent=None, country=None):
    world_filepath = gpd.datasets.get_path('naturalearth_lowres')
    worldgdf = gpd.read_file(world_filepath)
    if country is not None:
        # todo assert possible values Africa Antarctica Asia Europe
        # North America Oceania Seven seas (open ocean) South America
        return worldgdf[worldgdf.name == country]
    if continent is not None:
        return worldgdf[worldgdf.continent == continent]
    return worldgdf
    
# average per country
def t2m_mean_per_country(era5_gdf, reg_gdf):
    joined = gpd.sjoin(reg_gdf[['name','geometry']],era5_gdf[['year','t2m','geometry']], predicate='contains', how='inner')
    df = joined.groupby(['name','year']).mean('t2m').reset_index()
    geodf = reg_gdf[['name','geometry']].merge(df, on='name')
    return geodf
