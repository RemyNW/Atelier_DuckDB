/*
    Silver model for the "contributors" table.
    This table filters out commits with missing or invalid data.
*/

{{ config(materialized='table') }}

WITH cleaned_data AS (
    SELECT id, login
    FROM {{ ref('contributors') }} -- Reference the Bronze model
)

SELECT *
FROM cleaned_data