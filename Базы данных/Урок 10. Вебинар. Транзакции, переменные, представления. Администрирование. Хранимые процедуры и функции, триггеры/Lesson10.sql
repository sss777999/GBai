-- SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));

-- Задание 1
CREATE INDEX users_id ON users(id);
CREATE INDEX likes_users_id_target_id ON likes (user_id, target_id);

-- Задание 2. Есть несколько моментов: 1) 5 пункт: общее количество пользователей в группе, это по каждой группе отдельно или как это понять?
-- 2) если имеется ввиду во всех группах, тогда зачем следующий пункт общее в системе? Если у нас в базе это одинаковое число. Хотя логично что эти цифры в релаьности могут быть разными.
-- Было бы хорошо, если бы задания писались конкретнее!
-- 3) также и в последнем пункте общее количество пользователей в группе / всего пользователей в системе. О какой группе идет речь, или это не правильно написано? Тут получается общее 
-- количество 100, на 100 делим и на 100 умножаем, не совсем понял как должно быть!!!
-- 4) еще такой вопрос Min и Max писал одинаково слово в слово, но пока мучался до этого выдавало одинаковые значения в поле Min и Max после того как все удалил и написал заново, заработало,
-- это баги какие-то или в чем может быть проблема?
-- 5) Среднеее количетсво ползьователей в группах отностительно чего? Среднее от общего количества и количества людей в группе?
USE vk;
SHOW TABLES;
DESC likes;
DESC communities;
SELECT * FROM communities_users;
DESC profiles;
SELECT * FROM profiles;

-- SELECT COUNT(*), users.id FROM users JOIN communities_users ON users.id = communities_users.user_id GROUP BY 2;

SELECT DISTINCT communities.name, 
COUNT(communities_users.user_id) OVER (PARTITION BY communities_users.community_id) as Average, -- вообще не понял как это посчитать, получается не среднее а общее если просто AVG вместо COUNT
-- как это правильно прописать? Понимаю, что avg(sum(count())) что-то такое должно бытьпо логике. Но так не работает.
MIN(profiles.birthday) OVER (PARTITION BY communities_users.community_id) as Min,
MAX(profiles.birthday) OVER (PARTITION BY communities_users.community_id) as Max,
COUNT(communities_users.user_id) OVER (PARTITION BY communities_users.community_id) as Count,
COUNT(profiles.user_id) OVER () as total_users,
COUNT(communities_users.user_id) OVER (PARTITION BY communities_users.community_id) / COUNT(profiles.user_id) OVER () * 100 as '%'
	FROM communities
		JOIN communities_users
			ON communities_users.community_id = communities.id
		JOIN profiles 
			ON profiles.user_id = communities_users.user_id;

-- SELECT MIN(birthday) FROM profiles;
-- SELECT MAX(birthday) FROM profiles;


-- Задание 3
/*
 * 1) сделать ENUM;
 * 2) сделать общий индекс на likes.user_id и likes.target_id, media, messages;
 * 3) индекс на id в profiles;
 */



