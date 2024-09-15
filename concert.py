from config import cursor
class Concert:
    def __init__(self, id, band_id, venue_id, date):
        self.id = id
        self.band_id = band_id
        self.venue_id = venue_id
        self.date = date

    @staticmethod
    def band(concert_id):
        cursor.execute('''
        SELECT bands.* FROM bands
        JOIN concerts ON concerts.band_id = bands.id
        WHERE concerts.id = ?
        ''', (concert_id,))
        return cursor.fetchone()

    @staticmethod
    def venue(concert_id):
        cursor.execute('''
        SELECT venues.* FROM venues
        JOIN concerts ON concerts.venue_id = venues.id
        WHERE concerts.id = ?
        ''', (concert_id,))
        return cursor.fetchone()
    
    @staticmethod
    def hometown_show(concert_id):
        cursor.execute('''
        SELECT concerts.id FROM concerts
        JOIN bands ON bands.id = concerts.band_id
        JOIN venues ON venues.id = concerts.venue_id
        WHERE concerts.id = ? AND bands.hometown = venues.city
        ''', (concert_id,))
        return cursor.fetchone() is not None

    @staticmethod
    def introduction(concert_id):
        cursor.execute('''
        SELECT bands.name, bands.hometown, venues.city FROM concerts
        JOIN bands ON bands.id = concerts.band_id
        JOIN venues ON venues.id = concerts.venue_id
        WHERE concerts.id = ?
        ''', (concert_id,))
        result = cursor.fetchone()
        return f"Hello {result[2]}!!!!! We are {result[0]} and we're from {result[1]}"
    