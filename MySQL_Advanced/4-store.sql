-- SQL script that creates a trigger that decreases the quantity of an item
-- Add delimiter
DELIMITER //

CREATE TRIGGER decrease_quantity
AFTER INSERT ON orders
FOR EACH ROW 
BEGIN 
    UPDATE items SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END //

DELIMITER ;