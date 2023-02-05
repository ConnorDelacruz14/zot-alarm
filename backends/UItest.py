from apirequests import *
from datetime import datetime, timedelta

def check_conflict(schedule):
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

                    if end1 - start1 <= 2:
                        end1 += 12
                    if end2 - start2 <= 2:
                        end2 += 12

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

                    if end1 - start1 <= 2:
                        end1 += 12
                    if end2 - start2 <= 2:
                        end2 += 12

                    if start1 < end2 and end1 > start2:
                        return True
    return False


def add_courses():
    current_term = 2023
    current_quarter = "Winter"
    
    user_courses = []
    while True:
        user_dep = input("What is your department: ").upper()
        print(get_all_courses()[user_dep])

        user_cdnum = input("What is your course number: ")
        all_sections = get_sections(current_term, current_quarter, user_dep, user_cdnum)
        for section in all_sections:
            print(section['sectionCode'], end=" ")
        print()

        user_section = int(input("What is your section code: "))
        meeting_info = get_meeting_info(all_sections, user_section)
        if len(meeting_info[0]) > 1:    
            print("Your instructors are ", end = "")
        else:
            print("Your instructor is ", end = "")
        for instructor in meeting_info[0]:
            print(instructor, end = "")
        print(".")

        print("Schedule:", meeting_info[1])

        print("Final's Date:", meeting_info[2], end="\n\n")

        meeting_info[1][0]['course'] = f"{user_dep} {user_cdnum}"
        user_courses.append(meeting_info[1][0])
        if check_conflict(user_courses):
            print("The following course ", user_dep, user_cdnum, " has not been added due to schedule conflicts.", sep = "")
            user_courses.pop()

        isDone = input("Continue Adding (y/n): ")
        print()
        if isDone == "n":
            break

    return user_courses


def find_next_class(schedule):
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
