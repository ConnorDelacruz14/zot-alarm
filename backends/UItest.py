from apirequests import *

current_term = 2023
current_quarter = "Winter"

user_dep = input("What is your department: ").upper()
print(get_all_courses()[user_dep])

user_cdnum = input("What is your course number: ")
all_sections = get_sections(current_term, current_quarter, user_dep, user_cdnum)
for section in all_sections:
    print(section['sectionCode'], end=" ")
print()

meeting_info = get_meeting_info(all_sections, user_section)
user_section = int(input("What is your section code: "))
if len(meeting_info[0]) > 1:    
    print("Your instructors are ", end = "")
else:
    print("Your instructor is ", end = "")
for instructor in meeting_info[0]:
    print(instructor, end = "")
print(".")

print("Schedule:", meeting_info[1])

print("Final's Date:", meeting_info[2])