# BackendFinalProject
## API Specification
###### by Sophia Tan #

### Book Routes #
*** 

#### Get all books
#### GET /api/books/

##### Response #
<pre><code>{
    "success": true,
    "data": [
        {
            "id": 1,
            "title": "The Phantom Tollbooth",
            "author": "Norton Juster",
            "reviews": [ &lt;SERIALIZED REVIEW WITHOUT BOOK FIELD>, ... ],
            "users_who_read": [ &lt;SERIALIZED USER WITHOUT NAME, FAVORITE_BOOK, READ OR RECOMMENDED_BOOKS FIELDS>, ... ],
            "recommending_users": [ &lt;SERIALIZED USER WITHOUT NAME, FAVORITE_BOOK, READ OR RECOMMENDED_BOOKS FIELDS>, ... ]
        },
        {
            "id": 2,
            "title": "White Fang",
            "author": "Jack London",
            "reviews": [ &lt;SERIALIZED REVIEW WITHOUT BOOK FIELD>, ... ],
            "users_who_read": [ &lt;SERIALIZED USER WITHOUT NAME, FAVORITE_BOOK, READ OR RECOMMENDED_BOOKS FIELDS>, ... ],
            "recommending_users": [ &lt;SERIALIZED USER WITHOUT NAME, FAVORITE_BOOK, READ OR RECOMMENDED_BOOKS FIELDS>, ... ]
        }
        ...
    ]
}
</code></pre>

#### Create a book #
#### POST /api/books/ #

##### Request #
<pre><code>{
    "title": &lt;USER INPUT>,
    "author": &lt;USER INPUT>
}
</code></pre>

##### Response
<pre><code>{
    "success": true,
    "data": {
        "id": &lt;ID>,
        "title": &lt;USER INPUT FOR TITLE>,
        "author": &lt;USER INPUT FOR AUTHOR>,
        "reviews": [],
        "users_who_read": [],
        "recommending_users": []
    }
}
</code></pre>

#### Get a Specific Book #
#### GET /api/books/{id}/ #

##### Response #
<pre><code>
{
    "success": true,
    "data": {
        "id": &lt;ID>,
        "title": &lt;USER INPUT FOR TITLE>,
        "author": &lt;USER INPUT FOR AUTHOR>,
        "reviews": [ &lt;SERIALIZED REVIEW WITHOUT BOOK FIELD>, ... ],
        "users_who_read": [ &lt;SERIALIZED USER WITHOUT NAME, FAVORITE_BOOK, READ OR RECOMMENDED_BOOKS FIELDS>, ... ],
        "recommending_users": [ &lt;SERIALIZED USER WITHOUT NAME, FAVORITE_BOOK, READ OR RECOMMENDED_BOOKS FIELDS>, ... ]
    }
}
</code></pre>

#### Delete a specific book #
#### DELETE /api/books/{id}/ #

##### Response #
<pre><code>
{
    "success": true,
    "data": {
        "id": &lt;ID>,
        "title": &lt;USER INPUT FOR TITLE>,
        "author": &lt;USER INPUT FOR AUTHOR>,
        "reviews": [ &lt;SERIALIZED REVIEW WITHOUT BOOK FIELD>, ... ],
        "users_who_read": [ &lt;SERIALIZED USER WITHOUT NAME, FAVORITE_BOOK, READ OR RECOMMENDED_BOOKS FIELDS>, ... ],
        "recommending_users": [ &lt;SERIALIZED USER WITHOUT NAME, FAVORITE_BOOK, READ OR RECOMMENDED_BOOKS FIELDS>, ... ]
    }
}
</code></pre>

### User Routes #
*** 

#### Get all users #
#### GET /api/users/

##### Response #
<pre><code>
{   "success": true,
    "data": [
        {
            "id": 1,
            "name": "Sophia Tan",
            "username": "Lopkit",
            "favorite_book": "The Phantom Tollbooth",
            "read": [ &lt;SERIALIZED BOOK WITHOUT AUTHOR, REVIEWS, USERS_WHO_READ, AND RECOMMENDING_USERS FIELDS>, ... ], 
            "recommended_books": [ &lt;SERIALIZED BOOK WITHOUT AUTHOR, REVIEWS, USERS_WHO_READ, AND RECOMMENDING_USERS FIELDS>, ... ]
        },
        {
            "id": 2,
            "name": "Mehal Kashyap",
            "username": "Banana",
            "favorite_book": "Walden",
            "read": [ &lt;SERIALIZED BOOK WITHOUT AUTHOR, REVIEWS, USERS_WHO_READ, AND RECOMMENDING_USERS FIELDS>, ... ], 
            "recommended_books": [ &lt;SERIALIZED BOOK WITHOUT AUTHOR, REVIEWS, USERS_WHO_READ, AND RECOMMENDING_USERS FIELDS>, ... ]
        }
        ...
    ]
}
            

    
</code></pre>

















