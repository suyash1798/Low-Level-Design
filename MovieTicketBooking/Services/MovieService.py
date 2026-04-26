from MovieTicketBooking.Models.Movie import Movie

class MovieService:
    movies: list[Movie]
    movieById: dict[int, Movie]

    def __init__(self):
        self.movies = []
        self.movieById = {}
        pass

    def addMovie(self, name: str):
        movie = Movie(len(self.name), name)

        self.movies.append(movie)
        self.movieById[movie.id] = movie
    
    def getMovies(self) -> list(Movie):
        return self.movies
    
    def getMovieById(self, id) -> Movie:
        return self.movieById[id]
