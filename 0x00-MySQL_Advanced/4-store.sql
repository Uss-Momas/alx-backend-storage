-- sql script that creates a trigger
-- trigger that decreases the quantity of an item after adding new order
CREATE TRIGGER decreate_item_quantity 
AFTER INSERT ON orders FOR EACH ROW
BEGIN
	UPDATE items SET quantity = quantity - NEW.number Where NAME = NEW.item_name;
END;