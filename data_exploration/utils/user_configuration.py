import getpass 
import os 
user = getpass.getuser() 

if user == "larvorg":
    path = "D:/prez_opendata/data/output/samples/"
    os.environ["PROJ_LIB"]="C:/Users/larvorg/AppData/Local/Continuum/anaconda3/Library/share" 
    os.environ["ECCODES_DEFINITION_PATH"]="C:/Users/larvorg/AppData/Local/Continuum/anaconda3/Library/share/eccodes/definitions" 
elif user == "chabotv": 
    os.environ["PROJ_LIB"]="C:/Users/chabotv/AppData/Local/Continuum/anaconda3/Library/share" 
    os.environ["ECCODES_DEFINITION_PATH"]="C:/Users/chabotv/AppData/Local/Continuum/anaconda3/Library/share/eccodes/definitions" 
    path = "D:/Data/open_data/samples/"
else: 
    raise(ValueError("User is not known"))