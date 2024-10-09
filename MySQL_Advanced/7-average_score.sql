-- creates a stored procedure ComputerAverageScoreForUser
-- compute and store average score for student
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser (
    IN p_user_id INT
)
BEGIN
    DECLARE avg_score FLOAT;

    -- Caclculate average score for user_id
    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = p_user_id;

    -- Update
    UPDATE users
    SET average_score = avg_score
    WHERE id = p_user_id;

END //

DELIMITER ;