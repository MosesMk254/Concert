import sqlite3

# Create database connection
conn = sqlite3.connect('concerts.db')
cursor = conn.cursor()

# Create bands table
cursor.execute('''
CREATE TABLE IF NOT EXISTS bands (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    hometown TEXT
)
''')

# Create venues table
cursor.execute('''
CREATE TABLE IF NOT EXISTS venues (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    city TEXT
)
''')

# Create concerts table with foreign keys to bands and venues
cursor.execute('''
CREATE TABLE IF NOT EXISTS concerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    band_id INTEGER,
    venue_id INTEGER,
    date TEXT,
    FOREIGN KEY (band_id) REFERENCES bands (id),
    FOREIGN KEY (venue_id) REFERENCES venues (id)
)
''')

conn.commit()
