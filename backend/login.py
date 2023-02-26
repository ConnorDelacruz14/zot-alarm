import database_connect

def LoginStatus(user_data: dict) -> dict:
    try:
        first_login = database_connect.FirstLogin(user_data["email"], user_data["password"])
        if not first_login and database_connect.CorrectLoginInfo(user_data["email"], user_data["password"]):
            return {"status": "correct_login"}
        elif first_login:
            return {"status": "new_account"} 
        else:
            return {"status": "incorrect_login"}
    except:
        return {"status": "error"}
    

def CreateUser(user_data: dict) -> bool:
    try:
        database_connect.Adduser(user_data["email"])
        return True
    except:
        return False
    

def AddAllClasses(email: str, classes: list[dict]) -> None:
    for class_num, class_ in enumerate(classes):
        database_connect.AddClass(email, class_num + 1, class_["courseCode"]) 


def LoadClasses(user_data) -> dict:
    info_tuple = database_connect.GetClassInfo(user_data["email"], user_data["password"])
    return {"attendance_rate": info_tuple[5], "tardy_rate": info_tuple[7], "classes_attended": info_tuple[3], "total_classes": info_tuple[4], "late_classes": info_tuple[6], "class_1": info_tuple[8], "class_2": info_tuple[9], "class_3": info_tuple[10], "class_4": info_tuple[11], "class_5": info_tuple[12]} | {"global": LoadGlobal()}


def LoadGlobal() -> list:
    info_tuple = database_connect.GetGlobalInfo()
    return [code[0] for code in info_tuple]