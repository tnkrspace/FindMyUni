# FindMyUni Python Application
This is an overview of the Python application that is at the core of this project.

## Introduction
This Python project forms the API backend written with help of Flask.

## Usage
### POST ```/university/```
This is for creating a new University in the database.
#### Request
```json
[
    {
        "alpha_two_code": "US",
        "country": "United States",
        "domain": "acu.edu",
        "name": "Abilene Christian University",
        "web_page": "http://www.acu.edu/"
    },
    {
        "alpha_two_code": "CA",
        "country": "Canada",
        "domain": "uwaterloo.ca",
        "name": "University of Waterloo",
        "web_page": "https://www.uwaterloo.ca/"
    }
]
```

#### Response
##### 200 OK
```json
[
    {
        "status": "University Added Successfully",
        "id": <identifier>,
        "alpha_two_code": "US",
        "country": "United States",
        "domain": "acu.edu",
        "name": "Abilene Christian University",
        "web_page": "http://www.acu.edu/"
    },
    {
        "status": "University Added Successfully",
        "id": <identifier>,
        "alpha_two_code": "CA",
        "country": "Canada",
        "domain": "uwaterloo.ca",
        "name": "University of Waterloo",
        "web_page": "https://www.uwaterloo.ca/"
    }
]
```
##### 400 Bad Request/404 Not Found/500 Server Error
```json
{
    "errors": [
        {
            "error": "Error Message"
        },
        {
            "error": "Error Message"
        }
    ]
}
```

### PUT ```/university/```
This is for updating the details for a university.

#### Request
```json
[
    {
        "id": <identifier>,
        "alpha_two_code": "US",
        "country": "United States",
        "domain": "acu.edu",
        "name": "Abilene Christian University",
        "web_page": "http://www.acu.edu/"
    },
    {
        "id": <identifier>,
        "alpha_two_code": "CA",
        "country": "Canada",
        "domain": "uwaterloo.ca",
        "name": "University of Waterloo",
        "web_page": "https://www.uwaterloo.ca/"
    }
]
```

#### Response
##### 200 OK
```json
[
    {
        "status": "University Updated Successfully",
        "id": <identifier>
    },
    {
        "status": "University Updated Successfully",
        "id": <identifier>
    }
]
```
##### 400 Bad Request/404 Not Found/500 Server Error
```json
{
    "errors": [
        {
            "error": "Error Message"
        },
        {
            "error": "Error Message"
        }
    ]
}
```

### GET ```/university/<identifier>```
This is to fetch details for a particular university.
#### Response
##### 200 OK
```json
{
        "id": <identifier>,
        "alpha_two_code": "CA",
        "country": "Canada",
        "domain": "uwaterloo.ca",
        "name": "University of Waterloo",
        "web_page": "https://www.uwaterloo.ca/"
}
```
##### 400 Bad Request/404 Not Found/500 Server Error
```json
{
    "errors": [
        {
            "error": "Error Message"
        },
        {
            "error": "Error Message"
        }
    ]
}
```

### DELETE ```/university/<identifier>```
This is to delete a particular university.
#### Response
##### 200 OK
```json
{
    "status": "University Deleted Successfully",
    "id": <identifier>,
    "alpha_two_code": "CA",
    "country": "Canada",
    "domain": "uwaterloo.ca",
    "name": "University of Waterloo",
    "web_page": "https://www.uwaterloo.ca/"
}
```
##### 400 Bad Request/404 Not Found/500 Server Error
```json
{
    "errors": [
        {
            "error": "Error Message"
        },
        {
            "error": "Error Message"
        }
    ]
}
```

### POST ```/university/search/```
This is the search filter API.
#### Request
```json
{
    "filterGroup": {
        "operator": "AND",
        [
            {
                "filter": {
                    "key": "name",
                    "value": ["Waterloo", "Stanford"],
                    "operator": "OR"
                }
            },
            {
                "filter": {
                    "key": "alpha_two_code",
                    "value": [ "US", "CA" ],
                    "operator": "OR"
                }
            },
            {
                "filter": {
                    "key": "domain",
                    "value": [ "ca" ],
                    "operator": "OR"
                }
            }
        ]
    }
}
```
#### Response
##### 200 OK
```json
[
    {
        "id": <identifier>,
        "alpha_two_code": "US",
        "country": "United States",
        "domain": "acu.edu",
        "name": "Abilene Christian University",
        "web_page": "http://www.acu.edu/"
    },
    {
        "id": <identifier>,
        "alpha_two_code": "CA",
        "country": "Canada",
        "domain": "uwaterloo.ca",
        "name": "University of Waterloo",
        "web_page": "https://www.uwaterloo.ca/"
    }
]
```
##### 400 Bad Request/404 Not Found/500 Server Error
```json
{
    "errors": [
        {
            "error": "Error Message"
        },
        {
            "error": "Error Message"
        }
    ]
}
```
