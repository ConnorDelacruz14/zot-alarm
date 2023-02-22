from flask import Flask, request
from UItest import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def printData(class_list):
  print("Number of classes: ", len(class_list))
  for _class in class_list:
    print(_class)

def process_login(login_info):
  # TODO: Check if user is logging in for the first time
  first_login = True
  
  return {"first_login": first_login} 

@app.route("/process_data", methods=["POST"])
def process_data():
  user_data = request.get_json()

  # Check if data is for login
  if len(user_data) == 2:
      print(user_data)
      return process_login(user_data)

  print("Login info: ", user_data["login_info"])
  print("Current position: ", user_data["location"])
  printData(user_data["class_list"])

  #TODO: Process ^^^^^

  #TODO: Return -> Tution, other stats
  return user_data

if __name__ == "__main__":
  app.run()


