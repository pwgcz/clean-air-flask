# Clean Air
## Purpose
Purpose of this web-app is to store data from government api http://www.gios.gov.pl/pl/ about quality of air in Poland. Every hour app send request to government api and update database. Stored data are displayed on webside where you can choose station from map and show information about every parameter displayed on graphs.

### Example of use
#### Welcome window
![Screenshot from 2020-07-07 10-28-01](https://user-images.githubusercontent.com/62465226/86748187-9181e000-c03c-11ea-9433-83bfe9a2ac6b.png)

### Selected station
![Screenshot from 2020-07-07 10-25-24](https://user-images.githubusercontent.com/62465226/86747880-5b446080-c03c-11ea-8a10-73d8288a5885.png)
## Installing locally
### Back-end

Opne api directory in terminal, activate virtual env and install dependency and necessary modules from ```requirements.txt``` file using ```pip install -r requirements.txt```. Run migration file using ```flask db upgrade ``` then run python script ```initial_load.py``` to populate database with  data, script ```periodic_load_measurement.py``` when run will populate database every hour with current data. To start back-end go to project directory and run command  -```yarn start-api```

### Fron-end

Opne api directory in terminal, install all dependency and necessary modules from file ```package.json```, to start front-end run command -```yarn start```
Open api directory in terminal, activate vitruale env and inatall dependency and necessary modules from ```requirements.txt``` file using ```pip install -r requirements.txt```. Run migration file using ```flask db upgrade ``` then run python script ```initial_load.py``` to pupulate database with  data, script ```periodic_load_measurement.py``` when run will populate database every hour with current data. To start back-end go to project directory and run command  -```yarn start-api```

### Fron-end
Open api directory in terminal, install all dependency and necessary modules from file ```package.json```, to start front-end run command -```yarn start```


## WIP
* Deploying app on Heroku
* Make app responsive
