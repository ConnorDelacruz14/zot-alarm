<<<<<<< HEAD
import requests

def get_all_courses():
    courses = requests.get("https://api.peterportal.org/rest/v0/courses/all") #connects to PetrPortalAPI
    courses_data = courses.json()
    all_departments_info = {}
    for course in courses_data:
        course_dict = dict(course)
        number = course_dict["number"]
        department_name = course_dict["department"]
        terms = course_dict["terms"]
        if department_name in all_departments_info.keys():
            all_departments_info[department_name].append(number)
        else:
            all_departments_info[department_name] = [number]
    return all_departments_info

def get_sections(term, quarter, department, number):
    try:
        quarter = quarter.upper()
        department = department.upper()
        if department == "CRM/LAW":
            department = "CRM%2FLAW"
        elif department == "I&C SCI":
            department = "I%26C SCI"
        schedule = requests.get(f"https://api.peterportal.org/rest/v0/schedule/soc?term={term}%20{quarter}&department={department}&courseNumber={number}")
        schedule_dict = dict(schedule.json())
        # meetings = schedule_dict['schools'][0]['departments'][0]['courses'][0]['sections'][0]['meetings'][0]
        # section_code = schedule_dict['schools'][0]['departments'][0]['courses'][0]['sections'][0]['sectionCode']
        
        return schedule_dict['schools'][0]['departments'][0]['courses'][0]['sections']
    except:
        raise Exception("Nonexistent Course")

def get_meeting_info(sections_list, section_code):
    for section in sections_list:
        if section['sectionCode'] == str(section_code):
            return (section['instructors'], section['meetings'], section['finalExam'])
=======
import requests

def get_all_courses():
    courses = requests.get("https://api.peterportal.org/rest/v0/courses/all") #connects to PetrPortalAPI
    courses_data = courses.json()
    all_departments_info = {}
    for course in courses_data:
        course_dict = dict(course)
        number = course_dict["number"]
        department_name = course_dict["department"]
        terms = course_dict["terms"]
        if department_name in all_departments_info.keys():
            all_departments_info[department_name].append(number)
        else:
            all_departments_info[department_name] = [number]
    return all_departments_info

def get_sections(term, quarter, department, number):
    try:
        quarter = quarter.upper()
        department = department.upper()
        if department == "CRM/LAW":
            department = "CRM%2FLAW"
        elif department == "I&C SCI":
            department = "I%26C SCI"
        schedule = requests.get(f"https://api.peterportal.org/rest/v0/schedule/soc?term={term}%20{quarter}&department={department}&courseNumber={number}")
        schedule_dict = dict(schedule.json())
        # meetings = schedule_dict['schools'][0]['departments'][0]['courses'][0]['sections'][0]['meetings'][0]
        # section_code = schedule_dict['schools'][0]['departments'][0]['courses'][0]['sections'][0]['sectionCode']
        
        return schedule_dict['schools'][0]['departments'][0]['courses'][0]['sections']
    except:
        raise Exception("Nonexistent Course")

def get_meeting_info(sections_list, section_code):
    for section in sections_list:
        if section['sectionCode'] == str(section_code):
            return (section['instructors'], section['meetings'], section['finalExam'])
>>>>>>> 5f9ed89ecd62975ea8b75383caecb984166557a3
