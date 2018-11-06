class Movie:
    '''
    Movie class to define Movie Objects
    '''
    def __init__(self,id,title,overview,poster,vote_average,vote_count):
        self.id = id
        self.title = title
        self.overview = overview
        self.poster = 'https://image.tmdb.org/t/p/w500/' + poster
        self.vote_average = vote_average
        self.vote_count = vote_count 
# title - The name of the Movie
# overview - A short description on the Movie
# image - The poster image for the Movie
# vote_average - Average rating of the Movie
# vote_count - How many people have rated the Movie
# id - The movie id