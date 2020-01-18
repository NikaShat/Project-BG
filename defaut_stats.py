import sqlite3


def defaultstats():
    con = sqlite3.connect("data\database.db")
    cur = con.cursor()

    cur.execute("""UPDATE classes 
                   SET level = 0 
                   WHERE null = NULL """).fetchall()
    cur.execute("""UPDATE classes 
                   SET health = 10 
                   WHERE null = NULL """).fetchall()
    cur.execute("""UPDATE classes 
                   SET strength = 3 
                   WHERE name IN (wizard, necromancer)""").fetchall()
    cur.execute("""UPDATE classes 
                   SET strength = 6 
                   WHERE name = archer""").fetchall()
    cur.execute("""UPDATE classes 
                   SET strength = 5
                   WHERE name = crusader""").fetchall()
    cur.execute("""UPDATE classes 
                   SET strength = 7
                   WHERE name = barbarian""").fetchall()
    cur.execute("""UPDATE classes 
                   SET intelligence = 7
                   WHERE name IN (wizard, necromancer)""").fetchall()
    cur.execute("""UPDATE classes 
                   SET intelligence = 3
                   WHERE name = barbarian""").fetchall()
    cur.execute("""UPDATE classes 
                   SET intelligence = 4
                   WHERE name = archer""").fetchall()
    cur.execute("""UPDATE classes 
                   SET intelligence = 5
                   WHERE name = crusader""").fetchall()
    cur.execute("""UPDATE classes 
                   SET defence = 5
                   WHERE name IN (barbarian, necromancer)""").fetchall()
    cur.execute("""UPDATE classes 
                   SET defence = 3
                   WHERE name = archer""").fetchall()
    cur.execute("""UPDATE classes 
                   SET defence = 4
                   WHERE classes = wizard""").fetchall()
    cur.execute("""UPDATE classes 
                   SET intelligence = 7
                   WHERE classes = crusader""").fetchall()
    cur.execute("""UPDATE classes 
                   SET speed = 5
                   WHERE classes IN (barbarian, necromancer)""").fetchall()
    cur.execute("""UPDATE classes 
                   SET speed = 3
                   WHERE classes = crusader""").fetchall()
    cur.execute("""UPDATE classes 
                   SET speed = 6
                   WHERE classes = wizard""").fetchall()
    cur.execute("""UPDATE classes 
                   SET speed = 7
                   WHERE classes = archer""").fetchall()
