-- Impoprting metal bands.sql.zip then ordered by number
-- unzip metal_bands.sql.zip

CREATE DATABASE IF NOT EXISTS some_database;
Use some_database;

CREATE TABLE IF NOT EXISTS metal (
    origin VARCHAR(100),
    nb_fans INT
);

SOURCE metal_bands.sql;

SELECT origin, SUM(nb_fans) AS nb_fans,
        RANK() OVER (ORDER BY SUM(nb_fans) DESC) AS rank
FROM metal
GROUP BY origin
ORDER BY rank;