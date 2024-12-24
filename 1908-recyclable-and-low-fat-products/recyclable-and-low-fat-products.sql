# Write your MySQL query statement below
# SELECT Products WHERE low_fats and recyclable == Y; 
SELECT product_id
FROM Products 
WHERE low_fats = 'Y' 
AND recyclable = 'Y';
