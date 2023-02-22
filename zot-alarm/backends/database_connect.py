import mysql.connector

def CheckFirstLogin(email: str, password: str) -> bool:
    users = mysql.connector.connect(
        host="localhost",
        user="root",
        password="S3RJGY8jfRbow02D%i6U",
        database="zot_alarm",
    )
    info = (email, password)
    connection = users.cursor()
    connection.execute("SELECT id FROM users WHERE email = %s AND password = %s", info) 
    if connection.fetchall():
        return False
    return True


if __name__ == "__main__":
    CheckFirstLogin("connorjd@uci.edu", "password")