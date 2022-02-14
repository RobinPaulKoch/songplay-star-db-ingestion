# Short Description
A Postgres + Python example of ingesting sample data into tables forming a starschema. _(This project is a assignment project from the Udacity Data Engineer nanodegree program)_

## Installation guide
### Cloning and downloading the dependencies
Cloning the repository
```
git clone https://github.com/RobinPaulKoch/songplay-star-db-ingestion.git
```
Dependencies can be easily installed by using the pipenv package to install the pipfile while standing in the root of the project folder.
```
pipenv install
```
### Setting up postgres locally
This project assumes a locally installed postgres server to be available and active. 
For downloading the latest version of postgres visit https://www.postgresql.org/download/
The etl.py and create_tables.py modules make use of psycopg2 to connect to the local database. To interact with the database, you need to add two variables to your system path variables

```
"postgres_user" = <your local postgres user that has access to the database>
"postgres_password" = <the password to connect to the database with the user>
```

## Purpose of the project
The goal of this ingestion module is to ingest json files to create a data model which the user "Sparkify" can use to query and analyze data. The data model consists of songs and logs of the songs being listened to. Examples of use cases of the data model are analyzing which songs or artists are listened to the most and by which users.

## Running the ingestion modules
Ingestion is simple and is for now manually implemented. In case of new incoming files, time triggers could be implemented (for example).

Manually, running sequentially the create_tables.py and afterwards etl.py will initialize the database and the tables and process the json files in the data respectively.
Running the .py files is easy from any terminal or IDE with interactive python debugging capabilities.

```
python create_tables.py
python etl.py
```

## Files in the repository
Firstly, example data is included in the repository in the "data" directory. The data directory contains two types of data:
1. log_data
2. song_data

log_data includes data which is ingested in the "songsplays" fact table. log_data also contains

Moreover, the repository contains two functional files which should can be executed to initialize and process the data:
1. create_tables.py
2. etl.py

Besides there are jupyter notebook files with the following purposes:
1. etl.ipynb: provides a per command insight into the ingestion process of the different tables and etl
2. test.ipynb: connects to the database and runs some example queries

Finally there is the pipfile and the pipfile.lock which facilitate npm-like dependency installation for Python as discussed before.

