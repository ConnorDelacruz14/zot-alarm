from flask import Flask, request
import json
from UItest import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def printData(class_list):
  print("Number of classes: ", len(class_list))
  for _class in class_list:
    print(_class['departmentName'], _class['courseNumber'], _class['courseCode'])

@app.route("/process_data", methods=["POST"])
def process_data():
  # data = request.get_json()
  user_data = request.get_json()
  print("Login info: ", user_data["login_info"])
  print("Current position: ", user_data["location"])
  printData(user_data["class_list"])

  return user_data

if __name__ == "__main__":
  app.run()


