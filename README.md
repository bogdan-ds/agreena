# Agreena technical case

## Introduction

This is a technical case for Agreena. In order to complete the task, I leveraged the FastAPI framework to create a RESTful API.
Once the service is run, the API documentation can be found at http://localhost:8000/docs. 

In order to retrieve a visual representation of the Sentinel data for the given geo bounding box, I used the API method
to retrieve a quick look image. The latest image for any given bounding box is retrieved and displayed.

Testing is done using `pytest`. End to end/acceptance tests are separated in the file `tests/end2end.py`, an additional 
pytest plugin is used: `pytest-dependency` to ensure that the tests are run in the correct order.

Refer to the section Testing for more information on how to run the tests.

## Installation

### Local

```bash
python3 -m venv /path/to/new/virtual/environment
source /path/to/new/virtual/environment/bin/activate
pip install -r requirements.txt
uvicorn src.main:app --reload
```

### Docker

```bash
docker build -t agreena .
docker run -d -p 8000:8000 --name agreenacontainer agreena
```


## Testing

Once the service is executed either in Docker or locally, the tests can be run using the following command:

```bash
pytest
```

Note that `pytest` and `pytest-dependency` are required to run the tests.