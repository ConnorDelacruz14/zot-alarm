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
  message = request.get_json().get("message")
  # Perform processing on data
  
  processed_data = { "response": f"Received message: {message}" }
  return json.dumps(processed_data.update({"new_message": "received message"}))

if __name__ == "__main__":
  app.run()