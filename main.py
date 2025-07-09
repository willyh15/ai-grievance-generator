import sqlite3
import datetime

def log_grievance(issue, resolution):
    conn = sqlite3.connect('grievances.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS grievances (id INTEGER PRIMARY KEY, date TEXT, issue TEXT, resolution TEXT)")
    c.execute("INSERT INTO grievances (date, issue, resolution) VALUES (?, ?, ?)",
              (datetime.datetime.now().isoformat(), issue, resolution))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    log_grievance("Sample grievance", "Filed to local center rep")
