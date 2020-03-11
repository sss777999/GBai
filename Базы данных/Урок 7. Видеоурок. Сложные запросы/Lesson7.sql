-- Задание 1
INSERT INTO orders VALUES
  (1, 1, '2020-03-10 21:46:48', '2020-03-11 21:50:48'),
  (2, 1, '2019-03-11 22:54:48', '2020-04-11 22:50:48'),
  (3, 1, '2019-04-12 14:23:48', '2019-08-11 22:50:48'),
  (4, 2, '2020-04-09 15:43:48', '2020-03-11 22:50:48'),
  (5, 6, '2020-04-28 12:43:48', '2020-03-11 22:50:48'),
  (6, 6, '2019-05-30 11:34:48', '2019-06-11 22:50:48'),
  (7, 5, '2019-07-03 12:42:48', '2019-09-11 22:50:48'),
  (8, 3, '2020-02-05 23:11:48', '2020-03-11 22:50:48'),
  (9, 3, '2020-01-09 19:54:48', '2020-03-11 22:50:48'),
  (10, 2, '2019-04-05 20:47:48', '2019-06-11 22:50:48'),
  (11, 4, '2019-04-09 17:21:48', '2019-08-11 22:50:48');

SELECT DISTINCT 
name 
FROM 
users AS u
RIGHT JOIN 
orders AS o
ON 
o.user_id = u.id;



-- Задание 2
SELECT 
p.name, p.description, p.catalog_id 
FROM 
products AS p
JOIN 
catalogs AS c
ON
p.catalog_id = c.id;



-- Задание 3
DROP TABLE IF EXISTS flights;
CREATE TABLE flights (
id SERIAL PRIMARY KEY,
fromm VARCHAR(255) NOT NULL COMMENT 'Откуда рейс',
too VARCHAR(255) NOT NULL COMMENT 'Куда рейс');

INSERT INTO flights VALUES 
(1, 'moscow', 'omsk'),
(2, 'novgorod', 'kazan'),
(3, 'irkutsk', 'moscow'),
(4, 'omsk', 'irkutsk'),
(5, 'moscow', 'kazan');


DROP TABLE IF EXISTS cities;
CREATE TABLE cities (
label VARCHAR(255) NOT NULL COMMENT 'Наименование англ.',
name VARCHAR(255) NOT NULL COMMENT 'Наименование русское');

INSERT INTO cities VALUES 
('moscow', 'Москва'),
('novgorod', 'Новгород'),
('irkutsk', 'Иркутск'),
('omsk', 'Омск'),
('kazan', 'Казань');

-- Решение
SELECT (SELECT name FROM cities where label = vk.flights.fromm), (SELECT name FROM cities where label = vk.flights.too) FROM flights;
-- SELECT f.id, f.fromm, c.name FROM flights as f JOIN cities as c ON f.too = c.label;


