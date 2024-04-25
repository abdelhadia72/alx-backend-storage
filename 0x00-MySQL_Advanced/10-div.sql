-- Defines a safe division function named SafeDiv.
-- It prevents division by zero by returning 0 if the denominator is zero.
-- The function takes two integer parameters, a numerator (a) and a denominator (b), and returns their division result as a float.
DELIMITER $$

DROP FUNCTION IF EXISTS SafeDiv$$
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
    RETURN (IF (b = 0, 0, a / b));
END$$

DELIMITER ;

