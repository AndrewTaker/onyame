CREATE TABLE IF NOT EXISTS manga (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    creator_id INTEGER NOT NULL,
    chapters INTEGER NOT NULL,
    status TEXT CHECK(status IN ('Ongoing', 'Completed', 'Hiatus')) NOT NULL,

    FOREIGN KEY (creator_id) REFERENCES creators (id)
);

CREATE TABLE IF NOT EXISTS anime (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    studio_id INTEGER NOT NULL,
    episodes INTEGER NOT NULL,
    status TEXT CHECK(status IN ('Ongoing', 'Completed', 'Hiatus')) NOT NULL,

    FOREIGN KEY (studio_id) REFERENCES studios (id)
);

CREATE TABLE IF NOT EXISTS studios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    founded_year INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS creators (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    birth_year INTEGER
);
