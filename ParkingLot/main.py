import random
from ParkingLot.models.spot import Spot
from ParkingLot.models.vehicle import Vehicle
from ParkingLot.enums.spot_type import SpotTypeEnum
from ParkingLot.enums.vehicle_type import VehicleTypeEnum
from ParkingLot.services.parking_lot import ParkingLot

spots = []

for i in range(0, 2):
    spot = Spot(len(spots), SpotTypeEnum.LARGE)
    spots.append(spot)

for i in range(0, 2):
    spot = Spot(len(spots), SpotTypeEnum.MEDIUM)
    spots.append(spot)

for i in range(0, 2):
    spot = Spot(len(spots), SpotTypeEnum.SMALL)
    spots.append(spot)

random.shuffle(spots)

prakinglot = ParkingLot(spots)

vehicles = []

for i in range(0, 5):
    vehicles.append(Vehicle(len(vehicles), VehicleTypeEnum.CAR))

for i in range(0, 5):
    vehicles.append(Vehicle(len(vehicles), VehicleTypeEnum.BIKE))

for i in range(0, 5):
    vehicles.append(Vehicle(len(vehicles), VehicleTypeEnum.BIKE))

random.shuffle(vehicles)

for vehicle in vehicles:
    ticket = prakinglot.park(vehicle)

    if ticket == None:
        print('No spots available')
    else:
        print('Spot Alloted to ', vehicle.number, ' is ', ticket.spotId)


for vehicle in vehicles:
    ticket = prakinglot.exit(vehicle)

    if ticket == None:
        print('ticket not valid')
    else:
        print('Vehicle ', vehicle.number, ' exited from spot ', ticket.spotId)




