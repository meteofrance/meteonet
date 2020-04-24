# Observations au Sol

![Masks](../../img/GroundStationsObservations.png)


### Metadonnées

| Name | Description | Unit |
| -----| ----------- | ---- |
| number_sta | ground station ID | - |
| lat | latitude | decimal degrees (10<sup>-1</sup> °)|
| lon | longitude | decimal degrees (10<sup>-1</sup> °)|
| height_sta | station height | meters (m) |
| date |  a datetime object | format 'YYYY-MM-DD HH: mm :ss' |

### Paramètres Météorologiques

| Name | Description | Unit |
| -----| ----------- | ---- |
| dd | Wind direction | degrees (°) |
| ff | Wind speed |  m.s<sup>-1</sup>|
| precip | Precipitation during the reporting period | kg.m<sup>2</sup>|
| hu | Humidity | percentage (%) |
| td |  [Dew point](../../glossary/#dew-point) | Kelvin (K) |
| t |  Temperature | Kelvin (K) |
| psl |  Pressure reduced to sea level | Pascal (Pa) |