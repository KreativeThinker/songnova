## [Backend](./songnova_backend):

- ### [search.py](./songnova_backend/search.py):
	- Add more search methods
	- Add option to fetch more results for the same query
	- Add field `state: str = "idle" # ["playing", "paused"]` to search results
	- Add search method for local database with priority 0
	- Add documentation
	- Add usage examples

- ### [mediaplayer.py](./songnova_backend/mediaplayer.py):
	- Add better documentation
	- Add method `loop`
	- Add method `prev`
	
- ### [playlists.py](./songnova_backend/playlists.py)
	- Create methods `view_playlist`, `view_all`, `delete_playlist` and `edit_playlist`
	- Create default tables `liked music`, `playlists` and `downloaded music`
	- Create search function for the database with priority of results as 0
	- Add following code to view_playlist
```sqlite
INSERT INTO {playlist_id} VALUES (
{data["album"]["id"]},
{data["album"]["name"]},
{data["artists"][0]["id"]},
{data["artists"][0]["name"]},
{data["duration"]},
{data["thumbnails"][1]["url"]},
{data["title"]},
{data["videoID"]},
{data["year"]}
)
```
---

## [Frontend](./songnova_frontend):

- ### [main.py](./songnova_frontend/main.py):
	- Create the file
	- Add basic functionality for alpha-testing
	- Add Documentation

- ### [main.kv](./songnova_frontend/main.kv):
	- Create the file
	- Create basic layout
	- Keep minimal design

- ### [widgets](./songnova_frontend/widgets):
	- Create custom widgets
	- Keep widgets seperated with each widget having separete folders when required