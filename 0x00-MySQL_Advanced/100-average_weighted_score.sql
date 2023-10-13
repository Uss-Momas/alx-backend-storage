-- SQL Script  that creates a stored procedure ComputeAverageWeightedScoreForUser 
-- that computes and store the average weighted score for a student.
DELIMITER $$;
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    SET @average_score = (
        SELECT SUM((score * weight)) / SUM(weight) AS weighted_avg_score 
        FROM holberton.corrections
        Join projects
        ON projects.id = corrections.project_id
        where corrections.user_id = user_id
    );
    UPDATE users SET users.average_score=@average_score WHERE users.id = user_id;
END
$$;
DELIMITER ;