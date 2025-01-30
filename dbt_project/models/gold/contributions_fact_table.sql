/*
    Gold model for the "contribution_fact_table" table.
    This table joins the "branches_transformed", "contributor_stransformed", and "commits_transformed" tables.
*/


WITH commits_per_branch AS (
    SELECT
        b.name AS branch_name,
        c.sha AS commit_id,
        c.commit.author.name AS author_name,
        c.commit.author.date AS commit_date,
        c.commit.message AS commit_message,
    FROM {{ ref('branches_transformed') }} b
    LEFT JOIN {{ ref('commits_transformed') }} c
        ON c.sha = b.commit.sha
)

SELECT
    branch_name,
    commit_id,
    author_name,
    commit_date,
    commit_message
FROM commits_per_branch c
