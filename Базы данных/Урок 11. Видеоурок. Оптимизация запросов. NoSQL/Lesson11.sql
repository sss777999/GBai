-- Часть 1

-- Задание 1
DELIMITER //

DROP TABLE IF EXISTS logs;
CREATE TABLE logs (
	id INT UNSIGNED NOT NULL,
	time INT UNSIGNED NOT NULL,
	name VARCHAR(255) NOT NULL,
	ident_id INT NOT NULL,
	text_name VARCHAR(255) NOT NULL
) ENGINE=archive;

-- DROP TRIGGER IF EXISTS logs_update_users;
CREATE TRIGGER logs_update_users AFTER INSERT ON users
FOR EACH ROW
BEGIN
	INSERT INTO logs(time, name, ident_id, text_name) VALUES (NOW(), 'users', NEW.id, NEW.name);
END//

-- DROP TRIGGER IF EXISTS logs_update_catalogs;
CREATE TRIGGER logs_update_catalogs AFTER INSERT ON catalogs
FOR EACH ROW
BEGIN
	INSERT INTO logs(time, name, ident_id, text_name) VALUES (NOW(), 'catalogs', NEW.id, NEW.name);
END//

-- DROP TRIGGER IF EXISTS logs_update_products;
CREATE TRIGGER logs_update_products AFTER INSERT ON products
FOR EACH ROW
BEGIN
	INSERT INTO logs(time, name, ident_id, text_name) VALUES (NOW(), 'products', NEW.id, NEW.name);
END//

DELIMETER ;



-- Часть 2

-- Задание 1
/*
SADD ip 192.168.1.1 127.0.0.0 10.0.0.0
SCARD ip
*/

-- Задание 2
-- MSET name andrew email '2@mail.com'
-- MGET name
-- MGET email

-- Задание 3
/*
-- use shop
db.shop.insert({'category': {'CPU': ['Intel core i9', 'Intel core i7', 'AMD Ryzen 7']}, 'GPU': ['RTX 2080', 'Titan', 'AMD']})
-- db.shop.find()
-- категорий в базе не нашел и товаров тоже. Поэтому сделал свое по 2 категориям товаров.
*/

