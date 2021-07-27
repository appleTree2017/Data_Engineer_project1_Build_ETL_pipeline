# # DROP TABLES
#
# songplay_table_drop = "DROP TABLE IF EXISTS songplays"
# user_table_drop = "DROP TABLE IF EXISTS users"
# song_table_drop = "DROP TABLE IF EXISTS songs"
# artist_table_drop = "DROP TABLE IF EXISTS artists"
# time_table_drop = "DROP TABLE IF EXISTS time"
#
# # CREATE TABLES
#
#
# songplay_table_create = ("""
# CREATE TABLE IF NOT EXISTS songplays
# (songplay_id SERIAL primary key ,
# start_time bigint REFERENCES time(start_time) ,
# user_id int  references users,
# level varchar,
# song_id varchar references songs,
# artist_id varchar references artist,
# session_id int,
# location varchar,
# user_agent varchar)
# """)
#
# time_table_create = ("""
# Create Table IF NOT EXISTS time
# (start_time bigint primary key not null,
# hour int,
# day int,
# week int,
# month int,
# year int,
# weekday varchar)
# """)
#
# user_table_create = ("""
# CREATE TABLE IF NOT EXISTS users
# (user_id int  PRIMARY KEY ,
# first_name varchar ,
# last_name varchar,
# gender varchar,
# level varchar)
# """)
#
# song_table_create = ("""
# CREATE TABLE IF NOT EXISTS songs
# (song_id varchar PRIMARY KEY ,
# title varchar,
# artist_id varchar,
# year int,
# duration numeric not null)
# """)
#
# artist_table_create = ("""CREATE TABLE IF NOT EXISTS artist
# (artist_id varchar PRIMARY KEY ,
# name varchar,
# location varchar,
# latitude varchar,
# longitude varchar)
# """)
#
#
# # INSERT RECORDS
#
# songplay_table_insert = ("""
# Insert into songplays
# (start_time, user_id,level,song_id,artist_id,session_id,location,user_agent)
# VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
#
# """)
#
# user_table_insert = ("""
# Insert into users (user_id, first_name,last_name,gender,level)
# VALUES(%s,%s,%s,%s,%s)
# ON CONFLICT(user_id)
# DO UPDATE SET level=EXCLUDED.level
# """)
#
# song_table_insert = ("""
# INSERT INTO songs (song_id,title,artist_id,year,duration)
# VALUES (%s, %s, %s,%s,%s)
# ON CONFLICT (song_id ) DO NOTHING
# """)
#
# artist_table_insert = ("""
# Insert into artist (artist_id, name,location,latitude,longitude)
# VALUES (%s,%s,%s,%s,%s)
# ON CONFLICT (artist_id )
# DO NOTHING
#
# """)
#
#
# time_table_insert = ("""
# Insert into time(start_time,hour, day, week, month,year,weekday)
# VALUES (%s,%s,%s,%s,%s,%s,%s)
# ON CONFLICT(start_time)
# DO NOTHING
# """)
#
# # FIND SONGS
#
# song_select = ("""
# SELECT S.song_id,A.artist_id FROM songs S
# JOIN artist A on S.artist_id=A.artist_id
# WHERE S.title=%s AND A.name=%s AND S.duration=%s
# """)
#
# alter_table = ("""
# ALTER TABLE songplays ADD FOREIGN KEY (user_id) REFERENCES users(user_id);
# ALTER TABLE songplays ADD FOREIGN KEY (song_id) REFERENCES songs(song_id);
# ALTER TABLE songplays ADD FOREIGN KEY (start_time) REFERENCES time(start_time);
# ALTER TABLE songplays ADD FOREIGN KEY (artist_id) REFERENCES artist(artist_id);
# """)
# # QUERY LISTS
# create_table_queries = [  user_table_create, song_table_create, artist_table_create,time_table_create,songplay_table_create]
# drop_table_queries =[user_table_drop, song_table_drop, artist_table_drop, time_table_drop,songplay_table_drop]


# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays 
(songplay_id serial primary key , 
start_time bigint references time(start_time) , 
user_id int  references users(user_id)ON DELETE CASCADE  
ON UPDATE CASCADE , 
level varchar,
song_id varchar references songs(song_id), 
artist_id varchar references artist(artist_id), 
session_id int, 
location varchar, 
user_agent varchar)
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users 
(user_id int NOT NULL PRIMARY KEY, 
first_name varchar , 
last_name varchar, 
gender varchar, 
level varchar)
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs 
(song_id varchar PRIMARY KEY NOT NULL, 
title varchar, 
artist_id varchar, 
year int, 
duration numeric)
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artist   
(artist_id varchar PRIMARY KEY NOT NULL, 
name varchar, 
location varchar, 
latitude varchar, 
longitude varchar)
""")

time_table_create = ("""
Create Table IF NOT EXISTS time
(start_time bigint primary key NOT NULL, 
hour int, 
day int, 
week int, 
month int, 
year int, 
weekday varchar)
""")

# INSERT RECORDS

songplay_table_insert = ("""Insert into songplays
(start_time, user_id,level,song_id,artist_id,session_id,location,user_agent) 
VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
""")

user_table_insert = ("""Insert into users 
(user_id, first_name,last_name,gender,level) 
VALUES(%s,%s,%s,%s,%s) ON CONFLICT(user_id)
DO UPDATE SET level=EXCLUDED.level
""")

song_table_insert = ("""INSERT INTO songs 
(song_id,title,artist_id,year,duration) 
VALUES (%s, %s, %s,%s,%s) 
ON CONFLICT (song_id ) 
DO NOTHING

""")

artist_table_insert = ("""
Insert into artist (artist_id, name,location,latitude,longitude)
VALUES (%s,%s,%s,%s,%s)
ON CONFLICT (artist_id ) 
DO NOTHING

""")


time_table_insert = ("""Insert into time
(start_time,hour, day, week, month,year,weekday) 
VALUES (%s,%s,%s,%s,%s,%s,%s) 
ON CONFLICT(start_time)
DO NOTHING
""")
alter_table = ("""

ALTER TABLE songplays ADD FOREIGN KEY (start_time) REFERENCES time(start_time);

 """)
# FIND SONGS

song_select = ("""
SELECT S.song_id,A.artist_id FROM songs S
JOIN artist A on S.artist_id=A.artist_id
WHERE S.title=%s AND A.name=%s AND S.duration=%s
""")

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create]
drop_table_queries = [ user_table_drop, song_table_drop, artist_table_drop, time_table_drop,songplay_table_drop,]