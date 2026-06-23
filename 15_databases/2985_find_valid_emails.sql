-- Problem: 2985. Find Valid Emails
-- Pattern: Databases / String Matching (REGEXP)
-- Key insight: Use REGEXP to validate email structure - alphanumeric/underscore before @, letters-only domain, ends with .com

SELECT user_id, email
FROM Users
WHERE email REGEXP '^[a-zA-Z0-9_]+@[a-zA-Z]+\\.com$'
ORDER BY user_id;
