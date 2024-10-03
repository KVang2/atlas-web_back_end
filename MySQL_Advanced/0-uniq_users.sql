-- Table for User data
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email str(255), NOT NULL UNIQUE,
    name: str(255),
    PRIMARY KEY (id)
);