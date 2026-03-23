from collections import defaultdict

class SpotUtils:

    VehicleTypeAllowedSpotSize = {
        VehicleTypeEnum.BIKE: [SpotTypeEnum.SMALL, SpotTypeEnum.MEDIUM, SpotTypeEnum.LARGE],
        VehicleTypeEnum.CAR: [SpotTypeEnum.MEDIUM, SpotTypeEnum.LARGE],
        VehicleTypeEnum.TRUCK: [SpotTypeEnum.LARGE],
    }

    @staticmethod
    def findSpotByVehicleType(type: VehicleTypeEnum, spotIdsByType: dict[VehicleTypeEnum, list], spotsDict: dict[int, Spot]) -> int or None:
        
        allowedTypes = SpotUtils.VehicleTypeAllowedSpotSize[type]

        for allowed in allowedTypes:
            for spotId in spotIdsByType[allowed]:
                if spotsDict[spotId].isOccupied == True:
                    continue
                
                return spotsDict[spotId]


        return None

    @staticmethod
    def convertSpotsListToDict(spots: list[Spot]):
        spotDict = {}

        for spot in spots:
            spotDict[spot.id] = spot
        
        return spotDict

    @staticmethod
    def separateSpotByType(spots: list[Spot]) -> dict[SpotTypeEnum, list[Spot]]:
        spotByType = defaultdict(list)

        for spot in spots:
            spotByType[spot.type].append(spot.id)
        
        return spotByType