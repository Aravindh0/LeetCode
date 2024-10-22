/* Write your T-SQL query statement below */
WITH FirstLoginDates AS (
    SELECT
        player_id,
        MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
)
SELECT
    ROUND(CAST(COUNT(DISTINCT A.player_id) AS FLOAT) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM Activity A
JOIN FirstLoginDates F
    ON A.player_id = F.player_id
    AND A.event_date = DATEADD(DAY, 1, F.first_login);

