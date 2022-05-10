# Uplift - Assessment

### Set Up App

Once app is cloned from Github and virtual environment activated:

    1. Install requirements (*pip install -r requirements.txt*)
    2. Start Docker on desktop
    3. Run Docker containers for pgadmin and postgres from terminal: (*docker compose up -d*)
    4. Open pgadmin container in browser and log in (login: *admin@admin.com* password: *root*)
    5. Connect server using postgres container ID
        -obtain container ID in terminal (*docker ps*)
        -name database
        -under connection(host name = *postgres container ID*, user=*root*, password=*root*)
    6. Create tables
        -Use create_tables.sql to create table in pgadmin via QueryEditor
    7. Seed database
        -run seed.py file

### Interacting with database

To use HTML Rendering to interact with database and obtain query results:

    1. Run matchapp.py to open Flask webservice
    2. Open local host link provided in terminal (Press CRTL+C to quit when completed with webservice)
        -if prefer to open in debug status, uncomment app.debug=True in matchingapp.py file

### Test
    1. Use terminal to run pytest
    2. test_home.py creates client app for testing
        -tests for html index rendering

### Closing App
    1. Close Docker (*docker compose down* if deleting containers)
    2. Deactivate virtual environment


