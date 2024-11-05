
CREATE TABLE artist (
  id INTEGER PRIMARY KEY,
  artist_name TEXT
)

CREATE TABLE album (
  id INTEGER PRIMARY KEY,
  album_name TEXT,
  artist_id INTEGER,
)

CREATE TABLE song (
  id INTEGER PRIMARY KEY,
  song_name TEXT,
  track INTEGER,
  album_id INTEGER,
  artist_id INTEGER
  song_length INTEGER,
)