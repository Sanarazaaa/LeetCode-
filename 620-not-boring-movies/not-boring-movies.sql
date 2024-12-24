# Write your MySQL query statement below
# FROM Cinema table SELECT description 
SELECT * 
FROM Cinema 
WHERE MOD(id, 2) = 1 
AND description NOT LIKE '%boring%'
ORDER BY rating DESC;
