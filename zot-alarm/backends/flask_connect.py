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

@app.route("/process_data", methods=["POST"])
def process_data():
  user_data = request.get_json()

  # Check if data is for login
  if len(user_data) == 2:
      print(user_data)
      if not database_connect.FirstLogin(user_data["email"], user_data["password"]) and database_connect.CorrectLoginInfo(user_data["email"], user_data["password"]):
          return {"status": "correct login"}
      elif database_connect.FirstLogin(user_data["email"], user_data["password"]):
          return {"status": "new login"} 
      else:
          return {"status": "incorrect login"}

  return user_data

if __name__ == "__main__":
  app.run()


