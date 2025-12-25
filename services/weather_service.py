import json

class WeatherService:
    def __init__(self):
        self.file_path='weather_data.json'
        
    #----- Read data from file -----#   
    def read_data(self):
        with open(self.file_path, 'r') as file:
            return json.load(file)
    
    #----- Write data to file -----#
    def write_data(self, data):
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)
        
    #----- Get Weather Data Method -----#
    def get_weather(self):
        weather_data= self.read_data()
        return weather_data

    #----- Add Weather Data Method -----#
    def add_weather(self,data:dict):
        weather_data=self.read_data()
        data['id']=len(weather_data)+1
        weather_data.append(data)
        self.write_data(weather_data)
        return data

    #----- Update Weather Data Method -----#
    def update_weather(self,weather_id:int,data:dict):
        weather_data=self.read_data()
        for item in weather_data:
            if item['id'] == weather_id:
                item.update(data)
                self.write_data(weather_data)
                return item   
        return None    

    #----- Delete Weather Data Method -----#
    def delete_weather(self,weather_id:int):
        weather_data = self.read_data()
        for item in weather_data:
            if item['id'] == weather_id:
                weather_data.remove(item)
                self.write_data(weather_data)
                return item
        return None    
            