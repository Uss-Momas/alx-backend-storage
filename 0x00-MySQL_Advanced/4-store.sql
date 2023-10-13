-- sql script that creates a trigger
-- trigger that decreases the quantity of an item after adding new order
CREATE TRIGGER decreate_item_quantity 
AFTER INSERT 
ON orders 
FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE NAME = NEW.item_name;