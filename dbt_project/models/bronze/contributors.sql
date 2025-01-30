/*
    Bronze model for the "contributors" table.
    This table pulls raw data directly from "raw.contributors".
*/

{{ config(materialized='table') }}

SELECT * FROM {{ source('raw', 'contributors') }}