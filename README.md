# BackendFinalProject
API Specification
 -- Sophia Tan

----BOOK ROUTES------

Get all books
GET /api/books/

Response
{
    "success": true,
    "data": [
        {
            "id": 1,
            "title": "The Phantom Tollbooth",
            "author": "Norton Juster",
            "reviews": [ <SERIALIZED REVIEW WITHOUT BOOK FIELD>, ... ],
            "users_who_read": [ <SERIALIZED USER WITHOUT NAME, FAVORITE_BOOK, READ OR RECOMMENDED_BOOKS FIELDS>, ... ],
            "recommending_users": [ <SERIALIZED USER WITHOUT NAME, FAVORITE_BOOK, READ OR RECOMMENDED_BOOKS FIELDS>, ... ]
        },
        {
            "id": 2,
            "title": "White Fang",
            "author": "Jack London",
            "reviews": [ <SERIALIZED REVIEW WITHOUT BOOK FIELD>, ... ],
            "users_who_read": [ <SERIALIZED USER WITHOUT NAME, FAVORITE_BOOK, READ OR RECOMMENDED_BOOKS FIELDS>, ... ],
            "recommending_users": [ <SERIALIZED USER WITHOUT NAME, FAVORITE_BOOK, READ OR RECOMMENDED_BOOKS FIELDS>, ... ]
        }
        ...
    ]
}

Create a book
POST /api/books/

Request
{
    "title": <USER INPUT>,
    "author": <USER INPUT>
}

Response
{
    "success": true,
    "data": {
        "id": <ID>,
        "title": <USER INPUT FOR TITLE>,
        "author": <USER INPUT FOR AUTHOR>,
        "reviews": [],
        "users_who_read": [],
        "recommending_users": []
    }
}



















