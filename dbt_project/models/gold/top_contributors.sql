WITH commit_counts AS (
    SELECT
        commit.author.name AS author_name,
        COUNT(commit.author.name) AS commit_count
    FROM {{ ref('commits_transformed') }}
    GROUP BY commit.author.name
)

SELECT 
    author_name, 
    commit_count
FROM commit_counts
ORDER BY commit_count DESC
