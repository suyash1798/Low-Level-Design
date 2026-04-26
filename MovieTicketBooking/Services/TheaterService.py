from MovieTicketBooking.Models.Theater import Theater
from MovieTicketBooking.Models.Screen import Screen
from MovieTicketBooking.Services.ScreenService import ScreenService

class TheaterService:
    theaters: list[Theater]
    theaterById: dict[int, Theater]

    def __init__(self, screenService: ScreenService):
        self.theaters = []
        self.theaterById = {}
        self.screenService = screenService
        pass

    def addTheather(self, name: str, screens: list[str]):
        theater = Theater(len(self.theaters), name)

        self.theaters.append(theater)
        self.theaterById[theater.id] = theater

        for screen in screens:
            self.screenService.addScreen(screen[0], theater.id, screen[1:])
    
