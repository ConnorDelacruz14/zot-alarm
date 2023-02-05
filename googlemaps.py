import requests

api_key = "AIzaSyDnduWKdpEGqDnQ1NZAzaZh3wnVGeZRfG4"
address = "Political Sceince, Irvine, CA"
#address = "In, Irvine, CA"

url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}"

response = requests.get(url)

# print(response.json())

# Matthew = [{"9:00-10:00", "Klefstad", "DBH6011", "ICS51"}, ...]
# check = Matthew[0]["bldg"].split(" ")
# official = check[0]
# address = store_dictionary[official]
# address += "Irvine, CA"

store_dictionary = {"APL" : "Air Pollution Labs", "ALH": "Aldrich Hall", "ACRC": "Anteater Community Resource Center", "AIRB": "Anteater Instruction and Research Building", "ALP" : "Anteater Learning Pavilion", \
    "ART" : "Art Studio", "ACT" : "Art, Culture and Technology", "AITR" : "Arts Instruction and Technology Resource Center", "AIRB" : "Anteater Instruction and Researach Building", "ARC" : "Anteater Recreation Center", "ANTHRO": "Anthropology", "ART" : "Art", "ART HIS" : "Art History", \
        "ASIANAM" : "Asian American Studies", "ASUCI" : "Associated Students of UCI", "BLI" : "Beckman Laser Institute", "BH" : "Berk Hall Nursing Science", "BS3" : "Biological Sciences 3", "BME" : "Biomedical Engineering", \
            "BRL" : "Bonney Research Laboratory", "Calit2" : "325 Engineering Quad", "CHP" : "Caampuswide Honors Program", "CNLM" : "Center for the Neurobiology of Learning and Memory", \
                "CBEMS" : "Chemical Engineering & Materials Science", "CHEM" : "Chemistry", "CHC/LAT" : "383 Social Science Tower", "CTT" : "Claire Trevor Theatre", "CLASSIC" : "400 Murray Krieger Hall", "COGS": "Cognitive Sciences", "COM LIT" : "Comparative Literature", "CAC" : "Contempory Arts Center", "DCE" : "510 E Peltason Dr", \
                    "CRM/LAW" : "2340 Social Ecology 2", "CCC" : "Cross Cultural Center", "DANCE" : "301 Mesa Arts Building", "DEV BIO" : "2212 Biological Sciences 3", "DSC" :} #hicf

#d


store_dictoinary2 = {"ICS": "Information and Computer Science", "ICS2": "Information and Computer Science 2", "IAB": "Intercollegiate Athletic Building", \
                    "ISEB": "Interdisciplinary Science and Engineering Building", "ICF": "Interim Classroom Facility", "IH": "Joan Irvine Smith Hall", \
                    "CRH": "John V. Croul Hall", "KH": "Krieger Hall", "LLIB": "Langson Library", "LAW": "Law Building", "MDE": "McDonnel Douglas Engineering Auditorium", \
                    "MH": "McGaugh Hall", "SB1": "Merage School of Business", "SB2": "Merage School of Business 2", "MAB": "Mesa Arts Building", \
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
                    "UNEX": "231 Social Sciences Quad"}

#store_locations = {'DBH': "Donald Bren Hall, Irvine, CA", }

if response.status_code == 200:
    response_json = response.json()
    #print(response_json)
    northeast_lat_upper = response_json["results"][0]["geometry"]
    print(northeast_lat_upper)
    # southwest_lat_lower = response_json["results"][0]["geometry"]["bounds"]["southwest"]["lat"]
    # northeast_long_upper = response_json["results"][0]["geometry"]["bounds"]["northeast"]["lng"]
    # southwest_long_lower = response_json["results"][0]["geometry"]["bounds"]["southwest"]["lng"]
    # location = response_json["results"][0]["geometry"]["location"]
    # latitude = location["lat"]
    # longitude = location["lng"]
    # print(f"Latitude: {latitude}, Longitude: {longitude}")
#{'DBH' : 'Donald Bren Hall, Irvine, CA'}
else:
    print("Failed to retrieve coordinates.")