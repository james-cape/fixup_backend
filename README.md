+ [Create a User](#create_user)
+ [Create a Contractor](#create_contractor)
+ [Create a Project](#create_project)




# <a name="create_user"></a>Create a User
`https://fixup-backend.herokuapp.com/api/v1/users/`

A POST request to `/api/v1/users/` takes a body with an object of keys:
* `"full_name":`
* `"email":`
* `"phone_number":`
* `"zip":`

Example Request:
```
POST https://fixup-backend.herokuapp.com/api/v1/users/

Body; raw, JSON(application/json):
{
	"full_name": "user_1_name",
	"email": "user_1_email@email.com",
	"phone_number": "3333333",
	"zip": "98765"
}
```

Example Response:
```
Status: 201 Created
{
    "full_name": "user_1_name",
    "email": "user_1_email@email.com",
    "phone_number": "3333333",
    "zip": "98765"
}
```


# <a name="create_contractor"></a>Create a Contractor
`https://fixup-backend.herokuapp.com/api/v1/contractors/`

A POST request to `/api/v1/contractors/` takes a body with an object of keys:
* `"name":`
* `"email":`
* `"phone_number":`
* `"zip":`
* `"category":`
* `"logo":`

Example Request:
```
POST https://fixup-backend.herokuapp.com/api/v1/contractors/

Body; raw, JSON(application/json):
{
  "name": "Builder Bob",
  "email": "test@mail.com",
  "phone_number": "111111111",
  "zip": "80124",
  "category": "construction",
  "logo": "logo.jpg"
}
```

Example Response:
```
Status: 201 Created
{
    "name": "Builder Bob",
    "email": "test@mail.com",
    "phone_number": "111111111",
    "zip": "80124",
    "category": "construction",
    "logo": "logo.jpg"
}
```


# <a name="create_project"></a>Create a Project
`https://fixup-backend.herokuapp.com/api/v1/users/1/projects`

A POST request to `/api/v1/users/1/projects` takes a body with an object of keys:
* `"title":`
* `"description":`
* `"category":`
* `"user_before_picture":`

Example Request:
```
POST https://fixup-backend.herokuapp.com/api/v1/users/1/projects

Body; raw, JSON(application/json):
{
	"title": "newly uploaded project",
	"description": "this is the third project",
	"category": "plumbing",
	"user_before_picture": "picture.png"
}
```

Example Response:
```
Status: 201 Created
{
    "user_id": 1,
    "project": {
        "title": "newly uploaded project",
        "description": "this is the third project",
        "picture": "picture.png"
    }
}
```
