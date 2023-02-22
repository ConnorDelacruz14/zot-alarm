from flask import Flask, request
import json
from googlemaps import *
# from UItest import *

app = Flask(__name__)
c_list = []


@app.route("/process_data", methods=["POST"])
def process_data():
  in_class = checkCoordinates(-117.7, 33.6, c_list, "I&C SCI", "45C", 35630)
  # global input_data
  # input_data = request.get_json()

  # Perform processing on input_data
  
  # processed_data = { ... }



  return json.dumps(processed_data)

if __name__ == "__main__":
  #  app.run()
  process_data()