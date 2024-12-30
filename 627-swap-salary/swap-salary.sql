# Write your MySQL query statement below
UPDATE Salary
SET sex = CASE # handle multiple conditions and assign values based on those conditions
    WHEN sex = 'm' THEN 'f'
    WHEN sex = 'f' THEN 'm'
    ELSE sex # if the value of sex is neither 'm' nor 'f', it remains unchanged.
END;

