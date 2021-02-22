# Satellite data

![Masks](../../img/CT_Sat.png)

<a name="ct_satellite"></a>

## Cloud Type (CT) data

### Description

You will find one NetCDF file per geographic zone ('NW' for North-West of France and 'SE' for South-East of France) and per year. 

For each pixel, the value represents a category of cloud type (16 classes in total):

* 0:No data
* 1:Cloud-free land
* 2:Cloud-free sea
* 3:Snow over land
* 4:Sea ice
* 5:Very low clouds
* 6:Low clouds
* ...

The spatial resolution is 0.03° and the time step is 15 minutes but some dates can be missing (due to problems in original data, so we can do anything.

It is about a METEO FRANCE data fusion product. It combines different outputs (satellite imagery, numerical weather prediction parameters..etc) to compute the Cloud Type product. For more information, cf the [official documentation](https://www.nwcsaf.org/Downloads/GEO/2018/Documents/Scientific_Docs/NWC-CDOP3-GEO-MF-CMS-SCI-UM-Cloud_v1.0.pdf) (from page 26).

![Masks](../../img/CT_Sat_2.png)


**Note**: after we put these data online, we learned there is a parallax effect which is not corrected. According to the official documentation (*User Manual of the Parallax Correction Processor of the NWC/GEO*): 

Due to the Geostationary oblique view of features far to the sub-satellite point (ssp), the positions of objects  placed  above  the  surface  are  affected  by  parallax.  As  it  is  shown  in  Figure  1,  a  high  cloud located  on  the  vertical  of  the  site  A  in  the  Earth surface  is  seen  by  a  geostationary  satellite  in  the position of a different site B.

![Masks](../../img/parallax_effect.PNG)


It induces a shift on data (around 3 or 4 pixels on France) against the ground truth. We remarked also some shift between the data and the basemap (due to the used reprojection function). We plan to fix these two aspects for the next version of the dataset. Sorry for the inconvenience. 

### Files organization

The files are stored by zone and per year:

* NW zone: */data/NW/satellite/CT_NW_"year".nc*
* SE zone: */data/SE/satellite/CT_SE_"year".nc*
