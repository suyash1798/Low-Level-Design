from datetime import datetime

class FareCalculator:

    @staticmethod
    def calculateFareByTime(entry: datetime, exit: datetime) -> int:
        return int((exit - entry).total_seconds() / 3600)