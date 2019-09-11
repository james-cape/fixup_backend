+ [Create a User](#create_user)
+ [Create a Contractor](#create_contractor)
+ [See a single Contractor](#see_a_single_contractor)
+ [Update a Contractor](#update_contractor)
+ [Create a Project](#create_project)
+ [See User Show](#see_user_show)
+ [See Project Show](#see_project_show)
+ [See Projects By User](#see_projects_by_user)
+ [See Projects By Contractor](#see_projects_by_contractor)
+ [Get Batch of Projects via Contractor ID](#get_batch_of_projects_via_contractor_id)
+ [Get Project Suggestions via Contractor ID](#get_project_suggestions_via_contractor_id)
+ [Swiping Updates Contractor Choice](#swiping_updates_contractor_choice)
+ [User Selects Contractor](#update_user_choice)
+ [Contractor Sees Project For First Time](#update_seen_boolean)



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


# <a name="see_a_single_contractor"></a>See a Single Contractor
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


# <a name="update_contractor"></a>Update a Contractor
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


# <a name="see_user_show"></a>See User Show
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


# <a name="see_project_show"></a>See Project Show
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


# <a name="see_projects_by_user"></a>See Projects By User
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


# <a name="see_projects_by_contractor"></a>See Projects By Contractor
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


# <a name="get_batch_of_projects_via_contractor_id"></a>Get Batch of Projects via Contractor ID
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

# <a name="get_project_suggestions_via_contractor_id"></a>Get Project Suggestions via Contractor ID
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


# <a name="swiping_updates_contractor_choice"></a>Swiping Updates Contractor Choice
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


# <a name="update_user_choice"></a>User Selects Contractor
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

# <a name="update_seen_boolean"></a>Contractor Sees Project For First Time
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
