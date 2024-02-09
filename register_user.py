import sqlite3
import hashlib

def register_user(username, password):
    conn = sqlite3.connect('user_auth.db')
    cursor = conn.cursor()

    # Hash the password before storing it
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    username = input("Enter username: ")
    password = input("Enter password: ")

    register_user(username, password)
    print("User registered successfully!")
