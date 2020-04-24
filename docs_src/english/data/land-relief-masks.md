# Land-Sea and Relief Masks

![Masks](../../img/Masks.png)

For each geographical zone (North-West (NW) of France and South-East (SE) of France), two different masks are stored in a GRIB file:

* the **land-sea mask**, stored in the ```lsm``` file. The values are binary : 0 for sea and 1 for land.
  
* the **relief mask**, stored in the ```p3008``` file. The values are in meters.

The spatial resolution of the masks is 0.025°. 

Note : When you open a GRIB file with the library xarray, a new associated ```.idx``` file is created. 
