from flask import Flask, request
from flask_cors import CORS
import login

app = Flask(__name__)
CORS(app)


@app.route("/process_data", methods=["POST"])
def process_data() -> dict:
  user_data = request.get_json()
  user_request = user_data["request"]
  login_info = user_data["login_info"]
  match user_request:
      case "login":
        return login.LoginStatus(login_info)
      case "new account":
        return login.CreateUser(login_info)
      case "add_classes":
        login.AddAllClasses(login_info["email"], user_data["class_list"])
      case "load_global":
        return login.LoadClasses(login_info)

  return {}

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True) # Change this


