
CREATE TABLE IF NOT EXISTS studios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    founded_year INTEGER
);

CREATE TABLE IF NOT EXISTS creators (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    birth_year INTEGER
);

CREATE TABLE IF NOT EXISTS manga (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    creator_id INTEGER,
    chapters INTEGER,
    status TEXT CHECK(status IN ('Ongoing', 'Completed', 'Hiatus')),
    FOREIGN KEY (creator_id) REFERENCES creators (id)
);
CREATE TABLE IF NOT EXISTS anime (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    studio_id INTEGER 
    
);
CREATE TABLE IF NOT EXISTS year_the_anime_was_created (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	year text NOT NULL

);