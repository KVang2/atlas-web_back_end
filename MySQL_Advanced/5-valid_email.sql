-- Trigger that resets attribute valid_email
-- When email has been changed
DELIMITER //

CREATE TRIGGER reset_email
AFTER INSERT ON users
FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END //

DELIMITER ;