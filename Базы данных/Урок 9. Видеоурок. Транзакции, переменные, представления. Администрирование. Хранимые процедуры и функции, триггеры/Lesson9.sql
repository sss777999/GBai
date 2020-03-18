/* Часть 1 */

-- Задание 1
/*
CREATE DATABASE shop;
CREATE DATABASE sample;
SHOW TABLES;
SELECT * FROM shop.users;
SELECT * FROM sample.users;
use shop;
use sample;
TRUNCATE sample.users;
*/

START TRANSACTION;
INSERT INTO sample.users SELECT * FROM users WHERE id = 1;
COMMIT;

-- Задание 2

CREATE OR REPLACE VIEW prd AS 
	SELECT products.name 
		AS 'Product name', catalogs.name 
		AS 'Catalog name' 
	FROM products, catalogs 
	WHERE catalogs.id = products.catalog_id;
SELECT * FROM prd;



/* Часть 2 */

-- Задание 1
DROP FUNCTION IF EXISTS hello;
-- SELECT DATE_FORMAT(NOW(), '%H');
DELIMITER //
CREATE FUNCTION hello ()
RETURNS VARCHAR(255) DETERMINISTIC
BEGIN
	DECLARE t INT;
	SET t = DATE_FORMAT(NOW(), '%H');
	RETURN CASE
	WHEN t >= '06' AND t < '12' THEN 'Доброе утро'
	WHEN t >= '12' AND t < '18' THEN 'Добрый день'
	WHEN t >= '18' AND t < '00' THEN 'Добрый вечер'
	WHEN t >= '00' AND t < '06' THEN 'Доброй ночи'
	ELSE 'Привет'
	END;
END
//

SELECT hello()//

-- Задание 2
USE shop;
DELIMITER //
-- DROP TRIGGER IF EXISTS check_products_name;
-- DROP TRIGGER IF EXISTS check_products_description;
CREATE TRIGGER check_products_name BEFORE UPDATE ON products
FOR EACH ROW
BEGIN
	SET NEW.name = COALESCE(NEW.name, OLD.name);
	IF NEW.name = NULL THEN SIGNAL SQLSTATE '45001' SET MESSAGE_TEXT = 'Update of description cancelled';
	END IF;
END//

CREATE TRIGGER check_products_description BEFORE UPDATE ON products
FOR EACH ROW
BEGIN
	SET NEW.description = COALESCE(NEW.description, OLD.description);
	IF NEW.description = NULL THEN SIGNAL SQLSTATE '45002' SET MESSAGE_TEXT = 'Update of description cancelled';
	END IF;
END//

/* Не понимаю почему все равно можно NULL в name вставить, а в description нет. Одинаковые триггеры,
 * уже все перепробовал не могу понять. Доп видео и задания, если успею дополнительно доделаю.
 */


-- TRUNCATE products;
-- DELETE FROM products WHERE id = 9;
-- UPDATE products SET name = NULL;
-- UPDATE products SET description = NULL;
-- insert into products (name, description, price, catalog_id) values (NULL, 'NULL', '123', '123');
