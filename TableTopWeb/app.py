# Name: app.py
# Description: Main app for TableTopWeb, a page holding common utilities for tabletop gaming.
#              Please install requirements in requirements.txt first.
import sys
from flask import Flask, render_template, flash,request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View, Text
from boardgamegeek import BoardGameGeek
from wtforms import StringField, SubmitField, validators
from flask_wtf import Form

app = Flask(__name__)
scoreboard_dict = dict()
current_room_id = 0

class scoreboard_form(Form):
    player_names_field = StringField('Player Names:', [validators.DataRequired()], description='Input your player names seperated by commas. (e.g. Shaun, Ryan, Junsheng)')
    submit_button = SubmitField("Let's Play!!")

@app.route('/')
def index():
    # TODO: Homepage & dice roller
    return render_template('index.html')

@app.route('/scoreboard', methods=['GET', 'POST'])
def scoreboard():
    global current_room_id
    form = scoreboard_form()
    if request.method == 'POST' and form.validate():
        input = form.player_names_field.data
        list_of_names = input.split(",")
        current_room_id+=1
        scoreboard_dict[current_room_id]={}
        for i in range(len(list_of_names)):
            list_of_names[i] = list_of_names[i].strip()
            scoreboard_dict[current_room_id][list_of_names[i]] = 0
        print(scoreboard_dict)
        return redirect(url_for('scoreboardid', id=current_room_id))
    return render_template('scoreboard_home.html', form=form)

@app.route('/scoreboard/<id>')
def scoreboardid(id):
    global current_room_id
    try:
        if scoreboard_dict[int(id)]:
            print("HERE! {0}".format(scoreboard_dict[int(id)]))
            return render_template('scoreboard.html', id=int(id), result=scoreboard_dict[int(id)])
    except:
        e = sys.exc_info()[0]
        print(e)
        return render_template('invalid_scoreboard.html')


@app.route('/trending_games')
def trending_games():
    #TODO: trending_games
    bgg = BoardGameGeek()
    hot_items_dict = dict()
    for item in bgg.hot_items("boardgame"):
        hot_items_dict[item.id] = item.name
    return render_template('page.html', hot_items_dict = hot_items_dict)

@app.route('/dice_roller')
def dice_rollers():
    #TODO: dice_roller
    return render_template('dice.html')

if __name__ == '__main__':
    Bootstrap(app)
    app.secret_key = 'devkey'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SECRET_KEY'] = 'devkey'
    app.config['RECAPTCHA_PUBLIC_KEY'] = \
        '6Lfol9cSAAAAADAkodaYl9wvQCwBMr3qGR_PPHcw'
    nav = Nav()
    nav.register_element('top', Navbar(
    View('TableTopWeb', '.index'),
    View('Dice Roller', '.dice_rollers'),
    View('Scoreboard', '.scoreboard'),
    View('Trending Games', '.trending_games'),
    Text('Networks Lab 2 by Junsheng & Shaun'),))
    nav.init_app(app)
    app.run(debug=True, host='0.0.0.0')
