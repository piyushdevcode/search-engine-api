# DuckDuckgo Search API

### Django Rest Framework Application to expose an endpoint for duckduckgo search having rate limit of 5 API calls per min

## How To Run

### 1. Clone Repository

```sh
git clone https://github.com/piyushdevcode/search-engine-api
```

### 2. Setup virtual environment and install requirements

```sh
pip install -r requirements.txt
```

### 3. install the required browser
```sh
playwright install chromium
```

### 4. Run command
```sh
python manage.py makemigrations & python manage.py migrate
```

### 5. Start Server
```sh
python manage.py runserver
```

# To run tests

### in the base directory run command
```sh
python manage.py test
```

# API

### API URL - http://localhost:8000/api/ducksearch
#### parameters accepted 

- query: the query to get search results for.
    - Example URL : http://localhost:8000/api/ducksearch?query=latest+news
 
- pages: [optional] specify no of pages to scrape
    -   Example URL : http://localhost:8000/api/ducksearch?query=latest+news&pages=2

| End Point                        | HTTP Method | Result                                                   | Accessible by | Browsable API URL Examples|
| -------------------------------- | ----------- | -------------------------------------------------------- | ------------- | ------ |
| `ducksearch/`                         | GET        | get the search results for given query                         | Anyone        | [example](http://localhost:8000/api/ducksearch?query=latest+news)|
