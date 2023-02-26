import mysql.connector

def AddUser(email: str, password: str) -> None:
    users = mysql.connector.connect(
        host="localhost",
        user="root",
        password="S3RJGY8jfRbow02D%i6U",
        database="zot_alarm",
    )
    connection = users.cursor()
    connection.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, password))

    users.commit()
    connection.close()


def AddClass(email: str, class_num: int, class_code: int) -> None:
    users = mysql.connector.connect(
        host="localhost",
        user="root",
        password="S3RJGY8jfRbow02D%i6U",
        database="zot_alarm",
    )
    connection = users.cursor()
    connection.execute("UPDATE users SET class_%s = %s WHERE email = %s", [class_num, class_code, email])
    users.commit()
    connection.close()
    

def FirstLogin(email: str, password: str) -> bool:
    users = mysql.connector.connect(
        host="localhost",
        user="root",
        password="S3RJGY8jfRbow02D%i6U",
        database="zot_alarm",
    )
    connection = users.cursor()
    connection.execute("SELECT id FROM users WHERE email = %s", [email])

    if connection.fetchone():
        return False
    
    connection.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, password))
    users.commit()
    connection.close()
    return True


def CorrectLoginInfo(email: str, password: str) -> bool:
    if GetClassInfo(email, password):
        return True
    return False


def GetClassInfo(email: str, password: str) -> tuple:
    users = mysql.connector.connect(
        host="localhost",
        user="root",
        password="S3RJGY8jfRbow02D%i6U",
        database="zot_alarm",
    )
    connection = users.cursor()
    connection.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
    return connection.fetchone()


def GetGlobalInfo() -> tuple:
    global_ = mysql.connector.connect(
        host="localhost",
        user="root",
        password="S3RJGY8jfRbow02D%i6U",
        database="zot_alarm",
    )
    connection = global_.cursor()
    connection.execute("SELECT * FROM global LIMIT 5")
    return connection.fetchall()
    


if __name__ == "__main__":
    print(FirstLogin("test_user1@uci.edu", "password")) # Should be False
    print(CorrectLoginInfo("test_user1@uci.edu", "password")) # Should be True
    print(CorrectLoginInfo("test_user2@uci.edu", "1238579287")) # Should be False
