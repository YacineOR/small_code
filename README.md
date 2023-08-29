# Small_code
A small code/library that reads a NetCDF climate data file, does operations on the data and shows graphical representations

## The environment
I used the same conda environmet as the hat project.
```
conda env create -f environment.yml
conda activate hat
pip install -e .
```

## The data
ERA5 monthly averaged data on single levels from 1940 to present (8.3 GB)
datas of interest : 2m temperature, Surface net solar radiation
Downloaded from the Climate Data Store https://cds.climate.copernicus.eu/#!/home
Check out the file cds_request for more info on the data request.
