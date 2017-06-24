import media # Module for generating movie class instances
import fresh_tomatoes # Generates HTML document

interstellar = media.Movie( # The movie variable isn't used to render the movies in the HTML document in this example, but necessary if you want to isolation a single form of media.
    "Interstellar",
    "https://upload.wikimedia.org/wikipedia/en/thumb/b/bc/Interstellar_film_poster.jpg/220px-Interstellar_film_poster.jpg",
    "https://www.youtube.com/watch?v=0vxOhd4qlnA"
)

eternal_sunshine_of_the_spotless_mind = media.Movie(
    "Eternal Sunshine of the Spotless Mind",
    "https://upload.wikimedia.org/wikipedia/en/thumb/6/62/Eternal_sunshine_of_the_spotless_mind_ver3.jpg/220px-Eternal_sunshine_of_the_spotless_mind_ver3.jpg",
    "https://www.youtube.com/watch?v=0zFywiAh7N0"
)

hot_rod = media.Movie(
    "Hot Rod",
    "https://upload.wikimedia.org/wikipedia/en/thumb/7/7f/Hot-rod-poster.jpg/220px-Hot-rod-poster.jpg",
    "https://www.youtube.com/watch?v=DhdrA9qz79o"
)

all_movies = media.Movie.media_list # Prints All Movies

fresh_tomatoes.open_movies_page(all_movies) # Pass an array or media.py class instance to render in the HTML page.
