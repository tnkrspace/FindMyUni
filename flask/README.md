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
    "filters": [
      {
        "filter": {
          "key": "name",
          "value": [
            "Waterloo",
            "Stanford"
          ],
          "operator": "OR"
        }
      },
      {
        "filter": {
          "key": "alpha_two_code",
          "value": [
            "US",
            "CA"
          ],
          "operator": "OR"
        }
      },
      {
        "filter": {
          "key": "domain",
          "value": [
            "ca"
          ],
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
