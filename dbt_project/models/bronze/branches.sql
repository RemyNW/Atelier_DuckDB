/*
    Bronze model for the "branches" table.
    This table pulls raw data directly from "raw.branches".
*/

{{ config(materialized='table') }}

SELECT * FROM {{ source('raw', 'branches') }}