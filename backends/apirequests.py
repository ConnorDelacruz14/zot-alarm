import requests

courses = requests.get("https://api.peterportal.org/rest/v0/courses/all")
courses_data = courses.json()

for course in courses_data:
    course_dict = dict(course)
    id_name = course_dict["id"]
    department = course_dict["department"]
    print(id_name, department)