To run the project clone the repository with the command below
```sh
git clone https://github.com/KatePril/docker-compose-demo.git
```
Navigate to the project directory:
```sh
cd docker-compose-demo
```
Run the project:
```sh
docker-compose up --build
```

Select data from database:
```sh
docker exec -it postgres_db psql -U postgres -d test_db -c "SELECT * FROM contacts"
```
