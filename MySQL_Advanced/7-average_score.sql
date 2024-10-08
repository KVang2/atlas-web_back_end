-- creates a stored procedure ComputerAverageScoreForUser
-- compute and store average score for student
DELIMITER //

CREATE PROCEDURE ComputerAverageScoreForUser (
    IN p_user_id INT
)
BEGIN
    DECLARE average_score FLOAT;

    -- Caclculate average score for user_id
    SELECT AVG(score) INTO average_score
    FROM corrections
    WHERE corrections.user_id = p_user_id;

    -- Update
    UPDATE users
    SET average_score = average_score
    WHERE id = p_user_id;
END //

DELIMITER ;