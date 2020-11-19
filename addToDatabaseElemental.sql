DELIMITER //
CREATE PROCEDURE add_to_elemental(IN column1 VARCHAR(24), IN column2 VARCHAR(24), IN column3 VARCHAR(24))
BEGIN
	INSERT INTO Elemental_Interactions VALUES (column1, column2, column3);
END //
DELIMITER ;