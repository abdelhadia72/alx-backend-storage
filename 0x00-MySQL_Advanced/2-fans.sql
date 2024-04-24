-- Calculate the total number of fans for each origin
-- Group the bands by their origin and sum the number of fans for each group
-- Order the result set by the total number of fans in descending order

SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;

