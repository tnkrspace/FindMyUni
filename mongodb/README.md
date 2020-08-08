# FindMyUni MongoDB
This is an overview of the MongoDB collections that persist the application data.

## Introduction
This is a lightweight project with two collections and limited keys.

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
