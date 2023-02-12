from datetime import datetime, timedelta
from UItest import *
from flask_connect import *

#Ali's newest

if __name__ == "__main__":
    # print(get_all_courses().keys())
    # all_courses = add_courses()

    # print(all_courses)

    user_courses = []
    # ICS 45C Lec
    user_courses = add_courses(user_courses, "I&C SCI", "45C", 35630)
    # STATS 67 Dis
    user_courses = add_courses(user_courses, "STATS", "67", 37172)
    # STATS 67 Lec
    user_courses = add_courses(user_courses, "STATS", "67", 37170)
    # ICS 6D Lec
    user_courses = add_courses(user_courses, "I&C SCI", "6D", 35530)
    # ICS 6D Dis
    user_courses = add_courses(user_courses, "I&C SCI", "6D", 35531)
    print(user_courses)
    print(find_next_class(user_courses))
    app.run()