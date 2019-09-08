+ [Create a Contractor Request](#create_contractor)



# <a name="create_contractor"></a>Create a Contractor
`https://fixup-backend.herokuapp.com/api/v1/contractors/`

A POST request to `/api/v1/contractors/` takes a body with an object of keys:
* `"name":`
* `"email":`
* `"phone_number":`
* `"zip":`
* `"category":`
* `"logo":`

Example Request
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
Example Response
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


# <a name="create_contractor"></a>Create a Contractor
`https://fixup-backend.herokuapp.com/api/v1/contractors/`

A POST request to `/api/v1/contractors/` takes a body with an object of keys:
* `"name":`
* `"email":`
* `"phone_number":`
* `"zip":`
* `"category":`
* `"logo":`

Example Request
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
Example Response
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
