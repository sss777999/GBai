UPDATE users SET updated_at = current_timestamp() WHERE created_at > updated_at;
CREATE TEMPORARY TABLE gender (gender CHAR(1));
INSERT INTO gender VALUES ('m'), ('f');
SELECT * FROM gender;
UPDATE profiles SET gender = (SELECT gender FROM gender ORDER BY RAND() LIMIT 1);
SELECT * FROM profiles;
UPDATE profiles SET updated_at = current_timestamp() WHERE created_at > updated_at;
SELECT * FROM profiles;
SHOW TABLES;
SELECT * FROM messages LIMIT 10;
UPDATE messages SET from_user_id = FLOOR(1 + (RAND() * 100)),
to_user_id = FLOOR(1 + (RAND() * 100));
SELECT * FROM media_types;
DELETE FROM media_types;
INSERT INTO media_types (name) VALUES ('photo'), ('video'), ('audio');
TRUNCATE media_types;
SELECT * FROM media;
UPDATE media SET media_type = FLOOR(1 + (RAND() * 3)),
user_id = FLOOR(1 + (RAND() * 100));
UPDATE media SET file_name = CONCAT('https://goodle.docs/vk/file_', file_name);
UPDATE media SET file_name = CONCAT(file_name, '.jpg') WHERE media_type = 1;
UPDATE media SET file_name = CONCAT(file_name, '.mkv') WHERE media_type = 2;
UPDATE media SET file_name = CONCAT(file_name, '.mp3') WHERE media_type = 3;
SELECT * FROM media;
UPDATE media SET metadata = CONCAT('{"owner":"',
	(SELECT CONCAT(first_name, ' ', last_name) FROM users WHERE id = user_id),
	'"}');
DESC media;
ALTER TABLE media MODIFY COLUMN metadata JSON;
UPDATE profiles SET photo_id = (
	SELECT id FROM media 
		WHERE media.user_id = profiles.user_id AND media_type = 1 LIMIT 1
);
ALTER TABLE profiles MODIFY COLUMN photo_id INT;

SELECT * FROM friendship LIMIT 10;
UPDATE friendship SET 
	user_id = FLOOR(1 + (RAND() * 100)),
	friend_id = FLOOR(1 + (RAND() * 100))
;
SELECT * FROM friendship_statuses;
TRUNCATE friendship_statuses;
INSERT INTO friendship_statuses (name)
	VALUES ('Requested'), ('Confirmed'), ('Rejected');

UPDATE friendship SET status_id = FLOOR(1 + (RAND() * 3));

SELECT * FROM communities;
DELETE FROM communities WHERE id > 20;
SELECT * FROM communities_users;
UPDATE communities_users SET community_id = FLOOR(1 + (RAND() * 20)); 
DESC friendship;
SELECT * FROM communities_users;

-- добавление
DESC messages;
ALTER TABLE messages ADD COLUMN read_at DATETIME;
ALTER TABLE messages ADD COLUMN edited_at DATETIME;
DESC profiles;
ALTER TABLE profiles ADD COLUMN status_message VARCHAR(255) AFTER photo_id;

ALTER TABLE communities ADD COLUMN media_id INT UNSIGNED AFTER name;
ALTER TABLE communities ADD COLUMN motto VARCHAR(255) AFTER media_id;
ALTER TABLE communities ADD COLUMN info TEXT AFTER motto;
DESC communities;

CREATE TABLE posts (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	media_id INT UNSIGNED,
	user_id INT UNSIGNED NOT NULL,
	head VARCHAR(255),
	body MEDIUMTEXT,
	created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
	updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- реализация лайков
CREATE TABLE likes (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY;
	whom_liked_id INT UNSIGNED NOT NULL,
	which_liked_id INT UNSIGNED NOT NULL,
	media_id INT UNSIGNED NOT NULL,
	updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- (тут момент задача, чтобы просто если человек повторно тсавит лайк, то просто дата нового лайка,
	-- это будет правильная реализация?)
);




























