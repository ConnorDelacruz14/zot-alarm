# from flask import Flask, request
# import json
# from UItest import *

# app = Flask(__name__)

# @app.route("/process_data", methods=["POST"])
# def process_data():
#   global input_data
#   input_data = request.get_json()

#   # Perform processing on input_data
  
#   processed_data = { ... }
#   return json.dumps(processed_data)

# if __name__ == "__main__":
#   app.run()