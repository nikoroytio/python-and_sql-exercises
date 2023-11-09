CREATE TABLE IF NOT EXISTS artists(
    id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    followers int
);

CREATE TABLE IF NOT EXISTS albums(
    id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    tracks int,
    artist VARCHAR(255) NOT NULL,
    FOREIGN KEY (artist) REFERENCES artists(name)
);
