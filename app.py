import flask
from flask import request, jsonify
from data import movies

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Movie List Archive</h1>
<p>A prototype API for the latest 2021 movies.</p>'''


@app.route('/api/v1/resources/movies/all', methods=['GET'])
def api_all():
    return jsonify(movies)


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
    return jsonify(results)

app.run(port=6767)
