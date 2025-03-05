#Q5

class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
    
    def addTime(self, other):
        total_hours = self.hours + other.hours
        total_minutes = self.minutes + other.minutes
        if total_minutes >= 60:
            total_hours += 1
            total_minutes -= 60
        return Time(total_hours, total_minutes)
    
    def displayTime(self):
        print(f"{self.hours} hr and {self.minutes} min")
    
    def displayMinute(self):
        print(f"Total minutes: {self.hours * 60 + self.minutes}")

