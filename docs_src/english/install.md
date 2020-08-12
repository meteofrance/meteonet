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

We noticed some version incompatility issues between packages, especially during installation of basemap librairies like Cartopy. So it is recommended to use virtual environments (using conda if you have Anaconda : https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/ or virtualenv of you use pip : https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/). Once you created your virtual environment, you just have to run the following commands :

=== "** Conda (from scratch)"

    ``` python
    conda env create -f environment.yml  #yml file at the root of the repository 
    conda activate meteonet_toolbox      #activate the created environment 
    ```

=== "** Conda (from an existing environment)"

    ``` python
    #if necessary (it is about basic packages)
    #conda install -c anaconda numpy>=1.14.0
    #conda install -c anaconda pandas>=0.24.0
    #conda install -c anaconda scipy
    #conda install -c conda-forge matplotlib 
    conda install -c conda-forge eccodes
    conda install -c conda-forge cfgrib
    conda install -c anaconda xarray
    ```

=== "Pip"
    ``` python
    pip install -r requirements.txt 
    ```
** Conda is the recommended way 

## Install the package

Once the dependencies are installed, you can install the meteonet_toolbox package. Naviguate to the directory where you have cloned the repository, and run :

``` sh
pip install -e .
```

## Install Jupyter Notebook

To be able to open our notebooks and use the example code we provided, you will need to install Jupyter Notebook :

=== "** Conda (from scratch)"
    ``` python
    #nothing to do, already done!
    ```

=== "** Conda (from an existing environment)"

    ``` python
    #if necessary (it is about basic packages)
    #conda install -c conda-forge notebook
    ```

=== "Pip"
    ``` python
    pip install jupyter
    ```

Once the installation is done, navigate inside the repository and run : ```jupyter notebook```

You should be able to open each notebook and explore the sample data. 


## (Optional) Install Cartopy (*master* branch)
This new mapping library replaces Basemap since 2020. 
If you want to plot nice maps with your data, you can use the cartopy library. The recommended installation method uses anaconda through the conda-forge channel: 

=== "** Conda (from scratch)"
    ``` python
    #nothing to do, already done!
    ```

=== "** Conda (from an existing environment)"

    ``` python
    conda install -c conda-forge cartopy
    ```
    
=== "Pip"
    ``` python
    #The list of Cartopy dependencies can be found on this page : https://scitools.org.uk/cartopy/docs/latest/installing.html. 
    #Required version of PROJ is 4.9.0 or later.
    #Shapely should be install with:
    pip install shapely --no-binary shapely
    pip install Cartopy
    ```

## (Optional) Install Basemap (*basemap* branch)

!!! warning
    As **the basemap library is not maintained anymore** since 2020, you could have installation issues. 
    
    We updated the toolbox with a more recent mapping library, Cartopy. If you have tried another libraries, don't hesitate to make a pull request !

If you want to plot nice maps with your data, you can use the basemap library. The recommended installation method uses anaconda through the anaconda channel  as basemap is no longer uploaded to PyPI due to its size and non-python external dependencies :

```sh
conda install -c anaconda basemap
```

For some distributions, this installation of basemap is not sufficient. You might need to install *basemap-data-hires*:

```sh
conda install basemap-data-hires
```


## Troubleshooting

You could run into issues when trying to import and/or use the xarray or basemap librairies. 

!!! note
    It seems that the library Eccodes (used with the xarray library to open GRIB files) can create conflicts with other packages. In a future version, we will stop using the GRIB format and convert the data to the netCDF format, which is more common and should pose less intallation issues.

??? question "```ECCODES ERROR   :  Unable to find boot.def, the environment variable ECCODES_DEFINITION_PATH is defined but incorrect```"
    The solution is to indicate the path to the file ```boot.def``` by adding an ```ECCODES_DEFINITION_PATH``` environment variable. See example of configuration in ```meteonet_toolbox/user_configuration.py```.

??? question "```KeyError : 'PROJ_LIB'```"
    The solution is to indicate the path to the file ```epsg``` by adding a ```PROJ_LIB``` environment variable. See example of configuration in ```meteonet_toolbox/user_configuration.py```.
