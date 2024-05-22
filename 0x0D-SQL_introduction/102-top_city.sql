--Write a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
USE hbtn_0c_0;

SELECT city, temperature, recorded_date
FROM temperatures
WHERE MONTH(recorded_date) IN (7, 8)
ORDER BY temperature DESC
LIMIT 3;
