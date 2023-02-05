import requests
  
# api-endpoint
ac_token = "sk.eyJ1Ijoicm5hZGVlbSIsImEiOiJjbGRxaWdpdnoxZGFxM3BxN2hrdjY5anJ3In0.jYNuWs94Kr76n7rjVFXAIQ"
location = input("Enter location: ") #.replace(" ", "%") + " irvine"
location += " irvine"
location = location.replace(" ", "%") #ok





#https://api.mapbox.com/geocoding/v5/mapbox.places/{aldrich\%\hall.json?access_token={access_token}&types=place

#URL = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{location}.json?country=us&bbox=-117.86023450707728%2C33.63126701766686%2C-117.82099590641263%2C33.65777749228097&limit=1&proximity=ip&types=poi&language=en&access_token=sk.eyJ1Ijoicm5hZGVlbSIsImEiOiJjbGRxaWdpdnoxZGFxM3BxN2hrdjY5anJ3In0.jYNuWs94Kr76n7rjVFXAIQ&types=place"
#URL = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{location}.json?country=us&bbox=-117.86023450707728%2C33.63126701766686%2C-117.82099590641263%2C33.65777749228097&limit=1&proximity=ip&types=poi&language=en&access_token=sk.eyJ1Ijoicm5hZGVlbSIsImEiOiJjbGRxaWdpdnoxZGFxM3BxN2hrdjY5anJ3In0.jYNuWs94Kr76n7rjVFXAIQ&types=place"
#varURL = f"https://api.mapbox.com/geocoding/v5/mapbox.places/aldrich\%\hall.json?access_token={ac_token}&types=place"
#varURL = f"https://api.mapbox.com/geocoding/v5/mapbox.places/aldrich\%\hall.json?types=place&access_token={ac_token}" WORKING
#varURL = f"https://api.mapbox.com/geocoding/v5/mapbox.places/University%20of%20California%2C%20Irvine.json?types=place&country=US&access_token={access_token}" #UCI BBOX

#WORKING CURRENT
varURL = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{location}.json?country=US&types=place&limit=1&access_token={ac_token}" 
  
# sending get request and saving the response as response object
r = requests.get(url = varURL)
  
# extracting data in json format
data = r.json()

  
# extracting latitude, longitude and formatted address 
# of the first matching location

  
# printing the output
print(data['features'][0]['bbox'])
print(data['features'][0])




store_boundary = {}