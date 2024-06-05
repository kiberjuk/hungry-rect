import sqlite3 as sq
import pygame

def reg_user(name="user", password=1, scores=0):
    if name == "": name = "user"
    if password == "": password = 0

    with sq.connect("game.db") as con:
        cur = con.cursor()

        cur.execute("""CREATE TABLE IF NOT EXISTS users (
            login TEXT NOT NULL, 
            password TEXT NOT NULL, 
            scores INTEGER 
            )""")

        cur.execute(f"SELECT login FROM users WHERE login = '{name}'")
        row = cur.fetchone()
        if row is None:
            cur.execute("INSERT INTO users VALUES (?, ?, ?)",(name, password, scores))
            con.commit()
            print("Пользователь ", name, " успешно зарегестрирован!")
            return True
        else:
            cur.execute(f"SELECT password FROM users WHERE login = '{name}'")
            row = cur.fetchone()
            if row[0] == password:
                print("Пароль принят!")
                return True
            # else:
            #     print("Неверный пароль!")
            #     return False

def read_scores(name):

    with sq.connect("game.db") as con:
        cur = con.cursor()
        cur.execute(f"SELECT login FROM users WHERE login = '{name}'")
        if not cur.fetchone() is None:
            cur.execute(f"SELECT scores FROM users WHERE login = '{name}'")
            row = cur.fetchone()
            return row[0]

def edit_scores(name, scores=0):

    with sq.connect("game.db") as con:
        cur = con.cursor()
        cur.execute(f"SELECT login FROM users WHERE login = '{name}'")
        if not cur.fetchone() is None:
            cur.execute(f"UPDATE users SET scores= {scores} WHERE login = '{name}'")

def get_best():

    with sq.connect("game.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE scores > 0 ORDER BY scores DESC LIMIT 5")
        res = cur.fetchall()
        return res


def update_score(name, new_score):
    conn = sq.connect('game_data.db')
    c = conn.cursor()
    c.execute("UPDATE players SET score=? WHERE name=?", (new_score, name))
    conn.commit()
    conn.close()