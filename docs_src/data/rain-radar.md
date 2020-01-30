# Rain Radar

![Masks](../img/Rain-Radar.png)



## Rain Radar

You will find one archive per year and per zone, each one sliced in periods of 10 or 11 days (each month is separated in 3 files). 

Each `.npz` file contains 3 arrays :

* `data` : an array containing a rainfall map for each time step. For each pixel, the value represents the cumulated rainfall in hundreth of millimeters (10^(-2) mm). If the value is missing then the value is -1.

* `dates` : an array containing a datetime object for each `data` rainfall map.

* `miss_dates` : an array containing a datetime object for each missing rainfall map over the period.

The time step between two radar scans is 5 min. The radar starts scanning at 00h every day and ends at 23h55. So each file of 11 days should contain a maximum of 3168 rainfall maps (minus the missing dates).

The radar's spatial resolution is 0.01° and the projection system used is EPSG:4326.

![Masks](../img/Rain-Radar-4.png)


## Rain Radar Quality Code

For each pixel of the rainfall product is associated a quality code with values ranging between 0 (very bad) and 100 (perfect), the values are in percents. If the value is missing, then the value is 255.

The Rain Radar Quality Code data is organized like the Rain Radar data: you will find one archive per year and per zone, each one sliced in periods of 10 or 11 days (each month is separated in 3 files). The original data was to heavy to be manipulated so the qulity code data are divided into 2 files :

* `rainfall_mean_quality_DATE.npz` contains the quality code's average over a day and for each pixel.
  
* `rainfall_diff_quality_DATE.npz` contains the difference between the original value and the average over the day for each pixel.

!!! info
    **Remark about the average quality code computation** : if there is no value for a whole day on 1 pixel, it will be indicated as a missing value in the `mean` file, else the mean computation is done over the non missing values for 1 day and 1 pixel.



![Masks](../img/Rain-Radar-Quality-Code.png)

## Reflectivity - Old Product

Official documentation coming soon! Documentation available in the sample notebooks on GitHub for now...

![Masks](../img/Rain-Radar-Reflectivity-Old.png)

## Reflectivity - New Product

Official documentation coming soon! Documentation available in the sample notebooks on GitHub for now...

![Masks](../img/Rain-Radar-Reflectivity-New.png)
