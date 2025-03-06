```shell
docker-compose up --build
```

```sh
docker exec -it postgres_db psql -U postgres -d test_db -c "SELECT * FROM contacts"
```
