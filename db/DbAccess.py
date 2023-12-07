##SQL QUERIES AND UPDATE STATEMENTS##

import sqlite3
from contextlib import closing

from objects.Lineup import Lineup
from objects.Player import Player

conn = None

def connect():
    global conn
    if not conn:
        try:
            DB_FILE = r"db\\TeamManager.sqlite"
            conn = sqlite3.connect(DB_FILE)
            conn.row_factory = sqlite3.Row
        except:
            print("error connecting to db")

def close():
    if conn:
        conn.close()

#helpers for adding player
def make_player(row):
    return Player(row["batOrder"],
                  row["firstName"], 
                  row["lastName"],
                  row["position"],
                  row["atBats"], 
                  row["hits"]
    )

def make_lineup(results):
    lineup = Lineup()

    for row in results:
        lineup.add_player(make_player(row))
    return lineup

#get lineup
def get_lineup():
    connect()
    sql = '''SELECT *
             FROM Player
             ORDER BY batOrder ASC'''
    with closing(conn.cursor()) as c:
        c.execute(sql)
        results = c.fetchall()

    return make_lineup(results)

#add player
def add_player(player):
    connect()
    sql = '''INSERT INTO Player (batOrder, firstName, lastName, position, atBats, hits)
             VALUES(?, ?, ?, ?, ?, ?)'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (player.batOrder, player.firstName, player.lastName,
                        player.position, player.atBats, player.hits))
        conn.commit()

#delete player
def delete_player(batOrder):
    connect()
    sql = '''DELETE
             FROM Player
             WHERE batOrder = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (batOrder,))
        conn.commit()

#move player
def move_player(current_index, new_index):
    connect()

    with closing(conn.cursor()) as c:
        try:
            c.execute("SELECT batOrder FROM Player WHERE PlayerID = ?", (current_index,))
            current_bat_order = c.fetchone()[0]

            if new_index < current_bat_order:
                sql = '''
                    UPDATE Player
                    SET batOrder = batOrder + 1
                    WHERE batOrder >= ? AND batOrder < ?
                '''
                c.execute(sql, (new_index, current_bat_order))
            elif new_index > current_bat_order:
                sql = '''
                    UPDATE Player
                    SET batOrder = batOrder - 1
                    WHERE batOrder > ? AND batOrder <= ?
                '''
                c.execute(sql, (current_bat_order, new_index))

            c.execute("UPDATE Player SET batOrder = ? WHERE PlayerID = ?", (new_index, current_index))
            conn.commit()
            print("Player order updated successfully.")
        except sqlite3.Error as e:
            print("Error:", e)

#update position
def update_position(new_position, batOrder):
    connect()

    sql = '''UPDATE Player
             SET position = ?
             WHERE batOrder = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (new_position, batOrder))
        conn.commit()

#update stats
def update_stats(atBats, hits, batOrder):
    connect()

    sql = '''UPDATE Player
             SET atBats = ?,
                 hits = ?
            WHERE batOrder = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (atBats, hits, batOrder))
        conn.commit()

#FROM GUI
def update_player(player):
    connect()

    sql = '''UPDATE Player
             SET firstName = ?,
                 lastName = ?,
                 position = ?,
                 atBats = ?,
                 hits = ?
            WHERE batOrder = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (player.firstName, player.lastName, player.position, player.atBats, player.hits, player.batOrder))