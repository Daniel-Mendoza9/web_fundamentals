-- Forward engineer the dojos_and_ninjas_schema from the previous chapter

-- Create a .txt file where you'll save each of your queries from below

-- Query: Create 3 new dojos

INSERT INTO dojos (name) VALUES ('Burbank'), ('San Jose'), ('online');

-- Query: Delete the 3 dojos you just created

DELETE FROM dojos;

-- Query: Create 3 more dojos

INSERT INTO dojos (name) VALUES ('Burbank'), ('San Jose'), ('online');

-- Query: Create 3 ninjas that belong to the first dojo

INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ('Troy', 'Manasala', 23, 1), ('Val', 'Camarillo', 21, 1), ('John', 'code', 24, 1);


-- Query: Create 3 ninjas that belong to the second dojo

INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ('Chicken', 'Little', 21, 2), ('Donald', 'Duck', 20, 2), ('John', 'Doe', 24, 2);

-- Query: Create 3 ninjas that belong to the third dojo

INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ('Luffy', 'Land', 21, 3), ('Spider', 'Pig', 18, 3), ('Jane', 'Doe', 24, 3);

-- Query: Retrieve all the ninjas from the first dojo

SELECT * FROM ninjas WHERE dojo_id = 1;

-- Query: Retrieve all the ninjas from the last dojo

SELECT * FROM ninjas where dojo_id = 3;

-- Query: Retrieve the last ninja's dojo

SELECT * FROM dojos where id = (SELECT dojo_id FROM ninjas ORDER BY id DESC LIMIT 1);

-- Submit your .txt file that contains all the queries you ran in the shell