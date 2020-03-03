import getpass 
import os 

user = getpass.getuser() 

if user == "larvorg":
    os.environ["ECCODES_DEFINITION_PATH"]="C:/Users/larvorg/AppData/Local/Continuum/anaconda3/Library/share/eccodes/definitions" 
elif user == "chabotv": 
    os.environ["ECCODES_DEFINITION_PATH"]="C:/Users/chabotv/AppData/Local/Continuum/anaconda3/Library/share/eccodes/definitions" 
else: 
    print("User is not known. If you experiment some problems with path for library please add the specific path in `user_configuration.py` module")