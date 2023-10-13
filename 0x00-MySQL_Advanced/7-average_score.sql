-- SQL Script stored procedure that computes and store the 
-- average score for a student
DELIMITER $$;
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    SET @average_score = (SELECT avg(score) FROM corrections WHERE user_id = user_id);
    UPDATE users SET average_score=@average_score WHERE id = user_id;
END
$$;
DELIMITER ;