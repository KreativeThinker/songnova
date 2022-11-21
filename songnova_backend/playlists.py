"""
Playlist management system
"""
import sqlite3  # type: ignore
from pprint import pprint
from sqlite3 import Cursor
from search import Search
database = sqlite3.connect("songnova_backend/storage/playlists.db")
cursor = database.cursor()
s: str = "CREATE TABLE IF NOT EXISTS playlists(id VARCHAR(255) PRIMARY KEY," \
         "name VARCHAR(255) NOT NULL, unique (name))"
cursor.execute(s)


def create_playlist(playlist: str) -> str:
    """
    Adds a playlist to the database
    """
    playlist_id = playlist.replace(" ", "_")
    try:
        cursor.execute(f"INSERT INTO playlists (id, name) values ('{playlist_id}', '{playlist}')")
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {playlist_id} ("
                       "album_id CHAR(17), album_name VARCHAR(50),"
                       "artist_id CHAR(17), artist_name VARCHAR(50),"
                       "duration VARCHAR(4), thumbnail VARCHAR(255),"
                       "title VARCHAR(100), videoID CHAR(11),"
                       "year CHAR(4)"
                       ")")
        database.commit()
        return "Playlist creation successful"

    except sqlite3.IntegrityError:
        return "Playlist already exists."


def view_playlists() -> list:
    """
    Returns a list of playlists
    """
    playlists: Cursor = cursor.execute("SELECT * FROM playlists")
    return playlists.fetchall()


def delete_playlist(playlist_id: str) -> None:
    """
    Deletes a playlist from the database
    """
    playlist_id = playlist_id.replace(" ", "_")
    cursor.execute(f"DELETE FROM playlists WHERE id = '{playlist_id}'")
    database.commit()


def view_playlist(playlist_id: str) -> list:
    """
    View the playlist content
    """
    playlist_id = playlist_id.replace(" ", "_")
    res: Cursor = cursor.execute(f"SELECT * FROM {playlist_id}")
    return res.fetchall()


def add_to_playlist(playlist_id: str, data: dict):
    """
    Adds a song to the specified playlist
    """
    playlist_id = playlist_id.replace(" ", "_")
    album_id, album_name = data["album"]["id"], data["album"]["name"]
    artist_id, artist_name = data["artists"][0]["id"], data["artists"][0]["name"]
    duration = data["duration"]
    thumbnail = data["thumbnails"][0]["url"]
    title = data["title"]
    video_id = data["videoId"]
    year = data["year"]
    cursor.execute(f"""INSERT INTO {playlist_id} VALUES (
    '{album_id}',
    '{album_name}',
    '{artist_id}',
    '{artist_name}',
    '{duration}',
    '{thumbnail}',
    '{title}',
    '{video_id}',
    '{year}')""")
    database.commit()


e = Search()
r = e.search_songs("the lonely")[0]


while True:
    i = input("""
    (a) add playlist
    (b) view playlists
    (c) delete playlist
    (d) view playlist
    (e) Write 'r' to playlist: """)
    if i in 'aA':
        k: str = input("playlist name: ")
        print(create_playlist(k))

    elif i in 'bB':
        pprint(view_playlists())

    elif i in "cC":
        w: str = input("playlist id: ")
        delete_playlist(w)

    elif i in "dD":
        w = input("playlist id: ")
        pprint(view_playlist(w))

    elif i in "eE":
        w = input("playlist id: ")
        add_to_playlist(w, r)

    else:
        break
