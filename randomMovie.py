from data import movies
import re, random
def pick_random_movie(category = None):
    if category == None:
        return random(1, len(movies))
    movieIdList = []
    for movie in movies:
        genre_str = movie['genre']
        category_regex_find = re.search(category, genre_str)
        if category_regex_find:
            movieIdList.append(movie['id'])
    random.shuffle(movieIdList)
    randomMovieID = random.randrange(0, len(movieIdList))
    findId = movieIdList[randomMovieID]
    return findId
