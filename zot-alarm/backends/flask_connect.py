from flask import Flask, request
import json
from UItest import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def printData(classList):
  print("Number of classes: ", len(classList))
  for _class in classList:
    print(_class['departmentName'], _class['courseNumber'], _class['courseCode'])

@app.route("/process_data", methods=["POST"])
def process_data():
  # data = request.get_json()
  classList = request.get_json()
  printData(classList)

  return json.dumps(classList)

if __name__ == "__main__":
  app.run()


