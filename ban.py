from config import cursor, conn
from concert import Concert

class Band:
    def __init__(self, id, name, hometown):
        self.id = id
        self.name = name
        self.hometown = hometown

    @staticmethod
    def concerts(band_id):
        cursor.execute('''
        SELECT * FROM concerts WHERE band_id = ?
        ''', (band_id,))
        return cursor.fetchall()

    @staticmethod
    def venues(band_id):
        cursor.execute('''
        SELECT DISTINCT venues.* FROM venues
        JOIN concerts ON concerts.venue_id = venues.id
        WHERE concerts.band_id = ?
        ''', (band_id,))
        return cursor.fetchall()
    
    @staticmethod
    def play_in_venue(band_id, venue_id, date):
        cursor.execute('''
        INSERT INTO concerts (band_id, venue_id, date)
        VALUES (?, ?, ?)
        ''', (band_id, venue_id, date))
        conn.commit()

    @staticmethod
    def all_introductions(band_id):
        cursor.execute('''
        SELECT concerts.id FROM concerts WHERE band_id = ?
        ''', (band_id,))
        concerts = cursor.fetchall()
        introductions = []
        for concert in concerts:
            introductions.append(Concert.introduction(concert[0]))
        return introductions

    @staticmethod
    def most_performances():
        cursor.execute('''
        SELECT bands.*, COUNT(concerts.id) AS concert_count FROM bands
        JOIN concerts ON concerts.band_id = bands.id
        GROUP BY bands.id
        ORDER BY concert_count DESC LIMIT 1
        ''')
        return cursor.fetchone()

