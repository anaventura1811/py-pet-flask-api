CREATE TABLE IF NOT EXISTS pets (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  name TEXT NOT NULL,
  type TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS people (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTEGER NOT NULL,
  pet_id INTEGER NOT NULL,
  FOREIGN KEY (pet_id) REFERENCES pets(id)
);

INSERT INTO pets (name, type)
VALUES
      ("cobra", "snake"),
      ("cao", "dog"),
      ("bentinho", "cat"),
      ("jorgin", "hamster"),
      ("burro", "donkey"),
      ("shrek", "ogro"),
      ("belinha", "dog"),
      ("serena", "dog");
