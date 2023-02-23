import mysql.connector

def AddUser(email: str, password: str, classes: dict) -> None:
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
    # TODO: add classes 


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
    connection.close()
    return True


def CorrectLoginInfo(email: str, password: str) -> bool:
    users = mysql.connector.connect(
        host="localhost",
        user="root",
        password="S3RJGY8jfRbow02D%i6U",
        database="zot_alarm",
    )

    connection = users.cursor()
    connection.execute("SELECT id FROM users WHERE email = %s AND password = %s", (email, password))
    if connection.fetchone():
        return True
    return False


if __name__ == "__main__":
    print(FirstLogin("test_user1@uci.edu", "password")) # Should be False
    print(CorrectLoginInfo("test_user1@uci.edu", "password")) # Should be True
    print(CorrectLoginInfo("test_user2@uci.edu", "1238579287")) # Should be False
