DROP TABLE IF EXISTS assembly_part;
DROP TABLE IF EXISTS assembly;
DROP TABLE IF EXISTS part_image;
DROP TABLE IF EXISTS part_tag;
DROP TABLE IF EXISTS part;
DROP TABLE IF EXISTS part_model;
DROP TABLE IF EXISTS part_category;


CREATE TABLE part_categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
    description TEXT
);


CREATE TABLE part_models (
    id SERIAL PRIMARY KEY,
    uri VARCHAR(512) NOT NULL,
    format VARCHAR(50) NOT NULL,
    accuracy INTEGER NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE parts (
    id SERIAL PRIMARY KEY,
    part_number VARCHAR(100) NOT NULL UNIQUE,
    name VARCHAR(256) NOT NULL,
    description TEXT,
    category_id INT REFERENCES part_categories(id),
    uri VARCHAR(512),
    model_id INT REFERENCES part_models(id)
);


CREATE TABLE part_tags (
    id SERIAL PRIMARY KEY,
    part_id INT REFERENCES parts(id),
    tag VARCHAR(100) NOT NULL,
    value VARCHAR(256),
    unit VARCHAR(50)
);


CREATE TABLE part_images (
    id SERIAL PRIMARY KEY,
    part_id INT REFERENCES parts(id),
    uri VARCHAR(512) NOT NULL,
    caption TEXT
);


CREATE TABLE assemblies (
    id SERIAL PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
    description TEXT
);


CREATE TABLE assembly_parts (
    id SERIAL PRIMARY KEY,
    assembly_id INT REFERENCES assemblies(id),
    part_id INT REFERENCES parts(id),
    transform TEXT NOT NULL,
    parent_part_id INT REFERENCES parts(id)
);

