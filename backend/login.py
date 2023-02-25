import database_connect

def LoginStatus(user_data: dict) -> dict:
    try:
        first_login = database_connect.FirstLogin(user_data["email"], user_data["password"])
        if not first_login and database_connect.CorrectLoginInfo(user_data["email"], user_data["password"]):
            return {"status": "correct login"}
        elif first_login:
            return {"status": "new login"} 
        else:
            return {"status": "incorrect login"}
    except:
        return {"status": "error"}
    

def CreateUser(user_data: dict) -> bool:
    try:
        database_connect.Adduser(user_data["email"])
        return True
    except:
        return False
    

def AddAllClasses(email: str, classes: list[int]) -> None:
    for class_num, class_code in enumerate(classes):
        database_connect.AddClass(email, class_num, class_code)