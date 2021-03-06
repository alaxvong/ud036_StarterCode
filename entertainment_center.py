import media  # Module for generate movie class instances
import fresh_tomatoes  # Generates HTML document

interstellar = media.Movie(
    '''
    The movie variable isn't used to render the movies
    in the HTML document in this example,
    but necessary if you want to isolation a single form of media.
    '''
    "Interstellar",
    "http://bit.ly/2t3dhhk",
    "https://www.youtube.com/watch?v=0vxOhd4qlnA"
)

eternal_sunshine_of_the_spotless_mind = media.Movie(
    "Eternal Sunshine of the Spotless Mind",
    "http://bit.ly/2t7Joxc",
    "https://www.youtube.com/watch?v=0zFywiAh7N0"
)

hot_rod = media.Movie(
    "Hot Rod",
    "http://bit.ly/2u1ejrv",
    "https://www.youtube.com/watch?v=DhdrA9qz79o"
)

all_movies = media.Movie.media_list  # Prints All Movies

fresh_tomatoes.open_movies_page(all_movies)
# Pass an array or media.py class instance to render in the HTML page.
