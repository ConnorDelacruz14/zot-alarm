
from apirequests import *
from datetime import datetime, timedelta
import math


def check_conflict(schedule: list) -> bool:
    # Check if there is any conflicting courses within the provided schedule. Returns a bool
    for i in range(len(schedule) - 1):
        for j in range(i + 1, len(schedule)):
            course1 = schedule[i]
            course2 = schedule[j]
            if len(course1['days']) > len(course2['days']):
                if course2['days'] in course1['days']:
                    start1, end1 = course1['time'].split("-")
                    start2, end2 = course2['time'].split("-")
                    start1 = int(start1.strip().split(":")[0])
                    end1 = int(end1.strip().split(":")[0])
                    start2 = int(start2.strip().split(":")[0])
                    end2 = int(end2.strip().split(":")[0])


                    if end1 - start1 > 1:
                        end1 += 12
                    if end2 - start2 > 1:
                        end2 += 12
#hellotest2
                    if start1 < end2 and end1 > start2:
                        return True
            else:
                if course1['days'] in course2['days']:
                    start1, end1 = course1['time'].split("-")
                    start2, end2 = course2['time'].split("-")
                    start1 = int(start1.strip().split(":")[0])
                    end1 = int(end1.strip().split(":")[0])
                    start2 = int(start2.strip().split(":")[0])
                    end2 = int(end2.strip().split(":")[0])


                    if end1 - start1 > 1:
                        end1 += 12
                    if end2 - start2 > 1:
                        end2 += 12

                    if start1 < end2 and end1 > start2:
                        return True
    return False



# def add_courses():
#     current_term = 2023
#     current_quarter = "Winter"
    
#     user_courses = []
#     while True:
#         try:
#             user_dep = input("What is your department: ").upper()
#             print(get_all_courses()[user_dep])

#             user_cdnum = input("What is your course number: ")
#             all_sections = get_sections(current_term, current_quarter, user_dep, user_cdnum)
#             for section in all_sections:
#                 print(section['sectionCode'], end=" ")
#             print()

#             user_section = int(input("What is your section code: "))
#             meeting_info = get_meeting_info(all_sections, user_section)
#             if len(meeting_info[0]) > 1:    
#                 print("Your instructors are ", end = "")
#             else:
#                 print("Your instructor is ", end = "")
#             for instructor in meeting_info[0]:
#                 print(instructor, end = "")
#             print(".")

#             print("Schedule:", meeting_info[1])

#             print("Final's Date:", meeting_info[2], end="\n\n")

#             meeting_info[1][0]['course'] = f"{user_dep} {user_cdnum}"
#             user_courses.append(meeting_info[1][0])
#             if check_conflict(user_courses):
#                 print("The following course ", user_dep, user_cdnum, " has not been added due to schedule conflicts.", sep = "")
#                 user_courses.pop()

#             isDone = input("Continue Adding (y/n): ").lower()
#             print()
#             if isDone == "n":
#                 break
#         except Exception:
#             print("Error inputs. Please try again.")

#     return user_courses

def add_courses(courses_list: list, department: str, code_number: str, section_code: int, term: int = 2023, quarter: str = "Winter") -> list:
    all_sections = get_sections(term, quarter, department, code_number)
    meeting_info = get_meeting_info(all_sections, section_code)
    
    meeting_info[1][0]['course'] = f"{department} {code_number}"
    meeting_info[1][0]['instructors'] = meeting_info[0]
    courses_list.append(meeting_info[1][0])
    if check_conflict(courses_list):
        print("The following course ", department, code_number, " has not been added due to schedule conflicts.", sep = "")
        courses_list.pop()
    return courses_list


def find_next_class(schedule: list) -> str:
    # Returns the next class to attend
    now = datetime.now()
    current_day = now.strftime("%A")
    current_time = now.strftime("%I:%M%p")


    for course in schedule:
        if course['days'].find(current_day[:2]) != -1:
            start, end = map(str.strip, course['time'].split("-"))
            start_time = datetime.strptime(start, "%I:%M%p")
            end_time = datetime.strptime(end, "%I:%M%p")
            if start_time <= now <= end_time:
                return f"You are currently in {course['course']} class in {course['bldg']} building."
            if start_time > now:
                return f"Your next class is {course['course']} in {course['bldg']} building starting at {start}."


    return "You do not have any classes today."


def missed_classes(start_time, schedule: list) -> list:
    # Returns a list of missed classes, automatically append the missed course after current time has passed class time, starting from start_time
    current_day = datetime.now().strftime("%A")
    start_time = datetime.strptime(start_time, "%I:%M%p")


    missed = []
    for course in schedule:
        if course['days'].find(current_day[:2]) != -1:
            course_start, course_end = map(str.strip, course['time'].split("-"))
            course_start_time = datetime.strptime(course_start, "%I:%M%p")
            course_end_time = datetime.strptime(course_end, "%I:%M%p")
            if start_time <= course_start_time <= datetime.now() < course_end_time:
                missed.append(course['course'])


    return missed




def check_attendance(missed_courses: list, attended_courses: list) -> list:
    # Returns a list of missed courses after removing all the attended courses
    # Only available after the first ten minutes of the class
    for acourse in attended_courses:
        missed_courses.pop(missed_courses.index(acourse))
    return missed_courses


def is_attended(schedule: list) -> bool:
    now = datetime.now()
    current_day = now.strftime("%A")
    current_time = now.strftime("%I:%M%p")


    for course in schedule:
        if course['days'].find(current_day[:2]) != -1:
            start, end = map(str.strip, course['time'].split("-"))
            start_time = datetime.strptime(start, "%I:%M%p")
            end_time = datetime.strptime(end, "%I:%M%p")
            if start_time <= now <= end_time:
                return True

    return False



def tuition_loss_amount(total_units_applied: float, missed_class_units: float, missed_minutes: int, tuition_per_quarter: float, term: int) -> int:
    # Returns tuition loss based on specified parameters
    if (term.upper() == "FALL"):
        off_days = 24
        vacation_cost = off_days/7 * 150
    elif (term.upper() == "WINTER" or term.upper() == "SPRING"):
        off_days = 7
        vacation_cost = off_days/7 * 150
    else:
        vacation_cost = 0
    
    total_cost = (tuition_per_quarter/total_units_applied)*missed_class_units - vacation_cost
    proportion = total_cost/1500
    missed_cost = missed_minutes*proportion
    return "Total Tuition Loss: $" + str(math.ceil(missed_cost))


