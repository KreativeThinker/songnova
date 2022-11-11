"""
Playlist management system
"""
import sqlite3  # type: ignore
from pprint import pprint

database = sqlite3.connect("storage/playlists.db")
cursor = database.cursor()
s = "CREATE TABLE IF NOT EXISTS playlists(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(255) NOT NULL)"
cursor.execute(s)


def create_playlist(playlist: str) -> None:
    """
    Adds a playlist to the database
    """
    cursor.execute("INSERT INTO playlists (name) values ('%s')" % playlist)
    database.commit()


def view_playlists() -> list:
    """
    Returns a list of playlists
    """
    r = cursor.execute("SELECT * FROM playlists")
    return r.fetchall()


def delete_playlist(playlist_id: int) -> None:
    """
    Deletes a playlist from the database
    """
    cursor.execute("DELETE FROM playlists WHERE id = '%d'" % playlist_id)
    database.commit()


while True:
    i = input("(a) add playlist, (b) view playlists, (c) delete playlist: ")
    if i in 'aA':
        k = input("playlist name: ")
        create_playlist(k)

    elif i in 'bB':
        pprint(view_playlists())

    elif i in "cC":
        k = int(input("playlist id: "))
        delete_playlist(k)

    else:
        break
