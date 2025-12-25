from fastapi import FastAPI, HTTPException
from services.weather_service import WeatherService
from models.weather_model import WeatherCreateModel,WeatherUpdateModel

app = FastAPI()
weather_service=WeatherService()

#----- Get Weather Data -----#
@app.get('/weather')
def get_weather():
    result=weather_service.get_weather()
    
    return {
        "success":True,
        "message":"Data fetched successfully!",
        "data":result
    }
        

#----- Add Weather Data -----#
@app.post('/weather')
def add_weather(data:WeatherCreateModel):
    result=weather_service.add_weather(data.model_dump())
    
    if not result:
        return {
            "success":False,
            "message":"Data not added!"
        }
    return {
        "success":True,
        "message":"Data added successfully!",
        "data":result
    }
    
        
#----- Update Weather Data -----#
@app.put('/weather/{id}')
def update_weather(id:int,data:WeatherUpdateModel):
    result = weather_service.update_weather(id,data.model_dump(exclude_unset=True))
    
    if not result:
        raise HTTPException(status_code=404, detail="Data not found!") 
    return {
        "success":True,
        "message":"Data updated successfully!",
        "data":result
    }    

#----- Delete Weather Data -----#
@app.delete('/weather/{id}')
def delete_weather(id:int): 
    result=weather_service.delete_weather(id)
    
    if not result:
        raise HTTPException(status_code=404, detail="Data not found!")
    return {
        "success":True,
        "message":"Data deleted successfully!",
        "data":result
    }