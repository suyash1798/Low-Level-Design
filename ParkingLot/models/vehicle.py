from ParkingLot.enums.vehicle_type import VehicleTypeEnum

class Vehicle:
    number: str
    type: VehicleTypeEnum

    def __init__(self, number: str, type: VehicleTypeEnum):
        self.number = number
        self.type = type