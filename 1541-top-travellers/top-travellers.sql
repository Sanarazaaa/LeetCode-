# Write your MySQL query statement below
SELECT 
    u.name,
    COALESCE(SUM(r.distance), 0) AS travelled_distance
FROM 
    Users u
LEFT JOIN # write the name of the table that u want to join
    Rides r
ON  # on --> write what is present in both
    u.id = r.user_id
GROUP BY 
    u.id, u.name
ORDER BY 
    travelled_distance DESC,
    u.name ASC;
