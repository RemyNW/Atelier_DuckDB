/*
    Bronze model for the "commits" table.
    This table pulls raw data directly from "raw.commits".
*/

{{ config(materialized='table') }}

SELECT * FROM {{ source('raw', 'commits') }}
