import sqlite3 as sql

conn = sql.connect("teszt.db")
cur = conn.cursor()
cur.execute("""BAZI NAGY SQL STATEMENT""")
