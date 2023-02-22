from flask import Flask, request
from UItest import *
from flask_cors import CORS
import database_connect

app = Flask(__name__)
CORS(app)

def printData(class_list):
  print("Number of classes: ", len(class_list))
  for _class in class_list:
    print(_class)

def process_login(login_info):  
  return {"first_login": database_connect.CheckFirstLogin(login_info["email"], login_info["password"])} 

@app.route("/process_data", methods=["POST"])
def process_data():
  user_data = request.get_json()

  # Check if data is for login
  if len(user_data) == 2:
      print(user_data)
      return process_login(user_data)
  else:
      pass

  #TODO: Return -> Tution, other stats
  return user_data

if __name__ == "__main__":
  app.run()


