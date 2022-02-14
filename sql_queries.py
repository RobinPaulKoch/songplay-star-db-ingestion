# DROP TABLES

songplay_table_drop = """ DROP TABLE IF EXISTS songplays """
user_table_drop = " DROP TABLE IF EXISTS users "
song_table_drop = " DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE songplays (songplay_id int, start_time date, user_id VARCHAR(50), level varchar(200), song_id VARCHAR(50), artist_id VARCHAR(50), session_id VARCHAR(50), location varchar(200), user_agent varchar(200))
""")

user_table_create = ("""
CREATE TABLE users (user_id VARCHAR(50), first_name VARCHAR(100), last_name VARCHAR(100), gender VARCHAR(10), level VARCHAR(200))
""")

song_table_create = ("""
CREATE TABLE songs (song_id VARCHAR(50), title VARCHAR(100), artist_id VARCHAR(50), year int, duration NUMERIC(10,5))
""")

artist_table_create = ("""
CREATE TABLE artists (artist_id VARCHAR(50), name VARCHAR(100), location VARCHAR(100), latitude NUMERIC(8,2), longitude NUMERIC(8,2))
""")

time_table_create = ("""
CREATE TABLE time (start_time timestamp, hour int, day int, week int, month int, year int, weekday int)
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
INSERT INTO users (user_id, first_name, last_name, gender, level)
VALUES (%s, %s, %s, %s, %s)
""")

song_table_insert = ("""
INSERT INTO songs (song_id, title, artist_id, year, duration)
VALUES (%s, %s, %s, %s, %s)
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, latitude, longitude)
VALUES (%s, %s, %s, %s, %s)
""")

time_table_insert = ("""
INSERT INTO time (start_time, hour, day, week, month, year, weekday)
VALUES (%s, %s, %s, %s, %s, %s, %s)
""")

# FIND SONGS
song_select = ("""
SELECT
    a.artist_id,
    s.song_id
FROM
    artists as a
INNER JOIN
    songs as s
ON
    a.artist_id = s.artist_id
WHERE
    s.title = %s
AND
    a.name = %s
AND
    s.duration = %s
""")

# CLOSE EXISTING CONNECTIONS
close_connections = """
SELECT
    pg_terminate_backend(pid)
FROM
    pg_stat_activity
WHERE
    pid <> pg_backend_pid()
    AND datname='sparkifydb';
"""

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
