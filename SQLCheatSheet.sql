SELECT DISTINCT;

WHERE MOD(ID, 2) = 0; /* Get all Even ID, ODD = 1 */

SELECT COUNT (CITY) - COUNT (DISTINCT CITY); /* Number of entries MINUS number of distinct entries */

LIMIT 1;

SELECT DISTINCT CITY FROM STATION WHERE SUBSTRING(CITY,1,1) IN ('a','e','i','o','u'); /* Starts with a vowel */
SELECT DISTINCT CITY FROM STATION WHERE SUBSTRING(CITY,-1) IN ('a','e','i','o','u'); /* Ends with */

ORDER BY SUBSTRING(CITY, -3), ID /* Sort by last 3 Chars in CITY, then by ID */

SELECT MAX(column)
SELECT MIN(column)
