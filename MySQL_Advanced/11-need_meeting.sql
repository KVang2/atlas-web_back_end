-- create view for meeting
CREATE VIEW need_meeting AS
SELECT name
FROM student
WHERE score < 80
    AND (last_meeting IS NULL OR last_meeting < DATE_SUB(CURDATE(), INTERVAL 1 MONTH));