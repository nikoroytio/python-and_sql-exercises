CREATE TABLE IF NOT EXISTS yhteystiedot(
    sposti varchar(255) PRIMARY KEY NOT NULL,
    etunimi varchar(255) NOT NULL,
    sukunimi varchar(255) NOT NULL,
    syntymapaiva INTEGER NOT NULL 
);

-- timestamp can be repsented as integer


INSERT INTO yhteystiedot (sposti, etunimi, sukunimi, syntymapaiva) VALUES (?, ?, ?, ?); 