import numpy as np 
import xarray as xr
from data_exploration.utils.constant import SAT_COORD


def get_satellite_as_xarray(fname,zone,channel_name="unknown"):
    """
    :param fname: Absolute file path of npz data
    :param zone: Name of the area 
    :param channel_name: Name of the channel to use as dataarray name
    """
    d = np.load(fname, allow_pickle=True)
    d.files  #know the compressed file structure
    data = d['arr_0']
    
    ds = xr.Dataset()
    ds.coords["latitude"] =  SAT_COORD[zone]["lat"]
    ds.coords["longitude"] = SAT_COORD[zone]["lon"]
    ds[channel_name] = (("latitude",'longitude'),data)
    return ds