DROP TABLE IF EXISTS user_guesses;

CREATE TABLE user_guesses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    guessed_temp INTEGER NOT NULL,
    actual_temp INTEGER NOT NULL,
    dt INTEGER NOT NULL
);