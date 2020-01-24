# MeteoNet : Data exploration toolbox

This repository is intended as a toolbox to handle the MeteoNet dataset. It also serves as a communication interface with the users : you can post issues on this project via http://gitlab.meteo.fr/deep_learning/data_exploration/issues.

1. [What is MeteoNet ?](#meteonet)
2. [How to use this repository ?](#description)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Troubleshooting](#troubleshooting)

# What is MeteoNet ?<a name="meteonet"></a>

![imageMeteoNet](MeteoNet.PNG "Example of MeteoNet data")

MeteoNet is a meteorological dataset released by Météo France, the French national meteorological service. Our goal is to provide a clean and ready-to-use dataset for Data Scientist who want to try their hand on weather data.

The data spans over 3 years, 2016 to 2018, and covers two geographical areas : the north-western and south-eastern quarters of France.

The dataset regroups ground station observations, land-sea and relief masks, radar observations and weather models forecasts. **The satellite observations will be added in a future version.**

For more information about MeteoNet, check out our [Wiki](http://gitlab.meteo.fr/deep_learning/data_exploration/wikis/Home).


# How to use this repository ?<a name="description"></a>

This toolbox includes **data samples** from MeteoNet, the **meteonet_toolbox package** with some useful tools and **notebooks** to help you explore and cross-check all data types.

The notebooks should help you open each data type (grid and point data, different resolutions...) and visualize it with map and relief overlays.

The notebooks rely on the meteonet_toolbox package and we recommend that you install it.


# Requirements <a name="requirements"></a>

* Python 3
* conda
* pip

# Installation <a name="installation"></a>

## I - Install the dependencies

You can install the dependencies with Anaconda (recommended) or with pip.

## Install dependencies with Anaconda (Recommended) 


In a terminal run **in this order** :

```sh
conda install -c conda-forge eccodes
conda install -c conda-forge cfgrib
conda install -c anaconda xarray
```

## Install dependencies with pip

Naviguate to this repository and run :
```sh
pip install -r requirements.txt 
```

## II - Install the repository package

Once the dependencies are installed, you can install the meteonet_toolbox package.

Naviguate to the directory where you have cloned the repository, and run :

```sh
pip install -e .
```

## Install basemap (Optional)

If you want to plot nice maps, you will need the basemap library. The recommended installation method is using anaconda through the conda-forge channel (basemap is no longer uploaded to PyPI due to its size and non-python external dependencies).
The basemap library is not managed anymore since 2020. You could have installation issues (cf Issues in this Gitlab project). It is planned to update the toolbox with a more recent library for basemaps.  

```sh
conda install -c anaconda basemap
```

For some distributions, this installation of basemap is not sufficient. 
You might need to install *basemap-data-hires*:

```sh
conda install basemap-data-hires
```


# Troubleshooting <a name="troubleshooting"></a>

You could run into issues when trying to import the xarray or basemap librairies. 

## xarray

```sh
ECCODES ERROR   :  Unable to find boot.def, the environment variable 
ECCODES_DEFINITION_PATH is defined but incorrect
```

The solution is to indicate the path to the file 'boot.def'. See configuration in ```meteonet_toolbox/user_configuration.py```.

## basemap

```sh
KeyError : 'PROJ_LIB'
```

The solution is to indicate the path to the file 'epsg'. See configuration in ```meteonet_toolbox/user_configuration.py```.

