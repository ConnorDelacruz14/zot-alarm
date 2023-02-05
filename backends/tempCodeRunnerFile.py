courses = requests.get("https://api.peterportal.org/rest/v0/courses/all") #connects to PetrPortalAPI
# courses_data = courses.json()

# all_departments_info = {}
# for course in courses_data:
#     course_dict = dict(course)
#     number = course_dict["number"]
#     department_name = course_dict["department"]
#     terms = course_dict["terms"]
#     if department_name in all_departments_info.keys():
#         all_departments_info[department_name].append(number)
#     else:
#         all_departments_info[department_name] = [(number,terms)]
