-- Explore and analyze the students data to see how the length of stay (stay)
-- impacts the average mental health diagnostic scores of the international students 
-- present in the study.

-- Return a table with nine rows and five columns.
-- The five columns should be aliased as: stay, count_int, average_phq, average_scs, and average_as, in that order.
-- The average columns should contain the average of the todep (PHQ-9 test), 
-- tosc (SCS test), and toas (ASISS test) columns for each length of stay, 
-- rounded to two decimal places.
-- The count_int column should be the number of international students for each length of stay.
-- Sort the results by the length of stay in descending order.

SELECT
    stay,  -- Length of stay of the students
    COUNT(*) AS count_int,  -- Number of international students for each length of stay
    ROUND(AVG(todep), 2) AS average_phq,  -- Average score of PHQ-9 test, rounded to two decimal places
    ROUND(AVG(tosc), 2) AS average_scs,  -- Average score of SCS test, rounded to two decimal places
    ROUND(AVG(toas), 2) AS average_as  -- Average score of ASISS test, rounded to two decimal places
FROM 
    students
WHERE 
    inter_dom = 'Inter'  -- Filter to include only international students
GROUP BY
    stay  -- Group results by length of stay
ORDER BY
    stay DESC  -- Sort results by length of stay in descending order
LIMIT 9;  -- Limit the results to nine rows
