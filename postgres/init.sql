-- postgres/init.sql --- this is to import the initial data schema
CREATE TABLE users ( id SERIAL PRIMARY KEY, username VARCHAR(50) NOT NULL );
CREATE TABLE questions ( id SERIAL PRIMARY KEY, text TEXT NOT NULL );
CREATE TABLE attempts ( id SERIAL PRIMARY KEY, user_id INT, score INT );

INSERT INTO questions (text) VALUES 
('What does SRE stand for?'),
('Explain the RED method.'),
('What is a Service Level Objective?'),
('Define MTTR.'),
('How does distributed tracing work?');
