-- Сначала запускаем этот скрипт, после команды из 1.3 скриншота
/* Для того, чтобы работало пришлось из файла дампа удалить строку с TABLESPACE `mysql` 
в 30 строке.  Что было найдено методом перебора разных вариантов. Думаю это не правильно, 
подскажите как нужно было это сделать верно. */
DROP DATABASE IF EXISTS example;
CREATE DATABASE example;
USE example;
DROP TABLE IF EXISTS users;
CREATE TABLE users (
id INT,
name VARCHAR(255)
);
DESCRIBE users;
DROP DATABASE IF EXISTS sample;
CREATE DATABASE sample;
SHOW DATABASES;
