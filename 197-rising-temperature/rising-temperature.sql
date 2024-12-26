# Write your MySQL query statement below
SELECT w1.id
FROM Weather w1, Weather w2
WHERE DATEDIFF(w1.recordDate, w2.recordDate) = 1 AND w1.temperature > w2.temperature;

# https://www.w3schools.com/sql/func_sqlserver_datediff.asp --> for datedifference
# mention this because they mentioned yesterday which means 1 day difference WHERE DATEDIFF(w1.recordDate, w2.recordDate) = 1 