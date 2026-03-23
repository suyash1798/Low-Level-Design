from ParkingLot.enums.spot_type import SpotTypeEnum

class Spot:
    id: int
    type: SpotTypeEnum
    isOccupied: bool

    def __init__(self, id: int, type: SpotTypeEnum):
        self.id = id
        self.type = type
        self.isOccupied = False