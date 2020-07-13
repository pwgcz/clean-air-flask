# Clean Air
## Purpose
Purpose of this web-app is to store data from government api http://www.gios.gov.pl/pl/ about quality of air in Poland. Every hour app send request to government api and update database. Stored data are displayed on webside where you can choose station from map and show information about every parameter displayed on graphs.

### Example of use
#### Welcome window
![Screenshot from 2020-07-07 10-28-01](https://user-images.githubusercontent.com/62465226/86748187-9181e000-c03c-11ea-9433-83bfe9a2ac6b.png)

### Selected station
![Screenshot from 2020-07-07 10-25-24](https://user-images.githubusercontent.com/62465226/86747880-5b446080-c03c-11ea-8a10-73d8288a5885.png)
## Installing locally(only for linux/unix user)
### Back-end
1. Create virtual virtual env using command- ```python3 -m venv venv``` ``` then run python script ```initial_load.py``` to populate database with  data, script ```periodic_load_measurement.py``` when run will populate database every hour with current data. To start back-end go to project directory and run command  -```yarn start-api```
2. Activate virtual env using command- ```. env/bin/activate``` 
3. Install dependency from file requirements-dev.txt using command- ```pip install -r requirements-dev.txt``` 
4. Run migration file using command- ```flask db upgrade``` 
5. Run initial_load.py file to populate database with current data from past 3 days 
* Back-end is ready to use. To start backend api that connect to database use command - ```yarn start-api``` 

### Front-end

1. Install dependency from package.json file using command-  ``` npm install``` 
* Front-end is ready to use. To start frontend app use command- ```yarn start``` 

## WIP
* Deploying app on Heroku
* Make app responsive
