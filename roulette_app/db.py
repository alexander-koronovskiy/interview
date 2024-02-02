import sqlite3
from sqlite3 import OperationalError

def connect_sql():
    return sqlite3.connect("example.db")

def select_user_info(con, user_id):
    sql = f"SELECT round FROM routes WHERE user_id = '{user_id}'"
    res = con.cursor().execute(sql)
    return res.fetchall()

def add_info(conn, user_id, r:int, route:int, log:int):     
    cur = conn.cursor()     
    sql = f"INSERT INTO routes (user_id, round, route, log) VALUES ('{user_id}', '{r}', '{route}', '{log}')"
    cur.execute(sql)
    conn.commit()

def clear_routes_table(conn):
    cur = conn.cursor()
    cur.execute("DELETE FROM routes")
    conn.commit()

def count_by_user(conn, user_id):
    res = conn.cursor().execute("SELECT COUNT(*) FROM routes WHERE user_id = ?", (user_id,))
    return res.fetchall()
