-- models/gold/commits_by_week.sql

WITH commits_data AS (
    SELECT
        c.sha AS commit_id,
        c.commit.author.date AS commit_date,
        c.commit.message AS commit_message
    FROM {{ ref('commits_transformed') }} c
)

SELECT
    DATE_TRUNC('week', CAST(commit_date AS DATE)) AS commit_week,  -- Tronquer la date à la semaine
    COUNT(commit_id) AS commit_count                             -- Nombre de commits par semaine
FROM commits_data
GROUP BY commit_week  -- Regrouper par semaine
ORDER BY commit_week DESC