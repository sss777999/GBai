-- Задания 1,2
ALTER TABLE profiles
	ADD CONSTRAINT profiles_user_id_fk
		FOREIGN KEY (user_id) REFERENCES users (id),
	ADD CONSTRAINT profile_photo_id_fk
		FOREIGN KEY (photo_id) REFERENCES media (id);

ALTER TABLE profiles MODIFY COLUMN photo_id INT UNSIGNED;



ALTER TABLE friendship
	ADD CONSTRAINT friendship_user_id_fk
		FOREIGN KEY (user_id) REFERENCES users (id),
	ADD CONSTRAINT friendship_friend_id_fk
		FOREIGN KEY (friend_id) REFERENCES users (id),
	ADD CONSTRAINT friendship_status_id_fk
		FOREIGN KEY (status_id) REFERENCES friendship_statuses (id);

	
	
ALTER TABLE likes
	ADD CONSTRAINT likes_user_id_fk
		FOREIGN KEY (user_id) REFERENCES users (id),
	ADD CONSTRAINT likes_target_id_fk
		FOREIGN KEY (target_id) REFERENCES users (id),
	ADD CONSTRAINT likes_target_type_id_fk
		FOREIGN KEY (target_type_id) REFERENCES target_types (id);



ALTER TABLE messages
	ADD CONSTRAINT messages_from_user_id_fk
		FOREIGN KEY (from_user_id) REFERENCES users (id),
	ADD CONSTRAINT messages_to_user_id_fk
		FOREIGN KEY (to_user_id) REFERENCES users (id);



ALTER TABLE media
	ADD CONSTRAINT media_media_type_fk
		FOREIGN KEY (media_type) REFERENCES media_types (id),
	ADD CONSTRAINT media_user_id_fk
		FOREIGN KEY (user_id) REFERENCES users (id);
	


ALTER TABLE posts
	ADD CONSTRAINT posts_media_id_fk
		FOREIGN KEY (media_id) REFERENCES media (id),
	ADD CONSTRAINT posts_users_id_fk
		FOREIGN KEY (user_id) REFERENCES users (id);



ALTER TABLE communities_users
	ADD CONSTRAINT communities_users_community_id_fk
		FOREIGN KEY (community_id) REFERENCES communities (id),
	ADD CONSTRAINT communities_users_users_id_fk
		FOREIGN KEY (user_id) REFERENCES users (id);



ALTER TABLE communities
	ADD CONSTRAINT communities_media_id_fk
		FOREIGN KEY (media_id) REFERENCES media (id);

	

-- Задание 2

-- 1
SELECT SUM(total) AS 'Amount of likes' 
FROM (SELECT COUNT(*) AS total, target_id, (SELECT birthday FROM profiles WHERE target_id = user_id) AS bday
FROM likes JOIN profiles
ON target_type_id = 2 AND likes.target_id = profiles.user_id
GROUP BY 2 
ORDER BY 3 DESC 
LIMIT 10) 
as a;

-- 2	
SELECT 
  (CASE(p.gender)
		WHEN 'm' THEN 'man'
		WHEN 'f' THEN 'woman'
	END) AS gender, 
	COUNT(*) as likes_count 
	  FROM (
	    SELECT 
	      user_id as user, 
		    (SELECT gender FROM profiles) as gender 
		  FROM likes) dummy_table JOIN profiles as p
		  ON p.user_id = user
  GROUP BY p.gender
  ORDER BY likes_count DESC
  LIMIT 1;
	
-- 3 (не очень понял как тут нужно было JOIN использовать, поэтому просто с его помощью добавил информации)
-- если можно объясните, как это нужно было сделать
SELECT CONCAT(first_name, ' ', last_name) AS user, 
	(SELECT COUNT(*) FROM likes WHERE likes.user_id = users.id) + 
	(SELECT COUNT(*) FROM media WHERE media.user_id = users.id) + 
	(SELECT COUNT(*) FROM messages WHERE messages.from_user_id = users.id) 
	AS overall_activity, id, country
	FROM users JOIN profiles
	ORDER BY overall_activity
	LIMIT 10;

-- возможно такой вариант, делал ночью, сейчас днем пересмотрел немного, суть я понимаю хорошо, забыл немного структуру вк дб
SELECT 
CONCAT(users.id, ' ', first_name, ' ', last_name), COUNT(*) 
FROM users 
JOIN posts ON posts.user_id = users.id 
JOIN likes ON likes.target_id = users.id
JOIN messages ON messages.from_user_id = users.id
GROUP BY 1 
ORDER BY 2 LIMIT 10;

