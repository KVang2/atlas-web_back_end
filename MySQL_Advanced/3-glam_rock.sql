-- SQL script to lists all bands with Glam rock
-- Ranked by longevity
SELECT band_name,
    -- to calculate years band has been active (lifespan)
    IFNULL(split, YEAR(CURDATE())) - formed AS lifespan
FROM metal_bands
WHERE main_style = 'Glam rock'
ORDER BY lifespan DESC;