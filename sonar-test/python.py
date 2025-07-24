import os, sqlite3

# Hardcoded credentials
username = "admin"
password = "password123"

def login(a, b):
    if a == username and b == password:
        print("Welcome!")
    else:
        print("Access denied")

def unsafe_query(uid):
    conn = sqlite3.connect("db.sqlite3")
    # SQL injection
    conn.execute(f"SELECT * FROM users WHERE id = {uid}")
    conn.close()

def inject(ip):
    # Command injection
    os.system("ping " + ip)

login("admin", "password123")
unsafe_query("1 OR 1=1")
inject("; rm -rf /")

