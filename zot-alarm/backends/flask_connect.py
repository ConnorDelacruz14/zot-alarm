from flask import Flask, request
import json
from UItest import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def printData(class_list):
  print("Number of classes: ", len(class_list))
  for _class in class_list:
    print(_class)

@app.route("/process_data", methods=["POST"])
def process_data():
  user_data = request.get_json()
  print("Login info: ", user_data["login_info"])
  print("Current position: ", user_data["location"])
  printData(user_data["class_list"])

  #TODO: Process ^^^^^

  #TODO: Return -> Tution, other stats

  return user_data

if __name__ == "__main__":
  app.run()


