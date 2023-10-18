-- SQL Script  that creates a stored procedure ComputeAverageWeightedScoreForUser 
-- that computes and store the average weighted score for a student.
DELIMITER $$;
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    SET @average_score = 1
    UPDATE users SET users.average_score=@average_score WHERE users.id = user_id;
END
$$;
DELIMITER ;