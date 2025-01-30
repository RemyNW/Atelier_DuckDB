/*
    Silver model for the "issues" table.
    This table filters out closed issues and removes duplicates.
*/

{{ config(materialized='table') }}

WITH cleaned_data AS (
    SELECT DISTINCT *
    FROM {{ ref('issues') }} -- Reference the Bronze model
    WHERE state = 'open' -- Keep only open issues
)

SELECT *
FROM cleaned_data
