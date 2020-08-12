# Ground Observations

![Masks](../../img/GroundStationsObservations.png)


Hundreds of observation stations are built throughout the French territory, each one fitted with several sensors measuring parameters such as temperature, pressure, wind... Each parameter is measured every 6 minutes and each file contains 1 month of data for each geographical area ('NW' for North-West of France and 'SE' for South-East of France). 

### Files organization

For each zone, the files are stored per year with 2 compression levels (.tar.gz and .tar). 

Example

Here is the path for the NW zone, year 2016 : */data/NW/ground_stations/NW_ground_stations_2016.tar.gz/NW2016.tar/NW2016.csv*

### Metadata

| Name | Description | Unit |
| -----| ----------- | ---- |
| number_sta | ground station ID | - |
| lat | latitude | decimal degrees (10<sup>-1</sup> °)|
| lon | longitude | decimal degrees (10<sup>-1</sup> °)|
| height_sta | station height | meters (m) |
| date |  a datetime object | format 'YYYY-MM-DD HH: mm :ss' |

### Meteorological parameters

| Name | Description | Unit |
| -----| ----------- | ---- |
| dd | Wind direction | degrees (°) |
| ff | Wind speed |  m.s<sup>-1</sup>|
| precip | Precipitation during the reporting period | kg.m<sup>2</sup>|
| hu | Humidity | percentage (%) |
| td |  [Dew point](../../glossary/#dew-point) | Kelvin (K) |
| t |  Temperature | Kelvin (K) |
| psl |  Pressure reduced to sea level | Pascal (Pa) |