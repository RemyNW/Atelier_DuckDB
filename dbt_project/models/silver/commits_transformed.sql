/*
    Silver model for the "commits" table.
    This table filters out commits with missing or invalid data.
*/

{{ config(materialized='table') }}

WITH cleaned_data AS (
    SELECT sha, commit
    FROM {{ ref('commits') }} -- Reference the Bronze model
)

SELECT *
FROM cleaned_data