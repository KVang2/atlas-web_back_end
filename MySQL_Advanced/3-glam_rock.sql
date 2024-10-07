-- SQL script to lists all bands with Glam rock
-- Ranked by longevity
SELECT
    band_name,
    COALESCE(split, YEAR(CURDATE())) - formed AS lifespan
FROM metal_bands
WHERE main_style LIKE '%Glam rock%'
ORDER BY lifespan DESC;