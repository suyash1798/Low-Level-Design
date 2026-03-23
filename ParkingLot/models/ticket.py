from datetime import datetime

class Ticket:
    vehicleNumber: str
    spotId: int
    entryTime: datetime
    exitTime: datetime
    fare: int
    resolved: bool

    def __init__(self, vehicleNumber: str, spotId: int, entryTime: datetime):
        self.vehicleNumber = vehicleNumber
        self.spotId = spotId
        self.entryTime = entryTime
        self.resolved = False