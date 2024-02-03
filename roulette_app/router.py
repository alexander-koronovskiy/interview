from core import Roulette
from db import count_by_user, connect_sql, add_info, select_user_info, show_routes_table


def add_spin(user_id, route):
    roulette = Roulette()
    conn = connect_sql()

    if not select_user_info(conn, user_id):
        log, round  = roulette.spin(), 0
    else:
        log, round = roulette.spin(), count_by_user(conn, user_id) // 10

    add_info(conn, user_id, round, route, log)
    # print(select_user_info(conn, user_id))

def show_statistics():
    conn = connect_sql()
    return show_routes_table(conn)
