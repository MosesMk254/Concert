from config import cursor
class Venue:
    def __init__(self, id, title, city):
        self.id = id
        self.title = title
        self.city = city

    @staticmethod
    def concerts(venue_id):
        cursor.execute('''
        SELECT * FROM concerts WHERE venue_id = ?
        ''', (venue_id,))
        return cursor.fetchall()

    @staticmethod
    def bands(venue_id):
        cursor.execute('''
        SELECT DISTINCT bands.* FROM bands
        JOIN concerts ON concerts.band_id = bands.id
        WHERE concerts.venue_id = ?
        ''', (venue_id,))
        return cursor.fetchall()
    
    @staticmethod
    def concert_on(venue_id, date):
        cursor.execute('''
        SELECT * FROM concerts
        WHERE venue_id = ? AND date = ?
        ''', (venue_id, date))
        return cursor.fetchone()

    @staticmethod
    def most_frequent_band(venue_id):
        cursor.execute('''
        SELECT bands.*, COUNT(concerts.id) AS concert_count FROM bands
        JOIN concerts ON concerts.band_id = bands.id
        WHERE concerts.venue_id = ?
        GROUP BY bands.id
        ORDER BY concert_count DESC LIMIT 1
        ''', (venue_id,))
        return cursor.fetchone()

