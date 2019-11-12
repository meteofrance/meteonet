# Structure

This repository is structured as follows :
* *data_sample* : it contains samples of each data type sorted by data type (ground_stations, radar...)
* *ground_stations* : notebooks to open data from ground_stations
* *masks* : notebooks to open masks data (land-sea and relief masks)
* *radar* : notebooks to open radar data
* *satellite* : notebooks to open satellite data
* *superimpose_data* : notebooks with tools to superimpose all data types (grid and punctual data, different initial resolutions...)
* *utils* : python scripts useful for user configuration, functions useful to get coordinates, legends for plots...
* *weather_models* : notebooks to open data from weather models

# Prerequisites

There are 2 ways of installation : either by Anaconda (the recommended way) or by pip.

## By Anaconda : the recommended way
* install Anaconda with Python 3

and then, type in a terminal **in this order** :

```sh
conda install -c conda-forge eccodes
conda install -c conda-forge cfgrib
conda install -c anaconda xarray
```

## By pip
* install Python 3
* install pip

and then, type in a terminal (cf requirements.txt file in this repository) :
```sh
pip install -r requirements.txt 
```

### Optionnal

To plot nice plots with basemaps, you can install the basemap library. The recommended installation method is using anaconda through the conda-forge channel (Basemap is no longer uploaded to PyPI due to its size and non-python external dependencies).

```sh
conda install -c anaconda basemap
```

For some distributions, this installation of basemap  is not sufficient. 
It it is needed to install *basemap-data-hires* doing 

```sh
conda install basemap-data-hires
```

## In case of librairies import problems

You could have problems when you use the librairies xarray or basemap. 
* problem with the xarray library -> PROBLEM OF TYPE "ECCODES ERROR   :  Unable to find boot.def, the environment variable ECCODES_DEFINITION_PATH is defined but incorrect"

The solution is to indicate the path to the file 'boot.def'. 

* problem with the basemap library -> PROBLEM OF TYPE "KeyError : 'PROJ_LIB'"

The solution is to indicate the path to the file 'epsg'. 

Examples of paths on Windows are indicated in the script utils/user_configuration.py.

# Install the repository as a package

You can install this package by going in the dedicated directory (where you have clone the depository)

```sh
pip install -e .
```

This will install the package in the directory. 
After that, you can import the python file doing for example 

```python
import data_exploration.utils.coordinates_and_projection as cap
```


