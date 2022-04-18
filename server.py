from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
from content import *

app = Flask(__name__)


# score of the user
# +1 if one part is correct, total score is 12
user_score = 0
total_score = 12

# store answers of the user
user_answers = {
    "1":{
        "part1":{
            "pattern": "",
            "cells": [],
        },
        "part2":{
            "cells": [],
        },
    },
    "2":{
        "part1":{
            "pattern": "",
            "cells": [],
        },
        "part2":{
            "cells": [],
        },
    },
    "3":{
        "part1":{
            "pattern": "",
            "cells": [],
        },
        "part2":{
            "cells": [],
        },
    },
    "4":{
        "part1":{
            "pattern": "",
            "cells": [],
        },
        "part2":{
            "cells": [],
        },
    },
    "5":{
        "part1":{
            "pattern": "",
            "cells": [],
        },
        "part2":{
            "cells": [],
        },
    },
    "6":{
        "part1":{
            "pattern": "",
            "cells": [],
        },
        "part2":{
            "cells": [],
        },
    }
}

'''
    store correct answer
    pattern: "naked pair" / "hidden pair" / "x-wing"
    cells: correct answer based on its index, index = row_index * row + col_index
    correct is the number of correct answers, sum of 1 + the number of matched cells
    explanation is the explanation to the answer
    part 2 will be a dictionary with cell number as key, candidate array as value
        eg. "1": ['2', '3', '4']    
    '''
solutions = {
    "1":{
        "part1":{
            "pattern": "Naked Pair",
            "cells": ['1', '5'],
            "explanation": "There are exactly two candidates in only two cells in the house: 8 and 9 (in red). This is known as Naked Pair",
            "correct": 3,
        },
        "part2":{
            "pattern": "Naked Pair",
             "cells": ['0021', '0022', '1021','1022','1121', '1122','2021', '2022','2121','2122','2221','2222'],
             "explanation": "Eliminate all 8s and 9s in other non-red cells",
             "correct": 12,
        },
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
    return render_template('home.html', home=home_data)


@app.route('/learn/<learn_id>', methods=['GET', 'POST'])
def learn(learn_id):
    return render_template('learn.html', learn=learns_data[int(learn_id)-1])


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
    for key, value in solutions.items():
        if key == str(id):
            solution = value['part1']
            question = questions[key]
    return render_template('quiz_part1_answer.html', id=id, solution=solution, question=question)


@app.route('/quiz/<id>/part2', methods=['GET', 'POST'])
def quiz_part2(id):
    global user_score
    for key, value in solutions.items():
        if key == str(id):
            solution1 = value['part1']
            solution2 = value['part2']
            question = questions[key]
    if request.method == 'POST':
        json_data = request.get_json()
        user_answer = user_answers[id]["part1"]
        user_answer['cells'] = json_data['cells']
        solution = solutions[id]["part2"]
        correct = 0

        if len(user_answer['cells']) == len(solution['cells']):
            for cell in user_answer['cells']:
                if cell in solution['cells']:
                    correct += 1
        if correct == solution['correct']:
                user_score += 1
        print(user_score)

    return render_template('quiz_part2.html', id=id, question=question, solution1=solution1, solution2=solution2)


@app.route('/answer/<id>/part2', methods=['GET', 'POST'])
def answer_part2(id):
    for key, value in solutions.items():
        if key == str(id):
            solution1 = value['part1']
            solution2 = value['part2']
            question = questions[key]
    return render_template('quiz_part2_answer.html', id=id, solution1=solution1, solution2=solution2, question=question)


if __name__ == '__main__':
    app.run(debug=True)
