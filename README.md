# QA-Challenge

Even in the world of startups and company builders expenses for trips etc. have to be filed and managed.
The fictitious expense software Cashcog tries to manage this. The following challenge depicts a first version of this software and outlines only the user creation process.

For this purpose the Cashcog system provides a `GraphQL-API` and a `web interface`.

<br>

## 🚀 Getting started

In order to run the provided application, please make sure you have `docker` and `docker-compose` installed on your system.

<br>

### 📟 Running the GraphQL-API

Execute the following commands inside the `cashcog-be` folder.

`Build` the backend application:

```bash
docker-compose -f docker-compose.yml -f docker-compose.app.yml build
```

`Run` the backend application:

```bash
docker-compose -f docker-compose.yml -f docker-compose.app.yml up
```

`Inspect` the API using GraphiQL in your browser:

```bash
http://localhost:8080/graphql
```
<br>

### 📰 Running the Web-App

Execute the following commands inside the `cashcog-fe` folder.


`Build` the frontend application:

```bash
docker-compose -f docker-compose.yml build
```

`Run` the frontend application:

```bash
docker-compose -f docker-compose.yml up -d
```

`Open` the url in your browser:

```bash
http://localhost:80
```

<br>

## 🔧 Additional tools

The Cashcog system uses a `Postgres` database. In order to help you to inspect the data stored there the software `PgAdmin` is installed and running alongside the backend application.

You can `access` this tool in your browser as follows:

```bash
http://localhost:8081
```

`Credentials` to log into PgAdmin:

```bash
email: qa@xcnt.io
password: postgres
```

Database password:

```bash
database-password: postgres
```

