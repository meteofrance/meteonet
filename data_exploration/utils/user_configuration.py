import getpass 
import os 
from data_exploration.utils.constant import *
import logging 

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s  - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
log.addHandler(ch)


user = getpass.getuser() 

if user == "larvorg":
    path = "D:/MeteoNet/data_samples/"
    os.environ["PROJ_LIB"]="C:/Users/larvorg/AppData/Local/Continuum/anaconda3/Library/share" 
    os.environ["ECCODES_DEFINITION_PATH"]="C:/Users/larvorg/AppData/Local/Continuum/anaconda3/Library/share/eccodes/definitions" 
elif user == "chabotv": 
    os.environ["PROJ_LIB"]="C:/Users/chabotv/AppData/Local/Continuum/anaconda3/Library/share" 
    os.environ["ECCODES_DEFINITION_PATH"]="C:/Users/chabotv/AppData/Local/Continuum/anaconda3/Library/share/eccodes/definitions" 
    path = "D:/Data/open_data/samples/"
else: 
    log.warning("User is not known. If you experiment some problems with path for library please add the specific path in `user_configuration.py` module")
    #raise(ValueError("User is not known"))