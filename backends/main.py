from datetime import datetime, timedelta
from UItest import *

if __name__ == "__main__":
    print(get_all_courses().keys())
    all_courses = add_courses()

    print(all_courses)
    print(find_next_class(all_courses))
