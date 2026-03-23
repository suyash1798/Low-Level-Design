from datetime import datetime
from ParkingLot.services.fareCalculator import FareCalculator
from ParkingLot.models.spot import Spot
from ParkingLot.models.ticket import Ticket
from ParkingLot.models.vehicle import Vehicle
from ParkingLot.enums.spot_type import SpotTypeEnum
from ParkingLot.utils.spot_util import SpotUtils

class ParkingLot:
    spotsDict: dict[int, Spot]
    spotIdsByType: dict[SpotTypeEnum, list]
    tickets: dict[str, Ticket]

    def __init__(self, spots: list[Spot]):
        self.spotIdsByType = SpotUtils.separateSpotByType(spots)
        self.spotsDict = SpotUtils.convertSpotsListToDict(spots)
        self.tickets = {}

    def park(self, vehicle: Vehicle) -> Ticket or None:
        spot = SpotUtils.findSpotByVehicleType(vehicle.type, self.spotIdsByType, self.spotsDict)
        
        if spot is None:
            return None
        
        ticket = Ticket(vehicle.number, spot.id, datetime.now())

        spot.isOccupied = True
        self.tickets[vehicle.number] = ticket

        return ticket
    
    def exit(self, vehicle: Vehicle) -> Ticket or None:
        if vehicle.number not in self.tickets:
            return None

        ticket = self.tickets[vehicle.number]
        
        ticket.exitTime = datetime.now()
        self.spotsDict[ticket.spotId].isOccupied = False

        ticket.fare = FareCalculator.calculateFareByTime(ticket.entryTime, ticket.exitTime)

        self.tickets.pop(vehicle.number)

        return ticket
