from flask import Flask, request
import json
from UItest import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

test_data = {"attendance_rate": "97", "on_time_rate": "84", "tuition_lost": 442, "next_class": "I&C SCI 6D"}

@app.route("/process_data", methods=["POST"])
def process_data():
  # data = request.get_json()
  classList = request.get_json()
  print("Number of classes: ", len(classList))
  for _class in classList:
    print(_class['departmentName'])
    print(_class['courseNumber'])
    print(_class['courseCode'])
    print()
    
  return json.dumps(classList)

if __name__ == "__main__":
  app.run()