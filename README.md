# BackendFinalProject — API Specification #
###### URL: <http://34.86.12.80/> 
###### by Sophia Tan #

## Book Routes #
*** 

### Get all books
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
*** 

### Create a book #
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
*** 

### Get a Specific Book #
#### GET /api/books/{book_id}/ #

##### Response #
<pre><code>{
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
*** 

### Delete a specific book #
#### DELETE /api/books/{book_id}/ #

##### Response #
<pre><code>{
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

## User Routes #
*** 

### Get all users #
#### GET /api/users/

##### Response #
<pre><code>{   
    "success": true,
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
*** 

### Get a specific user #
#### GET /api/users/{user_id}/ #

##### Response #
<pre><code>{
    "success": true,
    "data": {
        "id": &lt;ID>,
        "name": &lt;USER INPUT FOR NAME>,
        "username": &lt;USER INPUT FOR USERNAME>,
        "favorite_book": &lt;USER INPUT FOR FAVORITE BOOK OR NULL>
        "read": [ &lt;SERIALIZED BOOK WITHOUT AUTHOR, REVIEWS, USERS_WHO_READ, AND RECOMMENDING_USERS FIELDS>, ... ], 
        "recommended_books": [ &lt;SERIALIZED BOOK WITHOUT AUTHOR, REVIEWS, USERS_WHO_READ, AND RECOMMENDING_USERS FIELDS>, ... ]
    }
}
</code></pre>
***

### Create a user #
#### POST /api/users/ #

##### Request #
<pre><code>{
    "name": &lt;USER INPUT>,
    "username": &lt;USER INPUT>,
    "favorite_book": &lt;USER INPUT OR NULL>,
}
</code></pre>

##### Response #
<pre><code>{
    "success": true,
    "data": {
        "id": &lt;ID>,
        "name": &lt;USER INPUT FOR NAME>,
        "username": &lt;USER INPUT FOR USERNAME>,
        "favorite_book": &lt;USER INPUT FOR FAVORITE_BOOK OR NULL>,
        "read": [],
        "recommended_books": []
    }
}
</code></pre>
***

### Add a user to recommending list/ book to recommended list #
#### POST /api/books/{book_id}/add/

##### Request #
<pre><code>{
    "user_id": &lt;USER INPUT>
}
</code></pre>

##### Response #
<pre><code>{
    "success": true,
    "data": &lt;SERIALIZED USER>
}
</code></pre>
***

### Update favorite book #
#### UPDATE api/users/{user_id}/ #

##### Request #
<pre><code>{
    "favorite_book": &lt;USER INPUT>
}
</code></pre>

##### Response #
<pre><code>{
    "success": true,
    "data": {
        "id": &lt;ID>,
        "name": &lt;USER INPUT FOR NAME>,
        "username": &lt;USER INPUT FOR USERNAME>,
        "favorite_book": &lt;USER INPUT FOR FAVORITE BOOK>,
        "read": [ &lt;SERIALIZED BOOK WITHOUT AUTHOR, REVIEWS, USERS_WHO_READ, AND RECOMMENDING_USERS FIELDS>, ... ], 
        "recommended_books": [ &lt;SERIALIZED BOOK WITHOUT AUTHOR, REVIEWS, USERS_WHO_READ, AND RECOMMENDING_USERS FIELDS>, ... ]
    }
}
</code></pre>
***

### Delete recommended book/recommending user #
#### POST /api/users/{user_id}/delete_recommended/ #

##### Request #
<pre><code>{
    "book_id": &lt;USER INPUT>
}
</code></pre>

##### Response #
<pre><code>{
    "success": true,
    "data": &lt;SERIALIZED USER>
}
</code></pre>
***

### Add book to read list #
#### POST /api/users/{user_id}/add_read/ #

##### Request #
<pre><code>{
    "book_id": &lt;USER INPUT>
}
</code></pre>

##### Response #
<pre><code>{
    "success": true,
    "data": &lt;SERIALIZED USER>
}
</code></pre>

## Review Routes #
***

### Create a review #
#### POST /api/books/{book_id}/review/ #

##### Request #
<pre><code>{
    "username": &lt;USER INPUT>,
    "review": &lt;USER INPUT>,
    "recommend": "Yes" or "No"
}
</code></pre>

##### Response #
<pre><code>{
    "success": true,
    "data": {
        "id": &lt;ID>,
        "username": &lt;USER INPUT FOR USERNAME>,
        "review":  &lt;USER INPUT FOR REVIEW>,
        "recommend": &lt;USER INPUT FOR RECOMMEND>,
        "book": &lt;SERIALIZED BOOK WITHOUT REVIEWS, USERS_WHO_READ, OR RECOMMENDING_USERS FIELDS>
    }
}
</code></pre>
***

### Update review #
#### POST /api/reviews/{review_id}/update/

##### Request #
<pre><code>{
    "review" &lt;USER INPUT OR NULL>,
    "recommend": &lt;YES, NO, OR NULL>
}
</pre></code>

##### Response #
<pre><code>{
    "success": true,
    "data": &lt;SERIALIZED REVIEW>
}
</pre></code
***

### Delete review #
#### DELETE /api/reviews/{review_id}/

##### Response #
<pre><code>{
    "success": true,
    "data": {
        "id": &lt;ID>,
        "username": &lt;USER INPUT FOR USERNAME>,
        "review": &lt;USER INPUT FOR REVIEW>,
        "recommend": &lt;USER INPUT FOR RECOMMEND>,
        "book": &lt;SERIALIZED BOOK WITHOUT REVIEWS, USERS_WHO_READ, OR RECOMMENDING_USERS FIELDS>
    }
}
</code></pre>



