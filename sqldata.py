from sqlite3 import Connection

conn = Connection("data.db")
c = conn.cursor()

def default():
    c.execute("CREATE TABLE IF NOT EXISTS users (user_id, job)")
    c.execute("CREATE TABLE IF NOT EXISTS pupils (user_id, ism, familya, phone, viloyat, tuman, maktab, sinf)")
    c.execute("CREATE TABLE IF NOT EXISTS teachers (user_id, ism, familya, phone, viloyat, tuman, maktab, pupil_info)")
    conn.commit()

def add_user(user_id, job):
    c.execute("INSERT INTO users VALUES (?, ?)", (user_id, job))
    conn.commit()

def add_pupil(user_id, ism, familya, phone, viloyat, tuman, maktab, sinf):
    c.execute("INSERT INTO pupils VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (user_id, ism, familya, phone, viloyat, tuman, maktab, sinf))
    conn.commit()

def add_teacher(user_id, ism, familya, phone, viloyat, tuman, maktab, pupil_info):
    c.execute("INSERT INTO teachers VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (user_id, ism, familya, phone, viloyat, tuman, maktab, pupil_info))
    conn.commit()

def get_users():
    return c.execute("SEELCT * FROM users").fetchall()

def get_pupils():
    return c.execute("SELECT * FROM pupils").fetchall()

def get_teachers():
    return c.execute("SELECT * FROM teachers").fetchall()

def get_user(user_id):
    return c.execute("SELECT * FROM users WHERE  user_id=?", (user_id, )).fetchall()

def get_pupil(user_id):
    return c.execute("SELECT * FROM pupils WHERE  user_id=?", (user_id, )).fetchall()

def get_teacher(user_id):
    return c.execute("SELECT * FROM teachers WHERE  user_id=?", (user_id, )).fetchall()

def del_user(user_id):
    c.execute("DELETE FROM users WHERE user_id=?", (user_id, ))
    conn.commit()

def close_db():
    conn.close()