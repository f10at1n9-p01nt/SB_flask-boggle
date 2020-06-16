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


@app.route('/')
def create_board():
    game_board = boggle_game.make_board()
    session['board'] = game_board

    return render_template('board.html', board=game_board)


@app.route('/check-word')
def validate_word():
    word = request.args['word_value']
    board = session['board']
    return jsonify(boggle_game.check_valid_word(board, word))
