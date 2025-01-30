/*
    Bronze model for the "issues" table.
    This table pulls raw data directly from "raw.issues".
*/

{{ config(materialized='table') }}

SELECT * FROM {{ source('raw', 'issues') }}
