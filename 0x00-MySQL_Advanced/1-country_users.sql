-- Create the users table if it doesn't already exist
-- Define the structure of the users table with necessary constraints

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255),
    country ENUM("US", "CO", "TN") NOT NULL DEFAULT "US"
)