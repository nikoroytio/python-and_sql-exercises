SELECT artists.name, artists.followers, albums.name, albums.tracks  FROM artists, albums WHERE artists.name = albums.artist ORDER BY artists.name;