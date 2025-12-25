from pydantic import BaseModel
from typing import Optional

#----- Location Model -----#
class Location(BaseModel):
    lat:float
    lon:float
 
#----- Weather Create Model -----#   
class WeatherCreateModel(BaseModel):
    location:Location
    temperature:float
    otherInfo:str

#----- Weather Update Model -----#  
class WeatherUpdateModel(BaseModel):
    location:Optional[Location]=None
    temperature: Optional[float]=None
    otherInfo: Optional[str]=None
    

    
