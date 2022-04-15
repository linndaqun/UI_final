from crypt import methods
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify

app = Flask(__name__)

# score of the user
score = 0

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
solution = {
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

@app.route('/')
def homepage():
   return render_template('home.html')

@app.route('/learn/<id>', methods=['GET', 'POST'])

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    return render_template('quiz.html')

@app.route('/quiz/<id>/part1', methods=['GET', 'POST'])
def quiz_part1(id):
    return render_template('quiz_part1.html')

@app.route('/answer/<id>/part1', methods=['GET', 'POST'])
def answer_part1(id):
    return render_template('quiz_part1_answer.html')

@app.route('/quiz/<id>/part2', methods=['GET', 'POST'])
def quiz_part2(id):
    return render_template('quiz_part2.html')

@app.route('/answer/<id>/part1', methods=['GET', 'POST'])
def answer_part2(id):
    return render_template('quiz_part2_answer.html')

if __name__ == '__main__':
   app.run(debug = True)