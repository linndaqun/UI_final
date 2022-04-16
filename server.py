from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
from content import *

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('home.html', home=home_data)


@app.route('/learn/<learn_id>', methods=['GET', 'POST'])
def learn(learn_id):
    return render_template('learn.html', learn=learns_data[int(learn_id)-1])


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    return render_template('quiz.html')


@app.route('/quiz/<id>/part1', methods=['GET', 'POST'])
def quiz_part1():
    return render_template('quiz_part1.html')


@app.route('/answer/<id>/part1', methods=['GET', 'POST'])
def answer_part1():
    return render_template('quiz_part1_answer.html')


@app.route('/quiz/<id>/part2', methods=['GET', 'POST'])
def quiz_part2():
    return render_template('quiz_part2.html')


@app.route('/answer/<id>/part1', methods=['GET', 'POST'])
def answer_part2():
    return render_template('quiz_part2_answer.html')


if __name__ == '__main__':
    app.run(debug=True)
