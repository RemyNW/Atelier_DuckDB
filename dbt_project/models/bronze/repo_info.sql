/*
    Bronze model for the "repo_info" table.
    This table pulls raw data directly from "raw.repo_info".
*/

{{ config(materialized='table') }}

SELECT * FROM {{ source('raw', 'repo_info') }}
