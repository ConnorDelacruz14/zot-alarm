from flask import Flask, request
from UItest import *
from flask_cors import CORS
from login import LoginStatus

app = Flask(__name__)
CORS(app)

def printData(class_list) -> None:
  print("Number of classes: ", len(class_list))
  for _class in class_list:
    print(_class)


@app.route("/process_data", methods=["POST"])
def process_data() -> dict:
  user_data = request.get_json()
  # Check if data is for login
  if len(user_data) == 2:
      return LoginStatus(user_data)
  else:
    return 
      
  return {}

if __name__ == "__main__":
  app.run()


