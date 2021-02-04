# Dataset Summary

The data cover two geographical zones, North-West and South-East of France, during three years, 2016 to 2018.

![Map](../../img/Map.png)

The full dataset can be downloaded [here](https://meteonet.umr-cnrm.fr/dataset/) (in the repository *data*).

There, for each geographical zone (*/data/NW or SE/*) and for the 3 years you will find the following data types :

| Data Type | Size for NW zone (GB) | Size for SE zone (GB) | Total Size (GB) | Path (example for the NW zone)
| ----------| --------------------- | --------------------- | --------------- | ---------------
| **Ground Observation**         | 0.5 | 2.5 | **3.0** | */data/NW/ground_stations/*
| **Rain Radar**                 | 5.8 | 6.5 | **12.3** | */data/NW/radar/rainfall/*
| **Rain Radar Quality Code**    | 19.6 | 31 | **50.6** | */data/NW/radar/rainfall_quality_code/*
| **Reflectivity (*new product*)** | 13.5 | 20.0 | **33.5** | */data/NW/radar/reflectivity_new_product/*
| **Reflectivity (*old product*)** | 3.9 | 4.0 | **7.9** | */data/NW/radar/reflectivity_old_product/*
| **Weather models 2D**          | 25.8 | 23.0 | **48.8** | */data/NW/weather_models/2D_parameters/*
| **Weather models 3D**          | 7.8 | 8.0 | **15.8** | */data/NW/weather_models/3D_parameters/*
| **Satellite data (CT for now)**  | 4.8 | 4.8 | **9.6** | */data/NW/satellite/*
| **Masks**                      | 0.0004 | 0.0004 | **0.001** | */data/NW/masks/*
| | | | |
| **TOTAL** | **81.7** | **99.8** | **181.5** |
