if not check_time_conflict(user_courses):
            print("The following course ", user_dep, user_cdnum, " has not been added due to schedule conflicts.", sep = "")
            user_courses.pop()