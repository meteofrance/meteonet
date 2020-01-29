# Installing our Toolbox

Here you will find install instructions for the MeteoNet Toolbox.

## Requirements

The following packages are required to use our toolbox : **Python 3** and **conda** or **pip**.

## Dowload the repository

Copy the repository from our [GitHub page](https://github.com/meteofrance/meteonet) or run :

```sh
git clone https://github.com/meteofrance/meteonet.git
```

## Install dependencies

You just have to run the following commands :

```sh tab="Conda (Recommended)"
conda install -c conda-forge eccodes
conda install -c conda-forge cfgrib
conda install -c anaconda xarray
```

```sh tab="Pip"
pip install -r requirements.txt 
```

## Install the package

Once the dependencies are installed, you can install the meteonet_toolbox package. Naviguate to the directory where you have cloned the repository, and run :

```sh
pip install -e .
```

## (Optional) Install basemap 

!!! warning
    As **the basemap library is not maintained anymore** since 2020, you could have installation issues. 
    
    We plan to update the toolbox with a more recent mapping library such as Mapbox or Cartopy. If you have tried these libraries, or another one, don't hesitate to make a pull request !

If you want to plot nice maps with your data, you can use the basemap library. The recommended installation method uses anaconda through the conda-forge channel  as basemap is no longer uploaded to PyPI due to its size and non-python external dependencies :

```sh
conda install -c anaconda basemap
```

For some distributions, this installation of basemap is not sufficient. You might need to install *basemap-data-hires*:

```sh
conda install basemap-data-hires
```


## Troubleshooting

You could run into issues when trying to import the xarray or basemap librairies. 

??? question "```ECCODES ERROR   :  Unable to find boot.def, the environment variable ECCODES_DEFINITION_PATH is defined but incorrect```"
    The solution is to indicate the path to the file ```boot.def``` by adding an ```ECCODES_DEFINITION_PATH``` environment variable. See example of configuration in ```meteonet_toolbox/user_configuration.py```.

??? question "```KeyError : 'PROJ_LIB'```"
    The solution is to indicate the path to the file ```epsg``` by adding a ```PROJ_LIB``` environment variable. See example of configuration in ```meteonet_toolbox/user_configuration.py```.
