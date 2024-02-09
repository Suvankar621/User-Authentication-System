import sqlite3
import hashlib

def authenticate_user(username, password):
    conn = sqlite3.connect('user_auth.db')
    cursor = conn.cursor()

    # Hash the entered password for comparison
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, hashed_password))
    user = cursor.fetchone()

    conn.close()

    return user is not None

if __name__ == "__main__":
    username = input("Enter username: ")
    password = input("Enter password: ")

    if authenticate_user(username, password):
        print("Authentication successful!")
    else:
        print("Authentication failed. Invalid username or password.")
