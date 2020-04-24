# Installation de la Boîte à Outils

## Prérequis

## Téléchargement du répertoire

```sh
git clone https://github.com/meteofrance/meteonet.git
```

## Installation des dépendances

```sh tab="Conda (Recommended)"
#only if you start from an empty virtual environment 
#conda install -c anaconda numpy>=1.14.0
#conda install -c anaconda pandas>=0.24.0
#conda install -c anaconda scipy
#conda install -c conda-forge matplotlib 
conda install -c conda-forge eccodes
conda install -c conda-forge cfgrib
conda install -c anaconda xarray
```

```sh tab="Pip"
pip install -r requirements.txt 
```

## Installation du paquet

```sh
pip install -e .
```

## Installation de Jupyter Notebook

```sh tab="Conda (Recommended)"
conda install -c conda-forge notebook
```

```sh tab="Pip"
pip install jupyter
```

## (Optionnel) Installation de Cartopy (branche *master*)

```sh tab="Conda (Recommended)"
conda install -c conda-forge cartopy 
```

```sh tab="Pip"
pip install Cartopy
```


## (Optionnel) Installation de Basemap (branche *basemap*)

!!! warning
    Attention

```sh
conda install -c anaconda basemap
```

```sh
conda install basemap-data-hires
```


## Problèmes fréquents

!!! note
     Eccodes

??? question "```ECCODES ERROR   :  Unable to find boot.def, the environment variable ECCODES_DEFINITION_PATH is defined but incorrect```"
    The solution is to indicate the path to the file ```boot.def``` by adding an ```ECCODES_DEFINITION_PATH``` environment variable. See example of configuration in ```meteonet_toolbox/user_configuration.py```.

??? question "```KeyError : 'PROJ_LIB'```"
    The solution is to indicate the path to the file ```epsg``` by adding a ```PROJ_LIB``` environment variable. See example of configuration in ```meteonet_toolbox/user_configuration.py```.

