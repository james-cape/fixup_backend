
# Welcome to Fix Up Backend!
This project makes it easy for property owners to connect with contractors for whatever problems they may have. Property owners just upload a picture, and contractors swipe left or right on those pictures depending on if they are interested in the job. If there's a connection between both parties, they'll get fixed up with each other's information!

## Introduction
This is a [cross-pollination project](https://backend.turing.io/module4/projects/cross_pollination/cross_pollination_spec) between two back-end and two front-end students at [Turing School of Software and Design](https://turing.io/).

#### Front-End Team
[Steve Rumizen](https://github.com/rumizen)

[Antonio Fry](https://github.com/AntonioFry)

[Front End Repository](https://github.com/rumizen/FixUp-fe)

#### Back-End Team
[James Cape](https://github.com/james-cape)

[Trevor Nodland](https://github.com/tnodland)

[Back End Repository](https://github.com/james-cape/fixup_backend)

#### Deployed Links
Back-End: https://fixup-backend.herokuapp.com/

Front-End: https://expo.io/@rumizen/FixUp

#### Learning Goals
* Demonstrate our development at Turing via a final group project before graduation
* Create an application from a raw idea to an MVP (minimum viable product)
* Break problems and responsibilities down into digestible pieces for each front-end/back-end team
* Implement a new technology (Python/Django for the back-end)
* Implement a new technology (React Native for the front-end)
* Focus on back-end/front-end communication and detailed documentation for each endpoint
* Practice written technical communication with concise, consistent git commits and clear pull requests
* Clearly document Introduction, Initial Setup, How to Use, Known Issues, Running Tests, How to Contribute, Core Contributors, Schema Design, and Tech Stack List

#### Future Iterations
Future iterations of this project will include:
* Fully built-out user login
* Full sad-path testing and accountability
* Location-based recommendations
* More lock-down on contractor contact information to keep anonymity until a match
* In-app communication in place of contact information
* Payment gates for contractors, such as to send a message to a match

## Local Setup

If you'd like to run this app locally, pull down this repo and run the following commands:

#### Dependencies
[Python 3.7.4](https://www.python.org/downloads/release/python-374/)

[Django 2.2.5](https://docs.djangoproject.com/en/2.2/releases/2.2.5/)

[Django Rest Framework](https://www.django-rest-framework.org)

#### Commands
Set up environment:
```
$ python3 -m venv env
$ source venv/bin/activate
```

Install dependencies:
```
$ pip3 install django
$ pip3 install djangorestframework
```

Lock dependency versions:
```
$ pip3 install -r requirements.txt
```

Set up database:
```
$ psql
$ CREATE DATABASE fixup_development;
$ CREATE USER (any username) WITH PASSWORD (any password);
$ GRANT ALL PRIVILEGES ON DATABASE fixup_development TO (the username you chose);
$ \q
$ export(DB_NAME, fixup_development)
$ export(DB_USER, (username you chose))
$ export(DB_PASSWORD, (password you chose))
$ python3 manage.py migrate
```

Testing:
```
python3 manage.py test
```

## Schema
![Schema](https://i.ibb.co/L5YTqjX/fixupschema.png "Fix Up Schema")

## Endpoints Available

+ [Create a User](#create_user)
+ [Update a User](#update_user)
+ [Create a Contractor](#create_contractor)
+ [See a single Contractor](#see_a_single_contractor)
+ [Update a Contractor](#update_contractor)
+ [Create a Project](#create_project)
+ [See User Show](#see_user_show)
+ [See Project Show](#see_project_show)
+ [Update a Project](#update_a_project)
+ [See Projects By User](#see_projects_by_user)
+ [See Projects By Contractor](#see_projects_by_contractor)
+ [Get Batch of Projects via Contractor ID](#get_batch_of_projects_via_contractor_id)
+ [Get Project Suggestions via Contractor ID](#get_project_suggestions_via_contractor_id)
+ [Swiping Updates Contractor Choice](#swiping_updates_contractor_choice)
+ [User Selects Contractor](#update_user_choice)
+ [Contractor Sees Project For First Time](#update_seen_boolean)
+ [User Sees One of Their Projects](#single_user_project)


## <a name="create_user"></a>Create a User
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

## <a name="update_user"></a>Update a User
`https://fixup-backend.herokuapp.com/api/v1/users/1`

A PATCH request to `/api/v1/users/:id` which takes a body.

Example Request:
```
PATCH https://fixup-backend.herokuapp.com/api/v1/users/1

Body; raw, JSON(application/json):
{
    "full_name": "other_Princess",
    "email": "another_castle@mail.com"
}
```

Example Response:
```
Status: 200 OK
{
    "id": 1,
    "full_name": "other_Princess",
    "email": "another_castle@mail.com",
    "phone_number": "3035555555",
    "zip": "80555"
}
```


## <a name="create_contractor"></a>Create a Contractor
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


## <a name="see_a_single_contractor"></a>See a Single Contractor
`https://fixup-backend.herokuapp.com/api/v1/contractors/1`

A GET request to `/api/v1/contractors/:id` which takes no body.

Example Request:
```
GET https://fixup-backend.herokuapp.com/api/v1/contractors/1
```

Example Response:
```
Status: 200 OK
{
  "name": "new_name_1",
  "email": "new_plumbing@gmail.com",
  "phone_number": "7205555555",
  "zip": "80555",
  "category": "plumbing",
  "logo": "plumbinglogo.png"
}
```


## <a name="update_contractor"></a>Update a Contractor
`https://fixup-backend.herokuapp.com/api/v1/contractors/1`

A PATCH request to `/api/v1/contractors/:id` takes a body with an object of any combination or number of the following keys:
* `"name":`
* `"email":`
* `"phone_number":`
* `"zip":`
* `"category":`
* `"logo":`

Example Request:
```
PATCH https://fixup-backend.herokuapp.com/api/v1/contractors/1

Body; raw, JSON(application/json):
{
	"name": "new_name_1",
	"email": "new_plumbing@gmail.com"
}
```

Example Response:
```
Status: 200 OK
{
  "name": "new_name_1",
  "email": "new_plumbing@gmail.com",
  "phone_number": "7205555555",
  "zip": "80555",
  "category": "plumbing",
  "logo": "plumbinglogo.png"
}
```


## <a name="create_project"></a>Create a Project
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


## <a name="see_user_show"></a>See User Show
`https://fixup-backend.herokuapp.com/api/v1/users/1`

A GET request to `/api/v1/users/:id` which takes no body.

Example Request:
```
GET https://fixup-backend.herokuapp.com/api/v1/users/1
```

Example Response:
```
Status: 200 OK
{
  "full_name": "Mario Mario",
  "email": "jumpman@gmail.com",
  "phone_number": "3035555555",
  "zip": "80555"
}
```


## <a name="see_project_show"></a>See Project Show
`https://fixup-backend.herokuapp.com/api/v1/projects/1`

A GET request to `/api/v1/projects/:id` which takes no body.

Example Request:
```
GET https://fixup-backend.herokuapp.com/api/v1/projects/1
```

Example Response:
(See last element for an example of a user's project which a contractor has swiped right on)
```
Status: 200 OK
{
  "title": "Broken Pipe",
  "description": "A pipe in my bathroom is leaky",
  "category": "plumbing",
  "user_before_picture": "brokenpipe.png",
  "user_after_picture": null
}
```


## <a name="update_a_project"></a>Update a Project
`https://fixup-backend.herokuapp.com/api/v1/projects/1`

A PATCH request to `/api/v1/projects/:id` which takes a body.

Example Request:
```
PATCH https://fixup-backend.herokuapp.com/api/v1/projects/1
{
  "id": 1,
  "title": "I changed the title",
  "description": "I changed the description",
  "category": "plumbing",
  "user_before_picture": "brokenpipe.png",
  "user_after_picture": null
}
```

Example Response:
```
Status: 200 OK
{
  "title": "Broken Pipe",
  "description": "A pipe in my bathroom is leaky",
  "category": "plumbing",
  "user_before_picture": "brokenpipe.png",
  "user_after_picture": null
}
```


## <a name="see_projects_by_user"></a>See Projects By User
`https://fixup-backend.herokuapp.com/api/v1/users/1/projects`

A GET request to `/api/v1/users/:id/projects` which takes no body.

Example Request:
```
GET https://fixup-backend.herokuapp.com/api/v1/users/1/projects
```

Example Response:
(See last element for an example of a user's project which a contractor has swiped right on)
```
Status: 200 OK
[
  {
    "id": 5,
    "title": "Broken Pipe",
    "description": "A pipe in my bathroom is leaky",
    "category": "plumbing",
    "user_before_picture": "brokenpipe.png",
    "user_after_picture": null,
    "contractors": []
  },
  {
    "id": 4,
    "title": "Broken Pipe",
    "description": "A pipe in my bathroom is leaky",
    "category": "plumbing",
    "user_before_picture": "brokenpipe.png",
    "user_after_picture": null,
    "contractors": []
  },
  {
    "id": 1,
    "title": "Broken Pipe",
    "description": "A pipe in my bathroom is leaky",
    "category": "plumbing",
    "user_before_picture": "brokenpipe.png",
    "user_after_picture": null,
    "contractors": [
      {
        "contractor_id": 1,
        "picture_1": "",
        "picture_2": ""
      }
    ]
  }
]
```


## <a name="see_projects_by_contractor"></a>See Projects By Contractor
`https://fixup-backend.herokuapp.com/api/v1/contractors/1/projects`

A GET request to `/api/v1/contractors/:id/projects` which takes no body.

Results are only returned if `user_choice = True` (contractor swiped right and customer chose )

Example Request:
```
GET https://fixup-backend.herokuapp.com/api/v1/contractors/1/projects
```

Example Response:
```
Status: 200 OK
[
	{
		"project": {
			"id": 1,
			"title": "Broken Pipe",
			"description": "A pipe in my bathroom is leaky",
			"category": "plumbing",
			"user_before_picture": "brokenpipe.png",
			"user_after_picture": null
		},
		"seen": false
	},
	{
		"project": {
			"id": 1,
			"title": "Broken Pipe",
			"description": "A pipe in my bathroom is leaky",
			"category": "plumbing",
			"user_before_picture": "brokenpipe.png",
			"user_after_picture": null
		},
		"seen": false
	},
]
```


## <a name="get_batch_of_projects_via_contractor_id"></a>Get Batch of Projects via Contractor ID
`https://fixup-backend.herokuapp.com/api/v1/projects?contractor_id=6`

A GET request to `/api/v1/contractors/:id/projects?contractor_id=:id` which takes no body.

Example Request:
```
GET https://fixup-backend.herokuapp.com/api/v1/projects?contractor_id=6
```

Example Response:
```
Status: 200 OK
[
  {
    "title": "Broken Pipe",
    "description": "A pipe in my bathroom is leaky",
    "category": "plumbing",
    "user_before_picture": "brokenpipe.png",
    "user_after_picture": null
  },
  {
    "title": "Broken Pipe",
    "description": "A pipe in my bathroom is leaky",
    "category": "plumbing",
    "user_before_picture": "brokenpipe.png",
    "user_after_picture": null
  },
  {
    "title": "Broken Pipe",
    "description": "A pipe in my bathroom is leaky",
    "category": "plumbing",
    "user_before_picture": "brokenpipe.png",
    "user_after_picture": null
  },
  {
    "title": "Broken Pipe",
    "description": "A pipe in my bathroom is leaky",
    "category": "plumbing",
    "user_before_picture": "brokenpipe.png",
    "user_after_picture": null
  },
  {
    "title": "Broken Pipe",
    "description": "A pipe in my bathroom is leaky",
    "category": "plumbing",
    "user_before_picture": "brokenpipe.png",
    "user_after_picture": null
  },
  {
    "title": "Broken Pipe",
    "description": "A pipe in my bathroom is leaky",
    "category": "plumbing",
    "user_before_picture": "brokenpipe.png",
    "user_after_picture": null
  },
  {
    "title": "Broken Pipe",
    "description": "A pipe in my bathroom is leaky",
    "category": "plumbing",
    "user_before_picture": "brokenpipe.png",
    "user_after_picture": null
  },
  {
    "title": "Broken Pipe",
    "description": "A pipe in my bathroom is leaky",
    "category": "plumbing",
    "user_before_picture": "brokenpipe.png",
    "user_after_picture": null
  },
  {
    "title": "Broken Pipe",
    "description": "A pipe in my bathroom is leaky",
    "category": "plumbing",
    "user_before_picture": "brokenpipe.png",
    "user_after_picture": null
  },
  {
    "title": "Broken Pipe",
    "description": "A pipe in my bathroom is leaky",
    "category": "plumbing",
    "user_before_picture": "brokenpipe.png",
    "user_after_picture": null
  },
  {
    "title": "Broken Pipe",
    "description": "A pipe in my bathroom is leaky",
    "category": "plumbing",
    "user_before_picture": "brokenpipe.png",
    "user_after_picture": null
  },
  {
    "title": "Broken Pipe",
    "description": "A pipe in my bathroom is leaky",
    "category": "plumbing",
    "user_before_picture": "brokenpipe.png",
    "user_after_picture": null
  },
  {
    "title": "Broken Pipe",
    "description": "A pipe in my bathroom is leaky",
    "category": "plumbing",
    "user_before_picture": "brokenpipe.png",
    "user_after_picture": null
  },
  {
    "title": "Broken Pipe",
    "description": "A pipe in my bathroom is leaky",
    "category": "plumbing",
    "user_before_picture": "brokenpipe.png",
    "user_after_picture": null
  },
  {
    "title": "Broken Pipe",
    "description": "A pipe in my bathroom is leaky",
    "category": "plumbing",
    "user_before_picture": "brokenpipe.png",
    "user_after_picture": null
  },
  {
    "title": "Broken Pipe",
    "description": "A pipe in my bathroom is leaky",
    "category": "plumbing",
    "user_before_picture": "brokenpipe.png",
    "user_after_picture": null
  },
  {
    "title": "Broken Pipe",
    "description": "A pipe in my bathroom is leaky",
    "category": "plumbing",
    "user_before_picture": "brokenpipe.png",
    "user_after_picture": null
  },
  {
    "title": "Broken Pipe",
    "description": "A pipe in my bathroom is leaky",
    "category": "plumbing",
    "user_before_picture": "brokenpipe.png",
    "user_after_picture": null
  },
  {
    "title": "Broken Pipe",
    "description": "A pipe in my bathroom is leaky",
    "category": "plumbing",
    "user_before_picture": "brokenpipe.png",
    "user_after_picture": null
  },
  {
    "title": "Broken Pipe",
    "description": "A pipe in my bathroom is leaky",
    "category": "plumbing",
    "user_before_picture": "brokenpipe.png",
    "user_after_picture": null
  },
  {
    "title": "Broken Pipe",
    "description": "A pipe in my bathroom is leaky",
    "category": "plumbing",
    "user_before_picture": "brokenpipe.png",
    "user_after_picture": null
  },
  {
    "title": "newly uploaded project",
    "description": "this is the third project",
    "category": "plumbing",
    "user_before_picture": "picture.png",
    "user_after_picture": null
  }
]
```

## <a name="get_project_suggestions_via_contractor_id"></a>Get Project Suggestions via Contractor ID
`https://fixup-backend.herokuapp.com/api/v1/projects?contractor_id=1&limit=5`

A GET request to `/api/v1/contractors/:id/projects?contractor_id=:id&limit=limit_quantity` which takes no body.

Example Request:
```
GET https://fixup-backend.herokuapp.com/api/v1/projects?contractor_id=1&limit=5
```

Example Response:
```
Status: 200 OK
[
  {
    "id": 11,
    "title": "Broken Pipe",
    "description": "A pipe in my bathroom is leaky",
    "category": "plumbing",
    "user_before_picture": "brokenpipe.png",
    "user_after_picture": null
  },
  {
    "id": 12,
    "title": "Broken Pipe",
    "description": "A pipe in my bathroom is leaky",
    "category": "plumbing",
    "user_before_picture": "brokenpipe.png",
    "user_after_picture": null
  },
  {
    "id": 13,
    "title": "Broken Pipe",
    "description": "A pipe in my bathroom is leaky",
    "category": "plumbing",
    "user_before_picture": "brokenpipe.png",
    "user_after_picture": null
  },
  {
    "id": 14,
    "title": "Broken Pipe",
    "description": "A pipe in my bathroom is leaky",
    "category": "plumbing",
    "user_before_picture": "brokenpipe.png",
    "user_after_picture": null
  },
  {
    "id": 15,
    "title": "Broken Pipe",
    "description": "A pipe in my bathroom is leaky",
    "category": "plumbing",
    "user_before_picture": "brokenpipe.png",
    "user_after_picture": null
  }
]
```


## <a name="swiping_updates_contractor_choice"></a>Swiping Updates Contractor Choice
Left Swipe:
`https://fixup-backend.herokuapp.com/api/v1/contractors/1/projects/1`
```
{
	"contractor_choice": 1
}
```

Right Swipe:
`https://fixup-backend.herokuapp.com/api/v1/contractors/1/projects/1`
```
{
	"contractor_choice": 2
}
```

Left swipe: a PATCH request to `/api/v1/contractors/contractor_id/projects/project_id` which takes a body.

Right swipe: a PATCH request to `/api/v1/contractors/contractor_id/projects/project_id` which takes a body.

Example Swipe LEFT Request:
```
PATCH https://fixup-backend.herokuapp.com/api/v1/contractors/1/projects/1
Body:
{
	"contractor_choice": 1
}
```

Example Swipe LEFT Response:
```
{
  "message": "contractor_project contractor_choice updated to 1"
}
```

Example Swipe RIGHT Request:
```
PATCH https://fixup-backend.herokuapp.com/api/v1/contractors/1/projects/1
Body:
{
	"contractor_choice": 2
}
```

Example Swipe RIGHT Response:
```
{
  "message": "contractor_project contractor_choice updated to 2"
}
```


## <a name="update_user_choice"></a>User Selects Contractor
`https://fixup-backend.herokuapp.com/api/v1/projects/1/contractors/1?user_choice=True`

A PATCH request to `/api/v1/projects/project_id/contractors/contractor_id?user_choice=True` which takes a body.

Example Request:
```
PATCH https://fixup-backend.herokuapp.com/api/v1/projects/1/contractors/1
Body:
{
	"user_choice": "True"
}
```

Example Response:
```
{
  "message": "You've been Fixed Up!",
  "contractor": {
    "name": "Plumbing Person",
    "email": "plumbing@gmail.com",
    "phone_number": "7205555555",
    "zip": "80555",
    "category": "plumbing",
    "logo": "plumbinglogo.png"
  },
  "project": {
    "title": "Broken Pipe",
    "description": "A pipe in my bathroom is leaky",
    "category": "plumbing",
    "user_before_picture": "brokenpipe.png",
    "user_after_picture": null
  },
  "user": {
    "full_name": "Mario Mario",
    "email": "jumpman@gmail.com",
    "phone_number": "3035555555",
    "zip": "80555"
  }
}
```

## <a name="update_seen_boolean"></a>Contractor Sees Project For First Time
`https://fixup-backend.herokuapp.com/api/v1/contractors/1/projects/1`

A PATCH request to `/api/v1/contractors/:id/projects/:id` which takes a body.

Example Request:
```
PATCH https://fixup-backend.herokuapp.com/api/v1/contractors/1/projects/1

Body; raw, JSON(application/json):
{
  "seen": "True"
}
```

Example Response:
```
Status: 200 OK
{
  "message": "Contractor's project marked as 'seen'"
}
```


## <a name="single_user_project"></a>User Sees One of Their Projects

A GET request to
`/api/v1/users/:user_id/projects/:project_id` which takes no body

Example Request:
```
GET https://fixup-backend.herokuapp.com/api/v1/users/1/projects/1
```

Example Response:
```
Status: 200 OK

{
	"user_id": 1,
	"project": {
		"id": 1,
		"title": "Broken Pipe",
		"description": "My pipe burst and I have a water leak",
		"picture": "pipe.png"
	}
}
