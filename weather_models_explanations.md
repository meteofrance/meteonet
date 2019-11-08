## French weather models 

Météo-France produce weather models to forecast the weather. It solve physical equations which model the atmospheric, oceanic phenomenon... all physical behaviours which influence the weather. 
It compute a lot of weather parameters (temperature, wind, humidity...) at different points on the globe in 4 dimensions (latitude, longitude, height and time).

Each model runs several times per day at fixed time. Each execution is called a 'run'. Each time step for which we have weather forecasts is called a 'valid time'. (We find these terms, runs and valid times, in the files).
On the globe surface, the points are spaced with regular latitude and longitude steps : this mesh of points is called a grid. 
About the vertical dimension (height), the points are not necessarily regurlarly spaced; the vertical levels can be expressed in height levels in meters or in isobar levels in hPa. The isobar are the levels for which the pressure is the same.

The 2 main models of Météo-France are AROME and ARPEGE. They do no have the same purposes but are complementary.

* ARPEGE is used to forecast the weather at a high scale in space and time. 
* AROME is used to forecast the weather at a finer scale in space and time.

In pratice, ARPEGE is used to forecast the weather on Europe and AROME on France. 

The order of magnitudes of resolutions are the following : 
* ARPEGE : horizontal spatial resolution, up to 0.1° (~10km), 4 runs/day, forecasts up to 102 hours ahead 
* AROME : horizontal spatial resolution, up to 0.01° (~1km), 8 runs/day, forecasts up to 48 hours ahead 

All these characteristics have been choses following the compromises between the needs and the time computing and costs. 

