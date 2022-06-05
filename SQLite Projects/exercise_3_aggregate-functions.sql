/* returning the count of the number of rows in a table */
select count(*) from fake_apps;

/* returning the count of the number of free apps in a table */
/* where 'price' is a REAL data-type. */
select count(*) from fake_apps where price = 0.0;

/* finding the total number of downloads across all apps */
select sum(downloads) from fake_apps;

/* returning the name of the app with the lowest amount of downloads with min() */
/* OPTION 1 */
select name from fake_apps
  where downloads = (select min(downloads) from fake_apps);
/* OPTION 2 */
/* the same query result but different execution */
select * from fake_apps
 order by downloads asc
 limit 1;

 /* returning info on apps that price rounds up to $1 */
 select * from fake_apps where round(price,0) = 1;

 /* return the name and rounded price of all apps */
 select name, round(price,0) from fake_apps;

 /* Getting the average value of all apps rounded to the 2nd decimal */
 select round(avg(price), 2) from fake_apps;

 /* Getting the count of apps at each price point */
select price as 'App Price', count(*) as 'Count'
 from fake_apps
 group by price;

 /* Getting the count of apps at each price point with the stipulation */
 /* that each app has been downloaded more than 20,000 times */
select price as 'App Price', count(*) as 'Count'
 from fake_apps
 where downloads > 20000
 group by price;

 /* Getting the total downlaods of each category of apps in the store */
 select category as 'App Category', sum(downloads) as 'Total Downlaods'
  from fake_apps
  group by category;