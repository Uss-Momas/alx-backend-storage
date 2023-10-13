-- create sql script that creates a trigger
-- the trigger resets the attribute 'valid_email' only when 'email' has been changed
CREATE TRIGGER email_validation 
BEFORE UPDATE
ON users 
FOR EACH ROW
IF NEW.email != OLD.email THEN SET NEW.valid_email = 0;
END IF;