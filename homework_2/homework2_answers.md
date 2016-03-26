# Homework 2 Answers

###Jade Tabony


**1) Look at the head and the tail of chipotle.tsv in the data subdirectory of this repo. Think for a minute about how the data is structured. What do you think each column means? What do you think each row means? Tell me! (If you're unsure, look at more of the file contents.)** 

The data is structured in a Tab seperated value file, which is comprised of columns that are seperated by tabs. 

`Jades-MacBook-Air:data Jade$ head chipotle.tsv*`

Column name and assessment:

|Column Name | What I think it means|
|------------|----------------------|
|order-id| Id number assigned to the sale.  There may be multiple items per sale and therefore, multiple rows for per order-id|
|quantity| The quantity of the following item purchased for this specific sale number|
|item_name |Name of the item sold|
|choice_description|Additional descriptor for the item sold (optional)|
|item_price| Price of the item sold|



**2) How many orders do there appear to be?**

`Jades-MacBook-Air:data Jade$ tail chipotle.tsv*`
 
	1831	1	Carnitas Bowl	[Fresh Tomato Salsa, [Fajita Vegetables, Rice, Black Beans, Cheese, Sour Cream, Lettuce]]	$9.25 
	1831	1	Chips	NULL	$2.15 
	1831	1	Bottled Water	NULL	$1.50 
	1832	1	Chicken Soft Tacos	[Fresh Tomato Salsa, [Rice, Cheese, Sour Cream]]	$8.75 
	1832	1	Chips and Guacamole	NULL	$4.45 
	1833	1	Steak Burrito	[Fresh Tomato Salsa, [Rice, Black Beans, Sour Cream, Cheese, Lettuce, Guacamole]]	$11.75 
	1833	1	Steak Burrito	[Fresh Tomato Salsa, [Rice, Sour Cream, Cheese, Lettuce, Guacamole]]	$11.75 
	1834	1	Chicken Salad Bowl	[Fresh Tomato Salsa, [Fajita Vegetables, Pinto Beans, Guacamole, Lettuce]]	$11.25 
	1834	1	Chicken Salad Bowl	[Fresh Tomato Salsa, [Fajita Vegetables, Lettuce]]	$8.75 
	1834	1	Chicken Salad Bowl	[Fresh Tomato Salsa, [Fajita Vegetables, Pinto Beans, Lettuce]]	$8.75 


Based on the the descending order of order-ids, there were 1834 orders

**3)How many lines are in this file?**

`Jades-MacBook-Air:data Jade$ wc -l chipotle.tsv`

    4623 chipotle.tsv
    
There are 4623 lines in this file.

**4) Which burrito is more popular, steak or chicken?**

`Jades-MacBook-Air:data Jade$ git grep -c 'Chicken Burrito'  chipotle.tsv`

	chipotle.tsv:553

`Jades-MacBook-Air:data Jade$ git grep -c 'Steak Burrito'  chipotle.tsv`

	chipotle.tsv:368
	
Chicken burritos are more popular in this sample.

**5) Do chicken burritos more often have black beans or pinto beans?**

`Jades-MacBook-Air:data Jade$ git grep 'Chicken Burrito'  chipotle.tsv | grep -c 'Black Beans'`
  
	282

`Jades-MacBook-Air:data Jade$ git grep 'Chicken Burrito'  chipotle.tsv | grep -c 'Pinto Beans'`
  
	105

Black beans are more common in chicken burritos in this sample.


**6) Make a list of all of the CSV or TSV files in the GA-SEA-DAT1 repo (using a single command). You will be working on your local repo on your laptop. Think about how wildcard characters can help you with this task.**

`Jades-MacBook-Air:GA-SEA-DAT2 Jade$ git ls-files | grep '.csv\|.tsv'`

	data/Airline_on_time_west_coast.csv
	data/NBA_players_2015.csv
	data/airlines.csv
	data/bank-additional.csv
	data/bikeshare.csv
	data/chipotle.tsv
	data/citibike_feb2014.csv
	data/drinks.csv
	data/drones.csv
	data/hitters.csv
	data/icecream.csv
	data/imdb_1000.csv
	data/mtcars.csv
	data/ozone.csv
	data/pronto_cycle_share/2015_station_data.csv
	data/pronto_cycle_share/2015_trip_data.csv
	data/pronto_cycle_share/2015_weather_data.csv
	data/sms.tsv
	data/syria.csv
	data/titanic.csv
	data/ufo.csv
	data/vehicles_test.csv
	data/vehicles_train.csv
	data/yelp.csv

To count the number of files listed.
	
`Jades-MacBook-Air:data Jade$ git ls-files | grep -c '.csv\|.tsv'`

	24

*Note, I ended up feeling like I didn't really need the wildcard (though I understand their purpose) in this method.*

**7) Count the approximate number of occurrences of the word "dictionary" (regardless of case) across all files in the GA-SEA-DAT1 repo.**

I ended up using two lines, just to verify my findings.  The first line of code showed the approximate number of instances of the string dictionary in each file.  The second counted them.

`Jades-MacBook-Air:GA-SEA-DAT2 Jade$ git grep -i -c dictionary .`

	README.md:17
	code/00_file_reading.py:1
	code/00_python_intermediate_workshop.py:6
	code/05_api.py:2
	code/05_web_scraping.py:3
	code/05_web_scraping_RH_edits.py:3
	code/99_pandas.py:2
	code/solutions/00_python_intermediate_workshop_with_answers.py:6
	code/solutions/03_file_reading_full_code_and_solutions.py:1
	code/solutions/03_file_reading_with_code_along_code.py:1
	code/solutions/04_pandas_with_all_answers.py:2
	code/solutions/07_api_census_with_answers.py:1
	data/sms.tsv:4
	data/yelp.csv:1
	data/yelp.json:1
	homework/03_python_homework_chipotle.py:1
	homework/04_command_line_chipotle.md:1
	homework/10_yelp_votes_homework.ipynb:1
	homework/solutions/02_command_line_chipotle_solution.md:4
	homework/solutions/04_python_homework_chipotle_with_answers.py:4
	notebooks/.ipynb_checkpoints/03_correlation_exercise_ice_cream_and_car_data-checkpoint.ipynb:2
	notebooks/.ipynb_checkpoints/03_correlation_exercise_ice_cream_and_car_data_with_solution-checkpoint.ipynb:2
	notebooks/.ipynb_checkpoints/15_bikeshare_exercise-checkpoint.ipynb:1
	notebooks/03_correlation_exercise_ice_cream_and_car_data.ipynb:2
	notebooks/10_titanic_confusion.ipynb:1
	notebooks/13_natural_language_processing.ipynb:2
	notebooks/15_bikeshare_exercise.ipynb:1
	notebooks/16_ensembling.ipynb:1
	other/python_reference:9
	project/README.md:1

`Jades-MacBook-Air:GA-SEA-DAT2 Jade$ git grep  dictionary . | wc -l`

      84


**8) Optional: Use the the command line to discover something "interesting" about the Chipotle data. Try using the commands from the "advanced" section!**

I ended up using all of the commands in the advanced section but that produced a large amount of output so I'm not going to repost here. 