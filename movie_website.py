
"""
movie_website.py file, displays the list of movies

"""
import movies
import movielist
import fresh_tomatoes

# represents the list of favoutite movies
movie_list = [movielist.toy_story, movielist.avatar,
              movielist.ratatouille, movielist.midnight_in_paris,
              movielist.fast_furious, movielist.school_of_rock]

fresh_tomatoes.open_movies_page(movie_list)
