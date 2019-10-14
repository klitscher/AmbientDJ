"""Module to create a database"""

import adj
import os
import sqlite3


def createDb(path=os.path.join(adj.path, 'AmbientDJ_DB.db')):
    """Function to create a databases with required tables
    path: Optional argument to already created database
    """

    connection = sqlite3.connect(path)

    """ Forcing foreign key constraints """
    connection.execute('PRAGMA foreign_keys = ON')

    music_sql = """CREATE TABLE IF NOT EXISTS music (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        album TEXT NOT NULL,
        trackNumber TEXT NOT NULL,
        pathToFile TEXT NOT NULL
        )
        """
    mood_sql = """CREATE TABLE IF NOT EXISTS moods (
        mood TEXT PRIMARY KEY
        )
        """
    association_sql = """CREATE TABLE IF NOT EXISTS moodIndex (
        mood TEXT,
        music_id INTEGER,
        PRIMARY KEY (mood, music_id)
        FOREIGN KEY(mood) REFERENCES moods ON DELETE CASCADE,
        FOREIGN KEY(music_id) REFERENCES
            music(id) ON DELETE CASCADE
        )
        """
    connection.execute(music_sql)
    connection.execute(mood_sql)
    connection.execute(association_sql)

    connection.commit()
    connection.close()

def insertMusicRow(title, album, trackNumber,
                   pathToMusic,
                   pathToDb=os.path.join(adj.path, 'AmbientDJ_DB.db')):
    """Method to insert a row into the music table
    title: title of the song
    album: album song is on
    trackNumber: track number of the song
    pathToMusic: path to the song in the user's music library
    pathToDb: path to the sqlite database
    """
    connection = sqlite3.connect(pathToDb)

    row_sql = """INSERT INTO moods (title, album, trackNumber, pathToFile)
        VALUES(title, album, trackNumber, pathToMusic)
        """
    connection.execute(row_sql)
    connection.commit()
    connection.close()
    