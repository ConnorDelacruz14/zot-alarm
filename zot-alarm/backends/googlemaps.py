import requests
from UItest import *

#################################

from flask import Flask, request
import json


app = Flask(__name__)

@app.route("/query_example", methods=["POST"])

def process_data():
    input_data = request.get_json()
    courses = add_courses(input_data)

  # Perform processing on input_data
    api_key = "AIzaSyDnduWKdpEGqDnQ1NZAzaZh3wnVGeZRfG4"
#ffdsa

    store_dictionary = {"APL" : "Air Pollution Labs", "ALH": "Aldrich Hall", "ACRC": "Anteater Community Resource Center", "AIRB": "Anteater Instruction and Research Building", \
        "ALP" : "Anteater Learning Pavilion", "ART" : "Art Studio", "ACT" : "Art, Culture and Technology", "AITR" : "Arts Instruction and Technology Resource Center", \
        "AIRB" : "Anteater Instruction and Researach Building", "ARC" : "Anteater Recreation Center", "ANTHRO": "Anthropology", "ART" : "Art", "ART HIS" : "Art History", \
        "ASIANAM" : "Asian American Studies", "ASUCI" : "Associated Students of UCI", "BLI" : "Beckman Laser Institute", "BH" : "Berk Hall Nursing Science", "BS3" : "Biological Sciences 3", \
        "BME" : "Biomedical Engineering", "BRL" : "Bonney Research Laboratory", "Calit2" : "325 Engineering Quad", "CHP" : "Caampuswide Honors Program", \
        "CNLM" : "Center for the Neurobiology of Learning and Memory", "CBEMS" : "Chemical Engineering & Materials Science", "CHEM" : "Chemistry", \
        "CHC/LAT" : "383 Social Science Tower", "CTT" : "Claire Trevor Theatre", "CLASSIC" : "400 Murray Krieger Hall", "COGS": "Cognitive Sciences", \
        "COM LIT" : "Comparative Literature", "CAC" : "Contempory Arts Center", "DCE" : "510 E Peltason Dr", "CRM/LAW" : "2340 Social Ecology 2", \
        "CCC" : "Cross Cultural Center", "DANCE" : "301 Mesa Arts Building", "DEV BIO" : "2212 Biological Sciences 3", "DSC" : "234 Social Sciences Quad", \
        "DBH" : "314 Engineering Quad", "DRAMA" : "249 Drama Building", "DRA" : "715 Arts Quad", "EARTHSS" : "3200 Croul Hall", "E ASIAN" : "443 Humanities Instructional Building", \
        "ECO EVO": "321 Steinhaus Hall", "ECON": "3223 Social Science Plaza B", "EDUC": "401 E Peltason Dr", "EECS": "2213 Engineering Hall", "ECT": "Engineering Computing Trailers", \
        "EG": "321 Engineering Quad", "EH": "308 Engineering Quad", "ELF": "323 Engineering Quad", "ELH": "305 Engineering Quad", "ET": "205 Engineering Quad", \
        "ENGRCEE": "e4130 Engineering Gateway", "ENGLISH": "435 Humantities Instructional Building", "EHS": "4600 Health Sciences Road", "ELS": "243 Humanities Intructional Building", \
        "FM": "201 Facilities Management Building", "FRF": "Faculty Research Building", "FLM&MDA": "2000 Humanities Gateway", "FRH": "4129 Frederick Reines Hall", "GNRF": "827 Medical Sciences Quad", \
        "HRH": "843 Medical Sciences Quad", "HISTORY": "200 Murray Krieger Hall", "HAS": "Student Center", "HSLH": "Howard Schneiderman Lecture Hall", "HG": "611 Humanities Gateway", "HH": "Humantities Hall", \
        "HIB": "610 Humanities Quad", "HICF": "523 Humanities Quad", "HRI": "Humantities Gateway", "IN4MATX": "5019 Donald Bren Hall", "ICS": "Information and Computer Science", \
        "ICS2": "Information and Computer Science 2", "IAB": "Intercollegiate Athletic Building", "ISEB": "Interdisciplinary Science and Engineering Building", \
        "ICF": "Interim Classroom Facility", "IH": "Joan Irvine Smith Hall", "CRH": "John V. Croul Hall", "KH": "Krieger Hall", "LLIB": "Langson Library", \
        "LAW": "Law Building", "MDE": "McDonnel Douglas Engineering Auditorium", "MH": "McGaugh Hall", "SB1": "Merage School of Business", "SB2": "Merage School of Business 2", "MAB": "Mesa Arts Building", \
        "MOB": "Mesa Office Building", "MPAA": "Multipurpose Academic and Administrator", "MSTB": "Multipurpose Science and Technology Building", \
        "MKH": "Murray Kreiger Hall", "MUSIC": "Music", "MM": "Music and Media Building", "NS1": "Natural Science 1", "NS2": "Natural Science 2", \
        "NEURBIO": "Neurobiology and Behavior", "OIT": "Office of Information Technology", "PCB": "Parkview Classroom Building", "MGMT": "Paul Merage School of Business", \
        "PHRMSCI": "Pharmaceutical Sciences", "PHILOS": "Philosophy", "PSCB": "Physical Sciences Classroom Building", "PSLH": "Physical Sceinces Lecture Hall", \
        "PHYSICS": "Physics and Astronomy", "PP&D": "Planning, Policy, and Design", "PH": "Plumwood House", "POL SCI": "Political Science", \
        "PSB": "Public Services", "QRL": "Qureshy Research Laboratory", "REC": "Rockwell Engineering Center", "RH": "Rowland Hall", "SLIB": "Science Library", \
        "SCS": "Sculpture, Ceramic Studios, Nixon Theatre", "SBSG": "Social and Behavioral Sciences Gateway", "SE": "Social Ecology", "SE2": "Social Ecology 2", \
        "SSH": "Social Science Hall", "SSL": "Social Science Lab", "SSLH": "Social Science Lecture Hall", "SSPA": "Social Science Plaza A", "SSPB": "Social Science Plaza B", \
        "SST": "Social Science Tower", "SSTR": "Social Science Trailer", "SOCIOL": "4215 Social Science Plaza B", "SPANISH&PORTUG": "Spanish and Portugal", "SPH": "Sprague Hall", \
        "STATS": "Donald Bren Hall", "SH": "Steinhaus Hall", "SC": "Student Center", "SHC": "Student Health Center", "SS1": "Student Services 1", "STU4": "Studio 4", \
        "UNEX": "231 Social Sciences Quad", "PSTU": "William J. Gillespie Performance Studios", "WSH": "Winifred Smith Hall", "WOMN ST": "Women's Studies"}



    courses = add_courses([], input_data)
    check = courses["bldg"].split(" ")
    official = check[0]
    address = store_dictionary[official]
    address += "Irvine, CA"


    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}"

    response = requests.get(url)


    if response.status_code == 200:
        x, y = 33.649349, -117.84238
        response_json = response.json()
        northeast_lat_upper = response_json["results"][0]["geometry"]["bounds"]["northeast"]["lat"]
        southwest_lat_lower = response_json["results"][0]["geometry"]["bounds"]["southwest"]["lat"]
        northeast_long_upper = response_json["results"][0]["geometry"]["bounds"]["northeast"]["lng"]
        southwest_long_lower = response_json["results"][0]["geometry"]["bounds"]["southwest"]["lng"]
        location = response_json["results"][0]["geometry"]["location"]
        latitude = location["lat"]
        longitude = location["lng"]
        print(southwest_lat_lower, northeast_lat_upper, southwest_long_lower, northeast_long_upper)
        xmin, xmax, ymin, ymax = southwest_long_lower, northeast_long_upper, southwest_lat_lower, northeast_lat_upper
        if xmin <= x <= xmax and ymin <= y <= ymax:
            if is_attended():
                print(find_next_class())
            else:
                quit()
        else:
            print("Failed to retrieve location.")


    #processed_data = { ... }
    return# json.dumps(processed_data)

if __name__ == "__main__":
  app.run()