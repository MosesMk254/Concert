from config import cursor,conn
from concert import Concert
from venue import Venue
from ban import Band

# Insert test data
def seed_data():
    cursor.execute("INSERT INTO bands (name, hometown) VALUES ('Band A', 'City A')")
    cursor.execute("INSERT INTO bands (name, hometown) VALUES ('Band B', 'City B')")
    cursor.execute("INSERT INTO venues (title, city) VALUES ('Venue 1', 'City A')")
    cursor.execute("INSERT INTO venues (title, city) VALUES ('Venue 2', 'City B')")
    cursor.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (1, 1, '2023-09-01')")
    cursor.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (2, 2, '2023-09-02')")
    conn.commit()

seed_data()

# Testing the methods

# Testing Concert.band()
print("Concert 1 Band: ", Concert.band(1)) # Should return Band A

# Testing Concert.venue()
print("Concert 1 Venue: ", Concert.venue(1)) # Should return Venue 1

# Testing Concert.hometown_show()
print("Is Concert 1 a hometown show?: ", Concert.hometown_show(1)) # Should return True

# Testing Concert.introduction()
print("Concert 1 Introduction: ", Concert.introduction(1)) # Should return introduction string

# Testing Band.play_in_venue()
Band.play_in_venue(1, 2, '2024-09-15') # Band A plays in Venue 2
print("Concerts by Band 1: ", Band.concerts(1)) # Should show the new concert

# Testing Band.all_introductions()
print("Band 1 Introductions: ", Band.all_introductions(1)) # Should show all introductions for Band A

# Testing Venue.most_frequent_band()
print("Most frequent band at Venue 1: ", Venue.most_frequent_band(1)) # Should return Band A

# Testing Band.most_performances()
print("Band with most performances: ", Band.most_performances()) # Should return Band with most concerts

conn.close()  # Close the connection
