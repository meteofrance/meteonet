You can install this package by going in the dedicated directory (where you have clone the depository)

```sh
pip install -e .
```

This will install the package in the directory. 
After that, you can import the python file doing for example 

```python
import data_exploration.utils.coordinates_and_projection as cap
```


To open easily a GRIB file with Python, it is necessary to install the packages (in this order) *eccodes*, *cfgrib* then *xarray* with the following commands (if you use the Anaconda environment):
```sh
    conda install -c conda-forge eccodes
    conda install -c conda-forge cfgrib
    conda install -c anaconda xarray
    conda install -c anaconda basemap
```
Optionnal : 
```sh
    conda install -c anaconda basemap
```
