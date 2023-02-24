import database_connect

def LoginStatus(user_data) -> dict:
    first_login = database_connect.FirstLogin(user_data["email"], user_data["password"])
    if not first_login and database_connect.CorrectLoginInfo(user_data["email"], user_data["password"]):
        return {"status": "correct login"}
    elif first_login:
        return {"status": "new login"} 
    else:
        return {"status": "incorrect login"}