from fastapi import FastAPI

app = FastAPI()

weather_data=[]
current_id=1

#----- Get Weather Data -----#
@app.get('/weather')
def get_weather():
    return weather_data

#----- Add Weather Data -----#
@app.post('/weather')
def add_weather(data:dict):   
    global current_id
    data['id']=current_id
    current_id+=1
   
    weather_data.append(data)
    return {"message":"Data added"}

#----- Update Weather Data -----#
@app.put('/weather/{id}')
def update_weather(id:int,data:dict):
    for item in weather_data:
        if item['id']==id:
            item.update(data)
            return {"message":"Data updated"}
    return {"message":"Data not found"}

#----- Delete Weather Data -----#
@app.delete('/weather/{id}')
def delete_weather(id:int): 
    for item in weather_data:
        if item['id']==id:
            weather_data.remove(item)
            return {"message":"Data deleted"}
    return {"message":"Data not found"}