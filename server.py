from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
from content import *

app = Flask(__name__)


# score of the user
# +1 if one part is correct, total score is 12
user_score = 0

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
            "explanation": "There are exactly two candidates in only two cells in the house: 8 and 9 (in green). This is known as Naked Pair",
            "correct": 3,
        },
        "part2":{
            "pattern": "Naked Pair",
             "cells": ['0021', '0022', '1021','1022','1121', '1122','2021', '2022','2121','2122','2221','2222'],
             "explanation": "According to Naked Pair, since only two cells contain exactly two candidates. This means that these two candidates cannot exist in other cells. So that we can eliminate all 8s and 9s in other non-green cells",
             "correct": 12,
        },
    },
    "4":{
        "part1":{
            "pattern": "Naked Pair",
            "cells": ['5', '8'],
            "explanation": "There are exactly two candidates in only two cells in the house: 6 and 7 (in green). This is known as Naked Pair",
            "correct": 3,
        },
        "part2":{
            "pattern": "Naked Pair",
            "cells": ['0020', '0412', '0420'],
            "explanation": "According to Naked Pair, since only two cells contain exactly two candidates. This means that these two candidates cannot exist in other cells. So that we can eliminate all 6s and 7s in other non-green cells",
            "correct": 3,
        },
    },
    "3":{
        "part1":{
            "pattern": "Hidden Pair",
            "cells": ['4', '6'],
            "explanation": "There are exactly two candidates that exist in only two cells in the house: 1 and 9 (in gree). This is known as Hidden Pair",
            "correct": 3,
        },
        "part2":{
            "pattern": "Hidden Pair",
            "cells": ['1112'],
            "explanation": "According to Hidden Pair, since only two cells contain 1s and 9s, 1s and 9s can only exist in these two cells. Other candidates in these two cells are not feasible, so we can eliminate other candidates.",
            "correct": 1,

        },
    },
    "2":{
        "part1":{
            "pattern": "Hidden Pair",
            "cells": ['1', '6'],
            "correct": 6,
            "explanation": "There are exactly two candidates that exist in only two cells in the house: 2 and 5 (in green). This is known as Hidden Pair",
        },
        "part2":{
            "pattern": "Hidden Pair",
            "cells": ['0102', '0110', '0610'],
            "correct": 3,
            "explanation": "According to Hidden Pair, since only two cells contain 2s and 5s, 2s and 5s can only exist in these two cells. Other candidates in these two cells are not feasible, so we can eliminate other c.",
        },
    },
    "5":{
        "part1":{
            "pattern": "X-wing",
            "cells": ['12', '16', '52', '48'],
            "correct": 5,
            "explanation": "On the 2nd and 6th row, there are only two 7s and they are on the same column. This is known as X-wing.",
        },
        "part2":{
            "pattern": "X-wing",
            "cells": ['0320', '4320', '7320', '7720', '8320', '8720'],
            "correct": 6,
            "explanation": "According to X-wing, since there are exactly two 7s on two rows along the same column, 7s must appear on either two of these four cells. Thus, we can eliminate other 7s from other cells."
        },
    },
    "6":{
        "part1":{
            "pattern": "Hidden Pair",
            "cells": ['3', '5', '7'],
            "correct": 4,
            "explanation":"There are exactly three candidates that exist in only three cells in the house: 2, 5, and 6 (in green). This is known as Hidden Pair/Set",
        },
        "part2":{
            "pattern": "Hidden Pair",
            "cells": ['0300', '0310', '0320', '0321', '0500', '0510', '0521', '0700', '0702', '0710', '0721'],
            "correct": 11,
            "explanation": "This is an advanced version of Hidden Pair, known as Hidden Set. According to Hidden Pair, since only three cells contain 2s, 5s and 6s, 2s, 5s and 6s can only exist in these three cells. Other candidates in these three cells are not feasible, so we can eliminate other candidates.",
        },
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
    "4":{
        "arrangement": [0,9,5,3,0,0,2,4,0],
        "candidates": [[1,7,8],[],[],[],[1,6,7,8],[6,7],[],[],[6,7]],
        "format": (1,9),
    },
    "3":{
        "arrangement": [0,0,4,0,0,5,0,3,0],
        "candidates": [[6,7,8],[2,6],[],[2,7],[1,6,9],[],[1,9],[],[2,7,8]],
        "format": (3,3),
    },
    "2":{
        "arrangement": [1,0,6,9,0,8,0,0,0],
        "candidates": [[],[2,3,4,5],[],[],[3,7],[],[2,4,5],[3,4,7],[4,7]],
        "format": (1,9),
    },
    "5":{
        "arrangement": 
        [1,0,0,0,0,0,5,6,9,
         4,9,2,0,5,6,1,0,8,
         0,5,6,1,0,9,2,4,0,
         0,0,9,6,4,0,8,0,1,
         0,6,4,0,1,0,0,0,0,
         2,1,8,0,3,5,6,0,4,
         0,4,0,5,0,0,0,1,6,
         9,0,5,0,6,1,4,0,2,
         6,2,1,0,0,0,0,0,5],
        "candidates": [[],[3,7,8],[3,7],[2,3,4,7,8],[2,7,8],[2,3,4,7,8],[],
        [],[],[],[],[],[3,7],[],[],[],[3,7],[],[3,7,8],[],[],[],[7,8],[],[],[],[3,7],
        [3,5,7], [3,7],[],[],[],[2,7],[],[2,5],[],[5,7],[],[],[2,7,8,9],[],[2,7,8],
        [3,7,9],[2,5],[3,7],[],[],[],[7,9],[],[],[],[7,9],[],[3,7,8],[],[3,7],[],[2,7,8,9],
        [2,3,7,8],[3,7,9],[],[],[],[3,7,8],[],[3,7,8],[],[],[],[3,7,8],[],[],[],[],[3,4,7,8],
        [7,8,9],[3,4,7,8],[3,7,9],[3,7,8,9],[]],
        "format": (9,9),
    },
    "6":{
        "arrangement": [0,0,0,0,0,0,9,0,0],
        "candidates": [[1,4],[1,3,7],[1,3,4,7],[1,2,4,5,6,7,8],[1,3,4,7,8],[1,2,4,5,6,8],[],[1,2,3,4,6,8],[1,3,4]],
        "format": (1,9),
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
    return render_template('quiz_part1.html', id=id, question=question)


@app.route('/answer/<id>/part1', methods=['GET', 'POST'])
def answer_part1(id):
    for key, value in solutions.items():
        if key == str(id):
            solution = value['part1']
            question = questions[key]
            answer = user_answers[key]["part1"]
    return render_template('quiz_part1_answer.html', id=id, solution=solution, question=question, answer=answer)


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
        user_answer = user_answers[id]["part2"]
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
            answer = user_answers[key]["part2"]
    return render_template('quiz_part2_answer.html', id=id, solution1=solution1, solution2=solution2, question=question, answer=answer)

@app.route('/score', methods=['GET', 'POST'])
def score():
    return render_template("score.html", score=user_score)

if __name__ == '__main__':
    app.run(debug=True)
