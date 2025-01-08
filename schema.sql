CREATE TABLE users (
    user_id SERIAL PRIMARY KEY, 
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20)
);

CREATE TABLE cat_species (
    species_id SERIAL PRIMARY KEY,
    species_name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE cats (
    cat_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    species_id INT REFERENCES cat_species(species_id),
    date_of_birth DATE,
    weight DECIMAL(5,2),
    profile_picture TEXT
);

CREATE TABLE grooming (
    grooming_id SERIAL PRIMARY KEY,
    cat_id INT REFERENCES cats(cat_id) ON DELETE CASCADE,
    last_nail_cut DATE,
    last_shower DATE
);

CREATE TABLE health_metrics (
    species_id INT PRIMARY KEY REFERENCES cat_species(species_id),  -- Links to cat species
    normal_weight_min DECIMAL(5,2),  -- Minimum healthy weight
    normal_weight_max DECIMAL(5,2)  -- Maximum healthy weight
);

