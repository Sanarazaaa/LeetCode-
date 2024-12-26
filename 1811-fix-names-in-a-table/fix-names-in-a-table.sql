# Write your MySQL query statement below
SELECT user_id,
CONCAT_WS('', UPPER(SUBSTR(name,1,1)), LOWER(SUBSTR(name,2))) AS name FROM users ORDER BY user_id;

# SUBSTR(name, 1, 1) extracts the first character of the name column.
# UPPER(...) converts that first character to uppercase
# SUBSTR(name, 2) extracts the substring starting from the second character of name (ignoring the first character).
# LOWER(...) converts the extracted substring to lowercase.