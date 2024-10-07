-- Importing metal bands.sql.zip then ordered by number
SELECT origin, SUM(nb_fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;