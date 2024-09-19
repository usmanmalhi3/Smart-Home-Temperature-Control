class SimpleReflexAgent:
    def __init__(self):
        self.temperature_thresohold= 22  
    
    def control_heater(self, current_temperature):
        if current_temperature < self.temperature_thresohold:
            return "Turn heater ON"
        else:
            return "Turn heater OFF"


agent = SimpleReflexAgent()
room_temperatures = [21,45,2,23] 

for temp in room_temperatures:
    action = agent.control_heater(temp)
    print(f"Current temperature: {temp}°C -> Action: {action}")



