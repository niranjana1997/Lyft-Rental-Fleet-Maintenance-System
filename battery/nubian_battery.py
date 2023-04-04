from battery.battery import Battery

import datetime

class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
        
    def needs_service(self):
        actual_service_date = self.last_service_date + datetime.timedelta(days=365*4)
        return actual_service_date < self.current_date