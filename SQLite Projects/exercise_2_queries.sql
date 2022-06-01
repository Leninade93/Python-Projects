https://www.codecademy.com/learn/learn-sql/modules/learn-sql-queries/cheatsheet
/* run queries where you have partial information with the % and _ wildcard charaters and */
/* and the like keyword */
select * from movies where name like '%Dead';
SELECT * FROM movies WHERE name LIKE 'Se_en';
/* the string literal in a %wildcard value is not case-sensitive */
select * from movies where name like '%man%';

/* Can use alias to change the returned name of columns in select queries */
SELECT name AS 'Desired_Value' FROM table_1;

/* Adding the DISTINCT keyword to a select statement will return only unique values */
SELECT DISTINCT name from table_1;

/* Can use the BETWEEN keyword added to a WHERE clause to filter results alphabetically and numerically. */
SELECT * FROM movies WHERE year BETWEEN 1990 AND 1999;

select * from movies where name between 'A' and 'J'; /* all moves that start with A up to but not including J */
/* However, if a movie has a name of simply ‘J’, it would actually match. This is because BETWEEN goes up to the
 second value — up to ‘J’. So the movie named ‘J’ would be included in the result set but not ‘Jaws’. */

/* Using the AND and OR keyword we can further tailor our results down */
select * from movies
where year between 1970 and 2020
    and genre = 'romance'
order by year asc;

select * from movies
where genre = 'romance'
  or genre = 'comedy'
order by imdb_rating desc;

/* Imposing LIMITs on query results. This always goes at the end of a statement and
   isn't supported by all SQL databases. */
select *
from movies
order by imdb_rating desc
limit 3;

/* A CASE statement allows us to create different outputs */
/* (usually in the SELECT statement). It is SQL’s way of handling if-then logic. */
SELECT name, imdb_rating,
 CASE
  WHEN imdb_rating > 8 THEN 'Fantastic'
  WHEN imdb_rating > 6 THEN 'Poorly Received'
  ELSE 'Avoid at All Costs'
 END AS 'Review'
FROM movies
ORDER BY imdb_rating DESC;

