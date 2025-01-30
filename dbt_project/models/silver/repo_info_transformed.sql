/*
    Silver model for the "repo_info" table.
    This table restructures the raw repository information for analytics.
*/

{{ config(materialized='table') }}

WITH structured_data AS (
    SELECT
        id,
        name,
        full_name,
        description,
        stargazers_count,
        forks_count,
        created_at,
        updated_at
    FROM {{ ref('repo_info') }} -- Reference the Bronze model
)

SELECT *
FROM structured_data
