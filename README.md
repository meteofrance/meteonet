# MeteoNet : Data exploration toolbox

This repository is intended as a toolbox to handle the MeteoNet dataset. It's also a communication interface with MeteoNet's users : if  you have a request or a problem concerning MeteoNet, you can post an  issue [here](http://gitlab.meteo.fr/deep_learning/data_exploration/issues) on this project. For more information (installation, data types, glossary...), check out our [documentation](http://gitlab.meteo.fr) !

1. [What is MeteoNet ?](#meteonet)
2. [How to use this repository ?](#description)
3. [Installation](#installation)

# What is MeteoNet ?<a name="meteonet"></a>
  ![imageMeteoNet](MeteoNet.PNG "Example of MeteoNet data")

MeteoNet is a meteorological dataset released by Météo France, the French national meteorological service. Our goal is to provide a clean and ready-to-use dataset for Data Scientist who want to try their hand on weather data.

The data spans over 3 years, 2016 to 2018, and covers two geographical areas : the north-western and south-eastern quarters of France.

The dataset regroups ground station observations, land-sea and relief masks, radar observations and weather models forecasts.

# How to use this repository ?<a name="description"></a>

This toolbox includes **data samples** from MeteoNet, the **meteonet_toolbox package** with some useful tools and **notebooks** to help you explore and cross-check all data types.

The notebooks should help you open each data type (grid and point data, different resolutions...) and visualize it with map and relief overlays.

The notebooks rely on the meteonet_toolbox package and we recommend that you install it.


# Installing the toolbox<a name="installation"></a>

All the install instructions for our toolbox are available [here](http://gitlab.meteo.fr/deep_learning/data_exploration/issues) in our documentation.
