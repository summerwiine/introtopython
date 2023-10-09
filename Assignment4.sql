-- task1
SELECT name, movie FROM winners;

-- task2
SELECT movie FROM winners
WHERE movie LIKE '[a,e,o,i,u]%';
	
-- task2b
SELECT movie FROM winners
WHERE movie NOT LIKE '[a,e,o,i,u]%';	
   	 
	  
-- task3
SELECT DISTINCT(movie) FROM winners
WHERE movie LIKE '%[a,e,o,i,u]'; 

-- task4
SELECT name FROM winners;

-- task5
SELECT name FROM winners 
WHERE award = 'Best actress' AND birth_pl = 'England';

-- task6
SELECT director FROM movies
WHERE country = 'United States';

-- task7
SELECT movie, oscar_yr FROM movies
WHERE oscar_yr > 2017;

-- task8
SELECT movie, oscar_yr AS year, budget FROM movies
WHERE oscar_yr > 2016 AND budget <= 15;

-- task9
SELECT movie, budget FROM movies
WHERE director = 'Joe Wright';

-- task10
SELECT company_name AS US_companies, country FROM global_top
WHERE country = 'USA';

-- task11
SELECT company_name AS US_companies, country FROM global_top
WHERE country <> 'USA';

-- task12
SELECT company_name, rank, previous_rank FROM global_top
WHERE rank = previous_rank;

-- task13
SELECT company_name, profits FROM us_top
WHERE profits > 15000;

-- task14
SELECT company_name FROM us_top
WHERE rank_us % 2 = 0;

-- task15
SELECT company_name FROM us_top
WHERE rank_us < previous_rank;
