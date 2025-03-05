#Q5

def temperature(temperature_readings):
    Avg = sum(temperature_readings)/len(temperature_readings)
    High = max(temperature_readings)
    Low = min(temperature_readings)
    
    print("Average Temperature:", round(Avg, 1))
    print("Highest Temperature:", High)
    print("Lowest Temperature:", Low)
    
temperature_readings = [25, 28, 21, 24, 27]
temperature(temperature_readings)