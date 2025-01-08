INSERT OR IGNORE INTO users (name, email, phone) VALUES ('Alice', 'alice@example.com', '123-456-7890');
INSERT OR IGNORE INTO cat_species (species_name) VALUES ('Maine Coon'), ('Siamese'), ('Persian'), ('Bengal');
INSERT OR IGNORE INTO cats (user_id, name, species_id, date_of_birth, weight, profile_picture) 
VALUES (1, 'Whiskers', 1, '2018-06-12', 6.5, 'whiskers.jpg');
INSERT OR IGNORE INTO health_metrics VALUES (1, 4.5, 7.5);
INSERT OR IGNORE INTO grooming (cat_id, last_nail_cut, last_shower) 
VALUES (1, '2023-11-01', '2023-10-15');
