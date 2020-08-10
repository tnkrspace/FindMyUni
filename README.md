# FindMyUni 
[[ https://github.com/tnkrspace/FindMyUni ]]
- FindMyUni is a search platform for students, parents and counsillor alike to find a University best suited to their needs, means and expectations
- FindMyUni is part of a programming assignment for a job opportunity at Azent Overseas Education

## Introduction
This Python project is a simple web application that allows users to create an account(TO DO), search for universities and bookmark them for later(TO DO).
There is also an admin user with greater access to data through APIs.

## Architecture
- We have a production-ready project with multiple APIs for the backend with help of Flask and various extensions
- We have MongoDB to persist the data in collections
- We have ElasticSearch implemented for indexing data on the fly (using signals from mongoengine) and using fuzzy search with filters to query universities

## Future Tasks
- Implement Authentication and Authorization using Bcrypt and Session Management
- Implement Logging
- Implement ELK for system and application monitoring, logging and reporting
- Implement Load Balancing with Nginx
- Implement Application Clustering
- Implement Database Clustering
- Implement ElasticSearch Clustering

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
  "query": {
    "bool": {
      "should": [
        {
          "fuzzy": {
            "name": "Waterloo"
          }
        },
        {
          "fuzzy": {
            "name": "Stanford"
          }
        }
      ],
      "filter": [
        {
          "bool": {
            "must": [
              {
                "bool": {
                  "should": [
                    {
                      "match": {
                        "alpha_two_code": "US"
                      }
                    },
                    {
                      "match": {
                        "alpha_two_code": "CA"
                      }
                    }
                  ]
                }
              },
              {
                "bool": {
                  "should": [
                    {
                      "match": {
                        "domain": "ca"
                      }
                    }
                  ]
                }
              }
            ]
          }
        }
      ]
    }
  },
  'from': 10,
  'size': 10
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

### POST ```/user/```
This is to create a new user.
#### Request
```json
[
    {
        "name": "user"
    }
]
```
#### Response
##### 200 OK
```json
[
    {
        "status": "User Added Successfully",
        "user_id": <identifier>,
        "name": "user",
        "uni_tracker": []
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

### PUT ```/user/```
This is to update the user. This is also used to add universities to the user's tracker.
#### Request
```json
[
    {
        "user_id": <identifier>,
        "name": "user",
        "uni_tracker": [ <identifer>, <identifier> ]
    }
]
```
#### Response
##### 200 OK
```json
[
    {
        "status": "User Updated Successfully",
        "user_id": <identifier>,
        "name": "user",
        "uni_tracker": [ <identifer>, <identifier> ]
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

### GET ```/user/<user_id>```
This is to fetch a particular user.
#### Response
##### 200 OK
```json
[
    {
        "user_id": <identifier>,
        "name": "user",
        "uni_tracker": [ <identifer>, <identifier> ]
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

### DELETE ```/user/<user_id>```
This is to delete a particular user.
#### Response
##### 200 OK
```json
[
    {
        "status": "User Deleted Successfully",
        "user_id": <identifier>,
        "name": "user",
        "uni_tracker": [ <identifer>, <identifier> ]
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

### POST ```/user/role/```
This is to change the role of a user from normal user to admin or vice-a-versa. We are using a separate API to do this to prevent an outside entity from knowning about this.
#### Request
```json
{
    "user_id": <identifier>,
    "role": "admin"
}
```
#### Response
##### 200 OK
```json
{
    "status": "User Role Updated",
    "user_id": <identifier>,
    "role": "admin"
}
```
##### 403 Forbidden
```json
{
    "errors": [
        {
            "error": "Unauthorized Access"
        }
    ]
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

### POST ```/user/login/```
This is to authenticate the user.
#### Request
```json
{
    "email": "test@test.com",
    "user_pass": "tnkrspace"
}
```
#### Response
##### 200 OK
```json
{
    "status": "Login Successful",
    "user_id": <identifier>
}
```
##### 401 Unauthorized
```json
{
    "errors": [
        {
            "error": "Login Failed"
        }
    ]
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

### PUT ```/user/login```
This is to update user login details.
#### Request
```json
{
    "user_id": <identifier>,
    "email": "test@test.org",
    "user_pass": "azentoverseaseducation"
}
```
#### Response
##### 200 OK
```json
{
    "status": "Login Updated",
    "user_id": <identifier>
}
```
##### 401 Unauthorized
```json
{
    "errors": [
        {
            "error": "Login Failed"
        }
    ]
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

## Collections
### University
```json
{
    "id": <identifier>,
    "alpha_two_code": "US",
    "country": "United States",
    "domain": "acu.edu",
    "name": "Abilene Christian University",
    "web_page": "http://www.acu.edu/"
}
```

### User
```json
{
    "user_id": <identifier>,
    "email": "admin@admin.com",
    "name": "admin",
    "role": "admin",
    "last_login": <Date>,
    "uni_tracker": [ <identifier>, <identifier> ]
},
{
    "user_id": <identifier>,
    "email": "user@user.com",
    "name": "user",
    "role": "user",
    "last_login": <Date>,
    "uni_tracker": [ <identifier>, <identifier> ]
}
```

### User_Password
```json
{
   "user_id": <identifier>,
   "hash": "$2b$10$69SrwAoAUNC5F.gtLEvrNON6VQ5EX89vNqLEqU655Oy9PeT/HRM/a",
   "last_pass_change": <Date>
}
```
