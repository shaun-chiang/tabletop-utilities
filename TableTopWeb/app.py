from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # TODO: Homepage & dice roller
    return render_template('index.html')

@app.route('/scoreboard')
def scoreboard():
    #TODO: scoreboard id
    return 'Yummy cakes!'

@app.route('/rpg_helper')
def rpg_helper(name):
    #TODO: rpg_helper
    return render_template('page.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')