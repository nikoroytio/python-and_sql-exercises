CREATE TABLE Sensors(
id INTEGER AUTOINCREMENT,
type VARCHAR(255) NOT NULL,
location VARCHAR(255) NOT NULL,
);

CREATE TABLE Measurements (
timestamp INTEGER NOT NULL,
value INT NOT NULL,
sID FOREIGN KEY (id) REFERENCES sensors (id),
);


INSERT INTO Sensors (id, type, location)
VALUES("", "temp", "Huippuvuoret");

INSERT INTO Measurements (timestamp, value, sID)
VALUES(1644475948620, 15, 1);