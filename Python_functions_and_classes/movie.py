"""This is a simple class function that when executed, gives information about a movie: movievtitle, movie storyline, movie posterImage, movie trailer"""

import webbrowser

class Movie():
    
    def __init__ (self, movie_title, movie_storyline, movie_posterImage, movie_trailer):
        self.title = movie_title
        self.storyline = movie_storyline 
        self.posterImage_url = movie_posterImage  
        self.trailer_url = movie_trailer
        
    def show_trailer(self):
        webbrowser.open(self.trailer_url)