# mugna_rickandmorty
Rick and morty database

Simple Rick and Morty database with simple CRUD functionalities.

Some of the frameworks/tools used in the development of this system are:
  * Django3.0
  * Bootstrap
  * PostgresQL

##### you can use pipenv or virtualenv since requirements.txt is provided. pipenv is recommended.

### Setup: 
1. Create *.env* file according to *.env.example*.
2. run the following commands on your terminal
  * `pipenv install` or `pip install -r requirements.txt` if running on virtualenv.
  * `py manage.py makemigrations`
  * `py manage.py migrate`
3. To initialize tables and download character avatar/images, run: `py manage.py summon`
