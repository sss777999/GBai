-- Таблица лайков
DROP TABLE IF EXISTS likes;
CREATE TABLE likes (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  user_id INT UNSIGNED NOT NULL,
  target_id INT UNSIGNED NOT NULL,
  target_type_id INT UNSIGNED NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Таблица типов лайков
DROP TABLE IF EXISTS target_types;
CREATE TABLE target_types (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL UNIQUE,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO target_types (name) VALUES 
  ('messages'),
  ('users'),
  ('media'),
  ('posts');
  
-- Заполняем лайки
INSERT INTO likes 
  SELECT 
    id, 
    FLOOR(1 + (RAND() * 100)), 
    FLOOR(1 + (RAND() * 100)),
    FLOOR(1 + (RAND() * 4)),
    CURRENT_TIMESTAMP 
  FROM messages;
 
/* ПЗ к 6 уроку */

-- 1 задание, предложений нет для улучшения.

-- 2 задание
SELECT SUM(total) AS 'Amount of likes' FROM (SELECT COUNT(*) AS total, target_id, (SELECT birthday FROM profiles WHERE target_id = user_id) AS bday FROM likes GROUP BY 2 ORDER BY 3 DESC LIMIT 10) as a;

-- 3 задание
SELECT IF 
((SELECT COUNT(tart) AS 'sum m' FROM (SELECT target_id, user_id, (SELECT gender FROM profiles WHERE target_id = user_id) AS tart FROM likes) as m WHERE tart = 'm') >
(SELECT COUNT(tart) AS 'sum m' FROM (SELECT target_id, user_id, (SELECT gender FROM profiles WHERE target_id = user_id) AS tart FROM likes) as e WHERE tart = 'f'), 'more male', 'more female');

-- SELECT COUNT(tart) AS 'sum male' FROM (SELECT target_id, user_id, (SELECT gender FROM profiles WHERE target_id = user_id) AS tart FROM likes) as m WHERE tart = 'm';
-- SELECT COUNT(tart) AS 'sum female' FROM (SELECT target_id, user_id, (SELECT gender FROM profiles WHERE target_id = user_id) AS tart FROM likes) as e WHERE tart = 'f';
-- DESC likes;
-- DESC profiles;

-- 4 задание

/* SHOW TABLES;
DESC posts;
DESC messages;
SELECT * FROM posts;

-- лайки
SELECT COUNT(*) AS total, target_id, (SELECT birthday FROM profiles WHERE target_id = user_id) AS bday FROM likes GROUP BY 2 ORDER BY 1, 2;
-- посты
SELECT COUNT(*) AS total, user_id AS us, (SELECT birthday FROM profiles WHERE us = user_id) AS bday FROM posts GROUP BY 2 ORDER BY 1, 2;
-- сообщения
SELECT COUNT(*) AS total, from_user_id, (SELECT birthday FROM profiles WHERE from_user_id = user_id) AS bday FROM messages GROUP BY 2 ORDER BY 1, 2;
*/

-- выбор рандомно 10 самых неактивных по трем источникам: лайки, посты, сообщения (чтобы user был хотя бы в 2 группах):
SELECT COUNT(target_id) AS 'count', target_id as 'ID of user' FROM 
((SELECT COUNT(*) AS total, target_id FROM likes GROUP BY 2 ORDER BY 1, 2)
UNION ALL
(SELECT COUNT(*) AS total, user_id FROM posts GROUP BY 2 ORDER BY 1, 2)
UNION ALL
(SELECT COUNT(*) AS total, from_user_id FROM messages GROUP BY 2 ORDER BY 1, 2)
) as h GROUP BY 2 HAVING count > 1 ORDER BY 1 DESC LIMIT 10;















 
 
 
 
 
 
 
 