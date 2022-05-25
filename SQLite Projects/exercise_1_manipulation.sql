CREATE TABLE celebs(
    id INTEGER PRIMARY KEY NOT NULL,
    acc_name TEXT,
    age INTEGER
);
INSERT INTO celebs(id, acc_name, age) VALUES
(1, 'Justin Bieber', 22), 
(2, 'Beyonce Knowles', 33),
(3, 'Jeremy Lin', 26),
(4, 'Taylor Swift', 26);

ALTER TABLE celebs ADD COLUMN twitter_handle TEXT;

UPDATE celebs SET twitter_handle = '@jLin' WHERE id = 3;

DELETE FROM celebs where id = 1;

