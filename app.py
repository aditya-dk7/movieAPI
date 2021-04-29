import flask
from flask import request, jsonify
from data import movies
from randomMovie import pick_random_movie

app = flask.Flask(__name__)
#app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Movie List Archive</h1>
<p>A prototype API for the latest 2021 movies.</p>'''


@app.route('/api/v1/resources/movies/all', methods=['GET'])
def api_all():
    response = jsonify(movies)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/api/v1/resources/movies/random', methods=['GET'])
def api_random():
    result = []
    if 'genre' in request.args:
        genre = str(request.args['genre'])
        x = pick_random_movie(genre)
        for movie in movies:
            if movie["id"] == x:
                result.append(movie)
        result = jsonify(result)
        result.headers.add('Access-Control-Allow-Origin', '*')        
        return result
    result.append(movies[int(pick_random_movie(""))])
    result = jsonify(result)
    result.headers.add('Access-Control-Allow-Origin', '*')
    return result

@app.route('/api/v1/resources/movies', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    results = []
    for movie in movies:
        if movie['id'] == str(id):
            results.append(movie)
    results = jsonify(results)
    results.headers.add('Access-Control-Allow-Origin', '*')
    return results

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
