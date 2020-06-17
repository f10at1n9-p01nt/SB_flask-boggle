from boggle import Boggle
from flask import Flask, render_template, session, redirect, request, jsonify
from flask_debugtoolbar import DebugToolbarExtension

boggle_game = Boggle()

app = Flask(__name__)

# For debugtoolbar
app.config['SECRET_KEY'] = 'kevin'
debug = DebugToolbarExtension(app)
# Prevents debugger from stopping redirct
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


high_score = 0


@app.route('/')
def create_board():
    game_board = boggle_game.make_board()
    session['board'] = game_board
    games_played = session.get('games_played', 0)
    high_score = session.get('high_score', 0)

    return render_template('board.html', board=game_board)


@app.route('/check-word')
def validate_word():
    word = request.args['word_value']
    board = session['board']
    return jsonify(boggle_game.check_valid_word(board, word))


@app.route('/stats', methods=["POST"])
def update_stats():
    score = request.json['game_score']
    # ? Why do I have to use get and not same as validate_word board
    # games_played = session['games_played']
    # high_score = session['high_score']
    games_played = session.get('games_played', 0)
    high_score = session.get('high_score', 0)
    games_played += 1
    session['games_played'] = games_played
    if int(score) > int(high_score):
        high_score = score
    session['high_score'] = high_score
    return jsonify(games_played)
