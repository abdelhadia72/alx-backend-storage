-- Trigger to ensure email validation integrity
-- Resets 'valid_email' attribute only when the email is updated,
-- ensuring accurate email validation status in the 'users' table

CREATE TRIGGER resets_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email <> NEW.email THEN
        SET NEW.valid_email = 0;
    END IF;
END;

