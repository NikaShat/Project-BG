import sqlite3

# сброс статов до начальных значений


def defaultstats(cur):
    cur.execute("""UPDATE classes
                   SET level = 0""").fetchall()
    cur.execute("""UPDATE classes
                   SET health = 10""").fetchall()
    cur.execute("""UPDATE classes
                   SET strength = 3
                   WHERE name IN ('wizard', 'necromancer')""").fetchall()
    cur.execute("""UPDATE classes
                   SET strength = 6
                   WHERE name = 'archer'""").fetchall()
    cur.execute("""UPDATE classes
                   SET strength = 5
                   WHERE name = 'crusader'""").fetchall()
    cur.execute("""UPDATE classes
                   SET strength = 7
                   WHERE name = 'barbarian'""").fetchall()
    cur.execute("""UPDATE classes
                   SET intelligence = 7
                   WHERE name IN ('wizard', 'necromancer')""").fetchall()
    cur.execute("""UPDATE classes
                   SET intelligence = 3
                   WHERE name = 'barbarian'""").fetchall()
    cur.execute("""UPDATE classes
                   SET intelligence = 4
                   WHERE name = 'archer'""").fetchall()
    cur.execute("""UPDATE classes
                   SET intelligence = 5
                   WHERE name = 'crusader'""").fetchall()
    cur.execute("""UPDATE classes
                   SET defence = 5
                   WHERE name IN ('barbarian', 'necromancer')""").fetchall()
    cur.execute("""UPDATE classes
                   SET defence = 3
                   WHERE name = 'archer'""").fetchall()
    cur.execute("""UPDATE classes
                   SET defence = 4
                   WHERE name = 'wizard'""").fetchall()
    cur.execute("""UPDATE classes
                   SET intelligence = 7
                   WHERE name = 'crusader'""").fetchall()
    cur.execute("""UPDATE classes
                   SET speed = 5
                   WHERE name IN ('barbarian', 'necromancer')""").fetchall()
    cur.execute("""UPDATE classes
                   SET speed = 3
                   WHERE name = 'crusader'""").fetchall()
    cur.execute("""UPDATE classes
                   SET speed = 6
                   WHERE name = 'wizard'""").fetchall()
    cur.execute("""UPDATE classes
                   SET speed = 7
                   WHERE name = 'archer'""").fetchall()
    cur.execute("""UPDATE player
                   SET money = -1
                   WHERE key = 1""").fetchall()
