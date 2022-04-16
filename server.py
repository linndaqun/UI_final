from flask import Flask
from flask import render_template
from flask import Response, request, jsonify

app = Flask(__name__)


# score of the user
user_score = 0

# store answers of the user
user_answers = {
    "1":{
        "part1":{
            "pattern": "",
            "cells": [],
        },
        "part2":{},
    },
    "2":{
        "part1":{
            "pattern": "",
            "cells": [],
        },
        "part2":{},
    },
    "3":{
        "part1":{
            "pattern": "",
            "cells": [],
        },
        "part2":{},
    },
    "4":{
        "part1":{
            "pattern": "",
            "cells": [],
        },
        "part2":{},
    },
    "5":{
        "part1":{
            "pattern": "",
            "cells": [],
        },
        "part2":{},
    },
    "6":{
        "part1":{
            "pattern": "",
            "cells": [],
        },
        "part2":{},
    }
}

'''
    store correct answer
    pattern: "naked pair" / "hidden pair" / "x-wing"
    cells: at least one cell numbered from "1" to "9" 
    "1" "2" "3"
    "4" "5" "6"
    "7" "8" "9"
    part 2 will be a dictionary with cell number as key, candidate array as value
        eg. "1": [2, 3, 4]'''
solutions = {
    "1":{
        "part1":{
            "pattern": "naked",
            "cells": ['10', '41'],
            "correct": 3,
        },
        "part2":{},
    },
    "2":{
        "part1":{
            "pattern": "",
            "cells": [],
        },
        "part2":{},
    },
    "3":{
        "part1":{
            "pattern": "",
            "cells": [],
        },
        "part2":{},
    },
    "4":{
        "part1":{
            "pattern": "",
            "cells": [],
        },
        "part2":{},
    },
    "5":{
        "part1":{
            "pattern": "",
            "cells": [],
        },
        "part2":{},
    },
    "6":{
        "part1":{
            "pattern": "",
            "cells": [],
        },
        "part2":{},
    }
}

'''
    store questions
    arrangement is an array representing filled cells. For unfilled cells, use 0 instead
    candidates is an array or array representing candidates of untill cells
    format is tuple representing the number of rows and columns
'''
questions = {
    "1":{
        "arrangement": [0,0,7,0,0,0,0,0,0],
        "candidates": [[5,8,9],[8,9],[],[1,2,4,8,9],[1,2,4,8,9],[8,9],[4,5,6,8,9],[3,4,6,8,9],[3,5,8,9]],
        "format": (3,3),
    },
    "2":{
        "arrangement": [],
        "candidates": [],
        "format": (),
    },
    "3":{
        "arrangement": [],
        "candidates": [],
        "format": (),
    },
    "4":{
        "arrangement": [],
        "candidates": [],
        "format": (),
    },
    "5":{
        "arrangement": [],
        "candidates": [],
        "format": (),
    },
    "6":{
        "arrangement": [],
        "candidates": [],
        "format": (),
    },
}

@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/learn/<id>', methods=['GET', 'POST'])
def learn():
    return render_template('learn.html')


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    return render_template('quiz.html')

@app.route('/quiz/<id>/part1')
def part1(id):
    for key, value in questions.items():
        if key == str(id):
            question = value
    return render_template('quiz_part1.html', id=id, question=question)

@app.route('/quiz/<id>/part1', methods=['GET', 'POST'])
def quiz_part1(id):
    global user_score
    for key, value in questions.items():
        if key == str(id):
            question = value
    
    json_data = request.get_json()
    id = json_data['id']
    technique = json_data['pattern']
    cells = json_data['cells']
    
    user_answer = user_answers[id]["part1"]
    user_answer['pattern'] = technique
    user_answer['cells'] = cells
    
    solution = solutions[id]["part1"]
    correct = 0
    if solution['pattern'] == technique:
        correct += 1
        if len(cells) == len(solution['cells']):
            for cell in cells:
                if cell in solution['cells']:
                    correct += 1
    if correct == solution['correct']:
        user_score += 1
    
    print(user_score)
    return render_template('quiz_part1.html', id=id, question=question)


@app.route('/answer/<id>/part1', methods=['GET', 'POST'])
def answer_part1(id):
    global user_score

    for key, value in solutions.items():
        if key == str(id):
            solution = value
    return render_template('quiz_part1_answer.html', id=id, solution=solution)


@app.route('/quiz/<id>/part2', methods=['GET', 'POST'])
def quiz_part2(id):
    for key, value in questions.items():
        if key == str(id):
            question = value
    return render_template('quiz_part2.html', id=id, question=question)


@app.route('/answer/<id>/part1', methods=['GET', 'POST'])
def answer_part2(id):
    for key, value in solutions.items():
        if key == str(id):
            solution=value
    return render_template('quiz_part2_answer.html', id=id, solution=solution)


if __name__ == '__main__':
    app.run(debug=True)
