CREATE TABLE artists(
    id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    followers int
);

CREATE TABLE albums(
    id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    tracks int,
    artist VARCHAR(255) NOT NULL,
    FOREIGN KEY (artist) REFERENCES artists(name)
);

CREATE TABLE products(
    name VARCHAR(255) NOT NULL,
    price_per_kilo FLOAT,
);

CREATE TABLE receipts(
    id INTEGER PRIMARY KEY,L,
    receipt DATE,
    salesperson name VARCHAR(255) NOT NULL
);

CREATE TABLE receipts_products(
    id INTEGER,
    FOREIGN KEY (id) REFERENCES receipts(id),
    product_id VARCHAR(255) NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(name),
    amount INTEGER,
    FOREIGN KEY (amount) REFERENCES COUNT products(name)
);

INSERT INTO artists VALUES(1, 'Emmet', 95984);
INSERT INTO artists VALUES(2, 'Beryl', 81046);
INSERT INTO artists VALUES(3, 'Alpha', 67741);
INSERT INTO artists VALUES(4, 'Lorri', 9038);
INSERT INTO artists VALUES(5, 'Rosabel', 36326);
INSERT INTO artists VALUES(6, 'Jaslene', 73053);
INSERT INTO artists VALUES(7, 'Kerry', 48168);



INSERT INTO albums VALUES(1, "painkiller", 15, "Emmet");
INSERT INTO albums VALUES(2, "motorhead", 12, 'Beryl');
INSERT INTO albums VALUES(3, "sleepy", 13, 'Alpha');
INSERT INTO albums VALUES(4, "killer", 17, 'Lorri' );
INSERT INTO albums VALUES(5, "turbolover", 18, 'Rosabel');
INSERT INTO albums VALUES(6, "bloodhound", 9, 'Jaslene');
INSERT INTO albums VALUES(7, "farty", 7, 'Kerry');

INSERT INTO albums VALUES(8, "rokkia", 14, "Emmet");
INSERT INTO albums VALUES(9, "master", 13, 'Beryl');
INSERT INTO albums VALUES(10, "of puppets", 12, 'Alpha');
INSERT INTO albums VALUES(11, "sandman", 1181, 'Lorri' );
INSERT INTO albums VALUES(12, "get rekt", 117, 'Rosabel');
INSERT INTO albums VALUES(13, "eminem show", 8, 'Jaslene');
INSERT INTO albums VALUES(14, "darty", 9, 'Kerry');