from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origins':"*"}})

@app.route('/', methods=['GET'])
def greetings():
    return "Hello, World!"

GAMES = []

#fet route handler
@app.route('/games', methods=['GET', 'POST'])
def all_games():
    response_object = {'status': 'success'}
    if request.method == "POST":
        post_data = request.get_json()
        GAMES.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'played': post_data.get('played')})
        response_object['message'] = "Game Added from Flask!"
        print(GAMES)
    else:
        response_object['games'] = GAMES
    return jsonify(response_object)

@app.route('/games/<game_id>', methods=['PUT', 'DELETE'])
def single_game(game_id):
    response_object = {'status': 'success'}
    if request.method == "PUT":
        post_data = request.get_json()
        remove_game(game_id)
        GAMES.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'played': post_data.get('played')}
        )
        response_object['message'] = 'Product Udated!'
        print(GAMES)
    if request.method == "DELETE":
        remove_game(game_id)
        response_object['message'] = 'Product Removed!'
    return jsonify(response_object)

def remove_game(game_id):
    for game in GAMES:
        if game['id'] == game_id:
            GAMES.remove(game)
            return True
    return False



if __name__  == "__main__":
    app.run(debug=True, host="0.0.0.0")

