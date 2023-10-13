-- SQL Script to create a view that lists all students 
-- that are under 80% and no last_meeting or more than 1 month
CREATE VIEW need_meeting AS 
	SELECT name
    FROM students 
    WHERE students.score < 80 AND (students.last_meeting IS NULL OR students.last_meeting < DATE_ADD(NOW(), INTERVAL -1 MONTH));