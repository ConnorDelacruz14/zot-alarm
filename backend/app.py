from flask import Flask, request
from UItest import *
from flask_cors import CORS
import login

app = Flask(__name__)
CORS(app)

def printData(class_list) -> None:
  print("Number of classes: ", len(class_list))
  for _class in class_list:
    print(_class)


@app.route("/process_data", methods=["POST"])
def process_data() -> dict:
  user_data = request.get_json()
  user_request = user_data["request"]

  match user_request:
      case "login":
        return login.LoginStatus(user_data)
      case "new account":
        return login.CreateUser(user_data)
      case "add classes":
        login.AddAllClasses(user_data["email"], user_data["classes"])
  
  return {}

if __name__ == "__main__":
  app.run()


