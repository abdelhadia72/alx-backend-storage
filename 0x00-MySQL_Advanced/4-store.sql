-- Decreases the quantity of items in response to new orders
-- Updates the 'quantity' of items by subtracting the newly inserted 'number'
-- Targets the item specified by 'item_name' in the 'items' table

CREATE TRIGGER decrease_items_quantity AFTER INSERT ON orders FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE name=NEW.item_name;
