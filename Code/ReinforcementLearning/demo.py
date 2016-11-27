from flask import Flask, render_template, url_for, json
import os
import json
app = Flask(__name__)

import main
from TicTacToe import TicTacToe

ai_start = False

@app.route("/")
def hello():
    ai_start = False
    print('load')
    print(ai_start)
    return render_template('index.html')

@app.route("/json/<file>")
def return_json(file):
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static", file)
    data = json.load(open(json_url))
    return json.dumps(data)

@app.route("/start")
def start_game():
    main.start_playing(ai_start)
    return 'game started'

@app.route("/train/<amount>")
def train(amount):
    print('start training')
    print(amount)
    print(main.start_training(amount))
    main.start_playing(ai_start)
    return 'training started'

@app.route("/move/<x>/<y>/<turn>")
def make_move(x, y, turn):
    print('Yo this move was just made: ' + str(main.game.player_turn(x, y)))

    return str([x,y])

@app.route("/swap")
def swap():
    global ai_start
    if ai_start:
        ai_start = False
    else:
        ai_start = True
    print('swap')
    return 'Swapped'

@app.route("/reset")
def reset_board():
    with open("static/test.json", "r") as jsonFile:
        data = json.load(jsonFile)

    print(data)
    data["board"] = [[0,0,0],[0,0,0],[0,0,0]]
    data["last_move"] = None
    data["trained"] = 0
    data["time"] = None
    data["qvalues"] = None
    print(data)

    with open("static/test.json", "w") as jsonFile:
        jsonFile.write(json.dumps(data))

    return 'success'

if __name__ == "__main__":
    app.run(debug=True)
