import sqlite3

conn = sqlite3.connect("nlp_demo.db")   # splite3 db 연결
conn.execute("CREATE TABLE IF NOT EXISTS Feedback(context TEXT, date TEXT)")   # Board 라는 DB생성
