from flask import Flask, request, jsonify
import json

app = Flask(__name__)

global data

# read data from file and store in global variable data
with open('data.json') as f:
  data = json.load(f)


@app.route('/')
def hello_world():
  return 'Hello, World!'  # return 'Hello World' in response


@app.route('/students/<id>')
def get_student(id):
  for student in data:
    if student['id'] == id:  # filter out the students without the specified id
      return jsonify(student)


@app.route('/students')
def get_students():
  result = []
  pref = request.args.get('pref')  # get the parameter from url
  if pref:
    for student in data:  # iterate dataset
      if student[
          'pref'] == pref:  # select only the students with a given meal preference
        result.append(student)  # add match student to the result
    return jsonify(result)  # return filtered set if parameter is supplied
  return jsonify(data)  # return entire dataset if no parameter supplied


@app.route('/stats')
def get_stats():
  stats = {
      "Chicken": 0,
      "Computer Science (Major)": 0,
      "Computer Science (Special)": 0,
      "Fish": 0,
      "Information Technology (Major)": 0,
      "Information Technology (Special)": 0,
      "Vegetable": 0
  }
  for student in data:
    if student['pref'] in stats:
      stats[student['pref']] += 1
    if student['programme'] in stats:
      stats[student['programme']] += 1
  return jsonify(stats)


@app.route('/add/<a>/<b>')
def add(a, b):
  x = {
      "Sum": 0,
  }
  x['Sum'] = int(a) + int(b)
  return x


@app.route('/subtract/<a>/<b>')
def subtract(a, b):
  x = {
      "Difference": 0,
  }
  x['Difference'] = int(a) - int(b)
  return x


@app.route('/multiply/<a>/<b>')
def mupltiply(a, b):
  x = {
      "Product": 0,
  }
  x['Product'] = int(a) * int(b)
  return x


@app.route('/divide/<a>/<b>')
def divide(a, b):
  x = {
      "Quotient": 0,
  }
  x['Quotient'] = int(a) / int(b)
  return x


app.run(host='0.0.0.0', port=8080, debug=True)
