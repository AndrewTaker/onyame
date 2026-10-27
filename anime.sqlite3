-- Enable foreign key support in SQLite
PRAGMA foreign_keys = ON;

-- ==========================================
-- SCHEMA DEFINITION
-- ==========================================

CREATE TABLE studios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    founded_year INTEGER
);

CREATE TABLE creators (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    birth_year INTEGER
);

CREATE TABLE manga (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    creator_id INTEGER,
    chapters INTEGER,
    status TEXT CHECK(status IN ('Ongoing', 'Completed', 'Hiatus')),
    FOREIGN KEY (creator_id) REFERENCES creators (id)
);

-- Anime table connects to both Studios and Manga (as source material)
CREATE TABLE anime (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    studio_id INTEGER,
    source_manga_id INTEGER, -- Can be NULL if it's an original anime
    episodes INTEGER,
    score REAL,
    FOREIGN KEY (studio_id) REFERENCES studios (id),
    FOREIGN KEY (source_manga_id) REFERENCES manga (id)
);

-- ==========================================
-- SEED DATA
-- ==========================================

-- Insert Studios
INSERT INTO studios (name, founded_year) VALUES 
('Madhouse', 1972),
('Bones', 1998),
('MAPPA', 2011),
('Ufotable', 2000),
('Trigger', 2011);

-- Insert Creators
INSERT INTO creators (name, birth_year) VALUES 
('Hajime Isayama', 1986),
('ONE', 1986),
('Koyoharu Gotouge', 1989),
('Kentaro Miura', 1966),
('Hiromu Arakawa', 1973);

-- Insert Manga
INSERT INTO manga (title, creator_id, chapters, status) VALUES 
('Attack on Titan', 1, 139, 'Completed'),
('One Punch Man', 2, 193, 'Ongoing'),
('Mob Psycho 100', 2, 101, 'Completed'),
('Demon Slayer', 3, 205, 'Completed'),
('Berserk', 4, 373, 'Ongoing'),
('Fullmetal Alchemist', 5, 108, 'Completed');

-- Insert Anime
INSERT INTO anime (title, studio_id, source_manga_id, episodes, score) VALUES 
('Attack on Titan: The Final Season', 3, 1, 35, 8.8),
('One Punch Man', 1, 2, 12, 8.7),
('Mob Psycho 100', 2, 3, 37, 8.5),
('Demon Slayer: Kimetsu no Yaiba', 4, 4, 26, 8.5),
('Fullmetal Alchemist: Brotherhood', 2, 6, 64, 9.1),
('Cyberpunk: Edgerunners', 5, NULL, 10, 8.6), -- Original anime, no manga source
('Death Note', 1, NULL, 37, 8.6); -- Let's pretend no manga source to demonstrate NULLs
