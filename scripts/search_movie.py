from configparser import ConfigParser
from django.shortcuts import render
import tmdbsimple as tmdb
import os

config = ConfigParser()
config.read('movies/config.cfg')
tmdb.API_KEY = config['tmdb']['API_KEY']
query = "avatar"
search_result = tmdb.Search().movie(query=query)['results']
# print(search_result)

# expected output
# [{'adult': False, 'backdrop_path': '/ruziOM4OlILvyrOdChvvFqy4Ggw.jpg', 'genre_ids': [28, 12, 14, 878], 'id': 19995, 'original_language': 'en', 'original_title': 'Avatar', 'overview': 'In the 22nd century, a paraplegic Marine is dispatched to the moon Pandora on a unique mission, but becomes torn between following orders and protecting an alien civilization.', 'popularity': 98.865, 'poster_path': '/kyeqWdyUXW608qlYkRqosgbbJyK.jpg', 'release_date': '2009-12-15', 'title': 'Avatar', 'video': False, 'vote_average': 7.582, 'vote_count': 31031}]

id = 19995
movie = tmdb.Movies(id)
trailers = list(filter(lambda v: v['type'] == 'Trailer', movie.videos()['results']))
teasers = list(filter(lambda v: v['type'] == 'Teaser', movie.videos()['results']))
keywords = movie.keywords()['keywords']
extracted_info = {
    "info": movie.info(),
    "year": movie.info()['release_date'][:4],
    "cast": movie.credits()['cast'][:15],
    "crew": movie.credits()['crew'][:15],
    "trailers": trailers,
    "teasers": teasers,
    "keywords": keywords,
    "reviews": movie.reviews()['results'],
    "alt": movie.alternative_titles()['titles']
}
print(extracted_info)
# expected output
# json format of film info
