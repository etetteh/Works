""" This calls the movie class.
    You can add as many movie details as you want."""
import movie



# It should be in this order: movie_title, movie_storyline, movie_posterImage, movie_trailer
my_movie = movie.Movie(
    "Suits",
    "Suits is set at a fictional law firm in New York City, and follows talented college dropout Mike Ross (Patrick J. Adams), who begins working as a law associate for Harvey Specter (Gabriel Macht), despite never attending law school.",
    "https://upload.wikimedia.org/wikipedia/commons/c/cc/Suits_Logo.png",
    "https://www.youtube.com/watch?v=85z53bAebsI"  
    )

# print(my_movie.movie_posterImage)

my_movie.show_trailer()