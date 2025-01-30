/*
    Silver model for the "branches" table.
    This table removes duplicates and applies basic transformations.
*/

{{ config(materialized='table') }}

WITH cleaned_data AS (
    SELECT name, commit
    FROM {{ ref('branches') }} -- Reference the Bronze model
)

SELECT *
FROM cleaned_data
