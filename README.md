# alexandria-catalogs
Decomposed microservice for only catalogs service

# Run/Set-up
```console
docker build -t local/alexandria-catalogs:1.0.001 . --no-cache
```

# Goal/Objective

We would be spinning up the Books Service and its related dependencies here:

```console
docker-compose up
```

1. You may check the API documentation by hitting http://localhost:9002/docs from your browser
2. It takes the port number 9002 configured in the Dockerfile.




# Below are the services currently available

Catalog APIs
1. Create New Catalog: "/api/catalogs/local"
2. Add a book to catalog: "/api/catalogs/local/name/{catalog_name}/{book_id}"
3. Get Catalog Details using name:"/api/catalogs/local/name/{catalog_name}"
4. Get All Books of a Catalog: "/api/catalogs/local/books"
5. Delete a Catalog by name: "/api/catalogs/local/name/{catalog_name}"
6. Get all Catalogs : "/api/catalogs/local/all"


# Tips for implementing a new service
1. Add URL Path in the **urls.py**
2. Tag the URL path in an annotation of respective api definition in **main.py**
3. Implement DB operation ( any of CURD operations ) in **database.py** if required
4. Call the above implemented DB operation in api definition of  **main.py**


# License
Please refer to the LICENSE